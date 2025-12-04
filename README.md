# Análise Quantitativa: Estresse, Sono, Carga Horária e Suporte Social

Projeto de análise estatística e visualização de dados para investigar as relações entre carga horária de trabalho, horas de sono, suporte social e níveis de estresse em uma amostra de indivíduos.

## 📋 Descrição do Projeto

Este projeto realiza uma análise quantitativa abrangente explorando os fatores que influenciam o estresse psicológico. Utiliza técnicas estatísticas avançadas, análise de agrupamento hierárquico e regressão linear para identificar padrões e relações entre variáveis.

### Variáveis Principais

- **Item 1**: Carga Horária (horas de trabalho por semana)
- **Item 2**: Horas de Sono (horas de sono por noite)
- **Item 3, 4, 5**: Componentes de Suporte Social
- **Item 6, 7**: Componentes de Estresse

### Variáveis Compostas (Derivadas)

- **Suporte_Social**: Soma dos itens 3, 4 e 5 (escala 0-21)
- **Estresse_Total**: Soma dos itens 6 e 7 (escala 0-14)

---

## 📁 Estrutura do Projeto

```
codigos-graficos/
├── README.md                           # Este arquivo
├── src/                                # Scripts de análise
│   ├── agrupamento-por-variavel.py    # Segmentação da amostra
│   ├── analises.py                     # Análise descritiva e regressão
│   ├── box-plot-1.py                  # Identificação de outliers
│   ├── dendrograma-agrupamento-por-variavel.py  # Clustering por variável
│   └── perfil-stress.py               # Análise de perfis comportamentais
├── planilhas/                         # Dados originais
│   ├── Box_Plot.xlsx                  # Dados brutos para análise de outliers
│   └── Amostra_apos_Box_Plox.xlsx    # Dados tratados após remoção de outliers
└── imagens-geradas/                   # Gráficos e visualizações gerados
    ├── boxplot_outliers.png           # Box plot dos itens 1 e 2
    ├── agrupamento_por_variavel.png   # Distribuições categorizadas
    ├── agrupamento_python.png         # Dendrograma e perfis de clusters
    ├── dendrogramas_por_variavel.png  # Dendrogramas individuais por variável
    ├── tabela3_python.png             # Estatística descritiva completa
    ├── correlacao_python.png          # Heatmap de correlação de Pearson
    ├── regressao_python.png           # Coeficientes da regressão linear
    └── perfis_variaveis.png           # Impacto das variáveis no estresse

```

---

## 🔬 Scripts de Análise

### 1. **box-plot-1.py** - Detecção e Tratamento de Outliers
**Objetivo**: Identificar e visualizar valores atípicos nos dados brutos.

**Funcionalidade**:
- Calcula Intervalo Interquartil (IQR) para Item 1 e Item 2
- Identifica outliers usando critério 1.5 × IQR
- Gera visualização com box plots
- Lista indivíduos com valores anômalos

**Entrada**: `planilhas/Box_Plot.xlsx`  
**Saída**: `imagens-geradas/boxplot_outliers.png`

**Uso**:
```bash
python src/box-plot-1.py
```

---

### 2. **agrupamento-por-variavel.py** - Segmentação da Amostra
**Objetivo**: Criar categorias de segmentação para cada variável principal.

**Funcionalidade**:
- Categoriza carga horária em 3 níveis: Baixa (<6h), Média (3-6h), Alta (>6h)
- Categoriza sono em 3 níveis: Baixo (<6h), Médio (6-8h), Alto (>8h)
- Categoriza suporte social: Baixo (0-7), Médio (8-14), Alto (15-21)
- Categoriza estresse: Baixo (0-4), Médio (5-9), Alto (10-14)
- Exibe distribuição de frequências com percentuais

**Entrada**: `planilhas/Amostra_apos_Box_Plox.xlsx`  
**Saída**: `imagens-geradas/agrupamento_por_variavel.png`

**Uso**:
```bash
python src/agrupamento-por-variavel.py
```

---

### 3. **analises.py** - Análise Descritiva e Regressão
**Objetivo**: Executar análises estatísticas abrangentes do conjunto de dados.

**Funcionalidades**:

#### 3.1 Estatística Descritiva
- Calcula média, mediana, moda, variância, desvio padrão
- Calcula assimetria (skewness) e curtose
- Gera tabela com estatísticas completas

#### 3.2 Análise de Agrupamento (Clustering)
- Aplica dendrograma com método Ward (agrupamento hierárquico)
- Identifica 3 clusters automaticamente
- Calcula perfis de clusters (médias padronizadas)
- Visualiza distâncias e agrupamentos

#### 3.3 Análise de Correlação
- Calcula matriz de correlação de Pearson
- Visualiza com heatmap colorido
- Identifica relações entre variáveis

#### 3.4 Análise de Regressão Linear
- Modelo: `Estresse_Total ~ Carga Horária + Sono + Suporte Social`
- Calcula coeficientes Beta com intervalo de confiança
- Visualiza impacto de cada preditor no estresse

**Entrada**: `planilhas/Amostra_apos_Box_Plox.xlsx`  
**Saídas**: 
- `imagens-geradas/tabela3_python.png`
- `imagens-geradas/agrupamento_python.png`
- `imagens-geradas/correlacao_python.png`
- `imagens-geradas/regressao_python.png`

**Uso**:
```bash
python src/analises.py
```

---

### 4. **dendrograma-agrupamento-por-variavel.py** - Clustering Individual
**Objetivo**: Analisar agrupamentos específicos para cada variável de interesse.

**Funcionalidade**:
- Cria 4 dendrogramas (um para cada variável principal)
- Aplica agrupamento hierárquico de forma independente
- Calcula estatísticas descritivas por cluster:
  - Média do valor
  - Contagem de observações
  - Mínimo e máximo
- Exibe tabelas de desempenho de cada cluster

**Entrada**: `planilhas/Amostra_apos_Box_Plox.xlsx`  
**Saída**: `imagens-geradas/dendrogramas_por_variavel.png`

**Uso**:
```bash
python src/dendrograma-agrupamento-por-variavel.py
```

---

### 5. **perfil-stress.py** - Análise de Perfis Comportamentais
**Objetivo**: Quantificar o impacto de cada fator comportamental no nível de estresse.

**Funcionalidade**:
- Cria perfis nomeados para cada dimensão:
  - **Carga**: O Minimalista | O Padrão | O Stakhanovista
  - **Sono**: O Zumbi | O Equilibrista | O Restaurado
  - **Suporte**: O Lobo | O Gregário | O Comunitário
  - **Estresse**: O Zen | O Tenso | O Colapso
- Calcula média de estresse para cada perfil
- Visualiza em gráficos de barras com escala padronizada
- Permite comparação direta do impacto de cada fator

**Entrada**: `planilhas/Amostra_apos_Box_Plox.xlsx`  
**Saída**: `imagens-geradas/perfis_variaveis.png`

**Uso**:
```bash
python src/perfil-stress.py
```

---

## 📊 Dados

### Arquivos de Entrada

#### `planilhas/Box_Plot.xlsx`
- **Descrição**: Dados brutos originais
- **Uso**: Base para identificação e remoção de outliers
- **Colunas**: Indivíduo, Item 1, Item 2, ... Item 7

#### `planilhas/Amostra_apos_Box_Plox.xlsx`
- **Descrição**: Dados tratados após análise de outliers
- **Uso**: Base para todas as análises posteriores
- **Observações**: Indivíduos com valores extremos foram removidos ou ajustados

---

## 🛠️ Requisitos e Instalação

### Dependências Python

```
pandas
numpy
matplotlib
seaborn
scipy
statsmodels
scikit-learn
openpyxl
```

### Instalação

1. Clone ou baixe o repositório:
```bash
git clone https://github.com/samucaasantos/trabalho-metodos-quantitativos.git
cd codigos-graficos
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
venv\Scripts\activate  # No Windows
# ou: source venv/bin/activate  # No Linux/Mac
```

3. Instale as dependências:
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels scikit-learn openpyxl
```

---

## ▶️ Como Executar

### Executar um script individual:
```bash
python src/box-plot-1.py
python src/agrupamento-por-variavel.py
python src/analises.py
python src/dendrograma-agrupamento-por-variavel.py
python src/perfil-stress.py
```

### Executar todos os scripts:
```bash
for /r src %f in (*.py) do python "%f"  # Windows PowerShell
# ou: for script in src/*.py; do python "$script"; done  # Linux/Mac
```

---

## 📈 Principais Descobertas

Com base na estrutura do projeto, as seguintes análises são possíveis:

1. **Correlações**: Qual variável tem maior impacto no estresse?
2. **Segmentação**: Como a amostra se distribui em categorias de risco?
3. **Clusters**: Quais grupos de indivíduos compartilham padrões similares?
4. **Regressão**: Qual é o coeficiente de impacto de cada fator no estresse?
5. **Perfis**: Quais combinações de comportamentos geram maior estresse?

---

## 📌 Metodologia

### Métodos Estatísticos Utilizados

- **Estatística Descritiva**: Média, mediana, variância, assimetria, curtose
- **Box Plot**: Detecção de outliers com método IQR (Intervalo Interquartil)
- **Análise de Agrupamento Hierárquico**: Método Ward com distância Euclidiana
- **Correlação de Pearson**: Medida de associação linear entre variáveis
- **Regressão Linear Múltipla**: Modelo OLS (Ordinary Least Squares)
- **Padronização (Z-score)**: Normalização para análises comparativas

### Categorização de Variáveis

As variáveis contínuas foram transformadas em categorias ordinais para análise exploratória:
- Método: Binning com cut-offs baseados em percentis e literatura de domínio
- Propósito: Facilitar interpretação e segmentação da amostra

---

## 📁 Estrutura das Imagens Geradas

| Arquivo | Descrição | Script |
|---------|-----------|--------|
| `boxplot_outliers.png` | Distribuição de Item 1 e 2 com outliers | box-plot-1.py |
| `agrupamento_por_variavel.png` | 4 gráficos de frequência (Carga, Sono, Suporte, Estresse) | agrupamento-por-variavel.py |
| `agrupamento_python.png` | Dendrograma + Perfis de clusters | analises.py |
| `tabela3_python.png` | Tabela com estatísticas descritivas | analises.py |
| `correlacao_python.png` | Heatmap da matriz de correlação | analises.py |
| `regressao_python.png` | Coeficientes Beta com IC 95% | analises.py |
| `dendrogramas_por_variavel.png` | 4 dendrogramas individuais | dendrograma-agrupamento-por-variavel.py |
| `perfis_variaveis.png` | 4 gráficos de impacto no estresse | perfil-stress.py |

---

## 👥 Autor

**Samuel Assunção dos Santos**  
[GitHub](https://github.com/samucaasantos)

---

## 📝 Licença

Este projeto é fornecido como parte de um trabalho acadêmico de Métodos Quantitativos.

---

## 🤝 Contribuições

Sugestões de melhorias, correções ou extensões são bem-vindas. Abra uma issue ou pull request no repositório.

---

## 📞 Contato e Suporte

Para dúvidas sobre o projeto ou análises, consulte os comentários no código de cada script ou abra uma issue no repositório GitHub.

---

**Última atualização**: Dezembro de 2025
