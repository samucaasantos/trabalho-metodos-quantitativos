import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.max_columns', None)
df = pd.read_excel('Box_Plot.xlsx')
print(df.head())
print(df.columns)
print(df.describe())


# Calcular IQR and identificar outliers para Item 1 e Item 2
outliers_dict = {}

for col in ['Item 1', 'Item 2']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    if not outliers.empty:
        outliers_dict[col] = outliers[['Indivíduo', col]].values.tolist()

print("Outliers found:", outliers_dict)


# Criar boxplot para Item 1 e Item 2
plt.figure(figsize=(10, 6))

# gráfico do boxplot do Item 1 e Item 2 
sns.boxplot(data=df[['Item 1', 'Item 2']])
plt.title('Distribuição e Outliers - Itens 1 e 2')
plt.ylabel('Valores (Horas)')
plt.xlabel('Variáveis')
plt.grid(True, linestyle='--', alpha=0.7)

# Salvar o gráfico
plt.savefig('boxplot_outliers.png')