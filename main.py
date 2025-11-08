import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Deixar os gráficos mais bonitos
sns.set(style="whitegrid")

# Caminho do arquivo CSV
caminho_csv = "dados/funcionarios.csv"

# Ler o CSV
df = pd.read_csv(caminho_csv)

print("Primeiras linhas:")
print(df.head())

print("\nInfo do DataFrame:")
print(df.info())

print("\nQuantidade de linhas antes de remover duplicados:", len(df))
df = df.drop_duplicates()
print("Quantidade de linhas depois de remover duplicados:", len(df))

print("\nValores ausentes por coluna:")
print(df.isna().sum())

# Tratar valores ausentes
# Preencher salário com a mediana
if df['salario'].isna().sum() > 0:
    mediana_salario = df['salario'].median()
    df['salario'] = df['salario'].fillna(mediana_salario)

# Preencher idade com a média
if df['idade'].isna().sum() > 0:
    media_idade = df['idade'].mean()
    df['idade'] = df['idade'].fillna(media_idade)

print("\nValores ausentes após tratamento:")
print(df.isna().sum())

# Converter data_admissao para datetime
df['data_admissao'] = pd.to_datetime(df['data_admissao'], errors='coerce')

# Remover linhas sem data de admissão válida (se tiver)
df = df.dropna(subset=['data_admissao'])

# Criar coluna tempo de casa em anos
df['tempo_casa'] = (pd.Timestamp.today() - df['data_admissao']).dt.days / 365

print("\nDescrição das variáveis numéricas:")
print(df[['idade', 'salario', 'tempo_casa']].describe())

print("\nMatriz de correlação (idade, tempo_casa, salario):")
corr = df[['idade', 'tempo_casa', 'salario']].corr()
print(corr)

os.makedirs("relatorios/graficos", exist_ok=True)

# Histograma de salários
plt.figure(figsize=(8, 5))
sns.histplot(df['salario'], kde=True)
plt.title("Distribuição dos Salários")
plt.xlabel("Salário (R$)")
plt.ylabel("Frequência")
plt.tight_layout()
plt.savefig("relatorios/graficos/distribuicao_salario.png")
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='cargo', y='salario', data=df)
plt.title("Distribuição de Salário por Cargo")
plt.xlabel("Cargo")
plt.ylabel("Salário (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("relatorios/graficos/salario_por_cargo.png")
plt.close()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="Blues")
plt.title("Mapa de Correlação: Idade x Tempo de Casa x Salário")
plt.tight_layout()
plt.savefig("relatorios/graficos/correlacao.png")
plt.close()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='idade', y='salario', data=df)
plt.title("Relação entre Idade e Salário")
plt.xlabel("Idade")
plt.ylabel("Salário (R$)")
plt.tight_layout()
plt.savefig("relatorios/graficos/idade_vs_salario.png")
plt.close()

df.to_csv("dados/funcionarios_limpo.csv", index=False)
print("\nArquivo 'funcionarios_limpo.csv' salvo em dados/")
