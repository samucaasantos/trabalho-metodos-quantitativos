import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

# Carregar os dados
df = pd.read_excel('Amostra_apos_Box_Plox.xlsx')

# Creiar Variáveis Compostas
df['Suporte_Social'] = df['Item 3'] + df['Item 4'] + df['Item 5']
df['Estresse_Total'] = df['Item 6'] + df['Item 7']

# Colunas para análise
X_cols = ['Item 1', 'Item 2', 'Suporte_Social']
y_col = 'Estresse_Total'

labels_map = {
    'Item 1': 'Carga Horária',
    'Item 2': 'Horas de Sono',
    'Suporte_Social': 'Suporte Social',
    'Estresse_Total': 'Estresse (Dep.)'
}
df_renamed = df.rename(columns=labels_map)
analyze_cols = list(labels_map.values())

# --- IMAGEM 1---
summary = df_renamed[analyze_cols].describe().T
summary['Moda'] = df_renamed[analyze_cols].mode().iloc[0]
summary['Variância'] = df_renamed[analyze_cols].var()
summary['Assimetria'] = df_renamed[analyze_cols].skew()
summary['Curtose'] = df_renamed[analyze_cols].kurt()
summary = summary[['mean', '50%', 'Moda', 'Variância', 'std', 'min', 'max', 'Assimetria', 'Curtose']]
summary.columns = ['Média', 'Mediana', 'Moda', 'Variância', 'Desvio Padrão', 'Mínimo', 'Máximo', 'Assimetria', 'Curtose']
summary = summary.round(2)

fig, ax = plt.subplots(figsize=(12, 4)) 
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=summary.values, colLabels=summary.columns, rowLabels=summary.index, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
plt.title('Tabela 3 - Estatística Descritiva (Gerada via Python)', y=0.8)
plt.savefig('tabela3_python.png', bbox_inches='tight', pad_inches=0.1)
plt.close()

# --- IMAGEM 2: CLUSTERING (Dendrograma & Perfis) ---
# Usando padronização
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[X_cols + [y_col]])
Z = linkage(X_scaled, method='ward')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Dendrograma
dendrogram(Z, ax=ax1, truncate_mode='lastp', p=12, leaf_rotation=90., leaf_font_size=10., show_contracted=True)
ax1.set_title('Dendrograma (Agrupamento Hierárquico)')
ax1.set_xlabel('Índices da Amostra (ou Cluster)')
ax1.set_ylabel('Distância (Ward)')

# Perfis de Cluster)
# Atribuir clusters (k=3)
from scipy.cluster.hierarchy import fcluster
df['Cluster'] = fcluster(Z, t=3, criterion='maxclust')
cluster_means = df.groupby('Cluster')[X_cols + [y_col]].mean()
# Normalizar para comparação visual
cluster_means_norm = (cluster_means - cluster_means.mean()) / cluster_means.std()

cluster_means_norm.T.plot(kind='bar', ax=ax2)
ax2.set_title('Perfil dos Clusters (Médias Padronizadas)')
ax2.set_xticklabels(['Carga', 'Sono', 'Suporte', 'Estresse'], rotation=0)
ax2.legend(title='Cluster')
plt.tight_layout()
plt.savefig('agrupamento_python.png')
plt.close()

# --- IMAGE 3: CORRELATION (Heatmap) ---
corr_matrix = df_renamed[analyze_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Matriz de Correlação de Pearson')
plt.savefig('correlacao_python.png')
plt.close()

# --- IMAGEM 4: REGRESSÂO (Plotagem de Coeficientes) ---
X = sm.add_constant(df[X_cols])
model = sm.OLS(df[y_col], X).fit()

# Pegar coeficientes e intervalos de confiança
coefs = model.params.drop('const')
conf_int = model.conf_int().drop('const')
errors = coefs - conf_int[0]

plt.figure(figsize=(8, 5))
coefs.plot(kind='barh', xerr=errors, capsize=5, color='skyblue', edgecolor='black')
plt.axvline(x=0, color='red', linestyle='--')
plt.title('Coeficientes da Regressão (Impacto no Estresse)')
plt.xlabel('Valor do Coeficiente (Beta)')
plt.yticks(ticks=range(len(coefs)), labels=['Carga Horária', 'Sono', 'Suporte Social'])
plt.tight_layout()
plt.savefig('regressao_python.png')
plt.close()