import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# Carregar os dados
df = pd.read_excel('Amostra_apos_Box_Plox.xlsx')

# Criar Variáveis Compostas
df['Suporte_Social'] = df['Item 3'] + df['Item 4'] + df['Item 5']
df['Estresse_Total'] = df['Item 6'] + df['Item 7']

# Columnas para análise
variables = {
    'Carga Horária': 'Item 1',
    'Horas de Sono': 'Item 2',
    'Suporte Social': 'Suporte_Social',
    'Estresse': 'Estresse_Total'
}

# Definir figura para os dendrogramas
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()
stats_text = ""

for i, (label, col) in enumerate(variables.items()):
    ax = axes[i]
    
    X = df[[col]].values
    
    Z = linkage(X, method='ward')
    
    dendrogram(Z, ax=ax, truncate_mode='lastp', p=12, leaf_rotation=90., leaf_font_size=8., show_contracted=True)
    ax.set_title(f'Dendrograma - {label}')
    ax.set_xlabel('Amostras')
    ax.set_ylabel('Distância')
    
     # Atribuir clusters (k=3)
    clusters = fcluster(Z, t=3, criterion='maxclust')
    df[f'Cluster_{col}'] = clusters
    
    # Calcular estatísticas por cluster
    group_stats = df.groupby(f'Cluster_{col}')[col].agg(['mean', 'count', 'min', 'max']).sort_values('mean')
    
    stats_text += f"\n--- {label} ---\n"
    stats_text += group_stats.to_string() + "\n"

plt.tight_layout()
plt.savefig('dendrogramas_por_variavel.png')
print(stats_text)