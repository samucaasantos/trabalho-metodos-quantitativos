import pandas as pd
import matplotlib.pyplot as plt

# carregar os dados
df = pd.read_excel('Amostra_apos_Box_Plox.xlsx')

# Criar Variáveis Compostas
df['Suporte_Social'] = df['Item 3'] + df['Item 4'] + df['Item 5']
df['Estresse_Total'] = df['Item 6'] + df['Item 7']

# Definir Categorias
df['Cat_Sono'] = pd.cut(df['Item 2'], bins=[-1, 5.9, 7.9, 24], labels=['Baixo (<6h)', 'Médio (6-8h)', 'Alto (>8h)'])
df['Cat_Carga'] = pd.cut(df['Item 1'], bins=[-1, 2.9, 6.9, 100], labels=['Baixa (0-2h)', 'Média (3-6h)', 'Alta (>6h)'])
df['Cat_Estresse'] = pd.cut(df['Estresse_Total'], bins=[-1, 4.9, 9.9, 20], labels=['Baixo (0-4)', 'Médio (5-9)', 'Alto (10-14)'])
df['Cat_Suporte'] = pd.cut(df['Suporte_Social'], bins=[-1, 7.9, 14.9, 30], labels=['Baixo (0-7)', 'Médio (8-14)', 'Alto (15-21)'])

# Plotting
fig, axes = plt.subplots(2, 2, figsize=(14, 11)) # Increased height slightly
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# Função para plotar cada categoria
def plot_cat(col, ax, title, color):
    counts = df[col].value_counts().sort_index()
    total = len(df)
    bars = ax.bar(counts.index, counts.values, color=color, edgecolor='black', alpha=0.7)
    
    # Definir limite y dinamicamente
    if len(counts) > 0:
        max_height = counts.max()
        ax.set_ylim(0, max_height * 1.25)
    
    ax.set_title(title, fontsize=12, fontweight='bold', pad=15) 
    ax.set_ylabel('Frequência')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        perc = (height / total) * 100
        # Checar se a altura é maior que zero antes de anotar
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height + (max_height * 0.02),
                    f'{int(height)}\n({perc:.1f}%)',
                    ha='center', va='bottom', fontsize=10)

# 1. Carga Horária
plot_cat('Cat_Carga', axes[0, 0], 'Distribuição de Carga Horária', 'skyblue')

# 2. Sono
plot_cat('Cat_Sono', axes[0, 1], 'Distribuição de Horas de Sono', 'lightgreen')

# 3. Suporte Social
plot_cat('Cat_Suporte', axes[1, 0], 'Distribuição de Suporte Social', 'salmon')

# 4. Estresse
plot_cat('Cat_Estresse', axes[1, 1], 'Distribuição de Níveis de Estresse', 'orange')

fig.suptitle('Agrupamento por Variável (Segmentação da Amostra)', fontsize=16, y=0.95)
plt.savefig('agrupamento_por_variavel.png', bbox_inches='tight')
plt.close()