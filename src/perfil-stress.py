import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
df = pd.read_excel('Amostra_apos_Box_Plox.xlsx')

# 2. Criar Variáveis Compostas
df['Suporte_Social'] = df['Item 3'] + df['Item 4'] + df['Item 5']
df['Estresse_Total'] = df['Item 6'] + df['Item 7']

# 3. Definir Categorias

df['Perfil_Carga'] = pd.cut(df['Item 1'], bins=[-1, 2.9, 6.9, 100], labels=['O Minimalista', 'O Padrão', 'O Stakhanovista'])
df['Perfil_Sono'] = pd.cut(df['Item 2'], bins=[-1, 5.9, 7.9, 24], labels=['O Zumbi', 'O Equilibrista', 'O Restaurado'])
df['Perfil_Suporte'] = pd.cut(df['Suporte_Social'], bins=[-1, 7.9, 14.9, 30], labels=['O Lobo', 'O Gregário', 'O Comunitário'])
df['Perfil_Estresse'] = pd.cut(df['Estresse_Total'], bins=[-1, 4.9, 9.9, 20], labels=['O Zen', 'O Tenso', 'O Colapso'])

# 4. Plotagem 
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
plt.subplots_adjust(hspace=0.4, wspace=0.3)

def plot_impact(col, ax, title, color_palette):
    # Calcular média de estresse por categoria
    means = df.groupby(col)['Estresse_Total'].mean()
    # Plotar
    sns.barplot(x=means.index, y=means.values, ax=ax, palette=color_palette, edgecolor='black')
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel('')
    ax.set_ylabel('Média de Estresse')
    ax.set_ylim(0, 12) # Escala fixa para comparação
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Adicionar valores nas barras
    for p in ax.patches:
        if p.get_height() > 0:
            ax.annotate(f'{p.get_height():.1f}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 9), 
                        textcoords = 'offset points',
                        fontsize=11, fontweight='bold')

# Plot 1: Carga
plot_impact('Perfil_Carga', axes[0, 0], 'A. Impacto da Carga Horária', 'Blues')

# Plot 2: Sono
plot_impact('Perfil_Sono', axes[0, 1], 'B. Impacto do Sono', 'Reds_r')

# Plot 3: Suporte
plot_impact('Perfil_Suporte', axes[1, 0], 'C. Impacto do Suporte Social', 'Greens_r')

# Plot 4: Validação do Estresse 
plot_impact('Perfil_Estresse', axes[1, 1], 'D. Validação dos Níveis de Estresse', 'Oranges')

plt.suptitle('Figura 7 – Níveis Médios de Estresse por Perfil Comportamental', fontsize=16, y=0.95)
plt.savefig('perfis_variaveis.png', bbox_inches='tight')
plt.show()

# Imprimir valores para conferência do texto
print("--- VALORES PARA O TEXTO ---")
print("Carga:\n", df.groupby('Perfil_Carga')['Estresse_Total'].mean())
print("Sono:\n", df.groupby('Perfil_Sono')['Estresse_Total'].mean())
print("Suporte:\n", df.groupby('Perfil_Suporte')['Estresse_Total'].mean())