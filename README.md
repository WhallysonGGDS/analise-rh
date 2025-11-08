# 📊 Projeto  – Limpeza e Exploração de Dados de RH (Python + Seaborn)

Este projeto simula uma análise de dados de Recursos Humanos, com foco em **limpeza de dados**, **tratamento de valores ausentes** e **análise exploratória** utilizando **Python, Pandas e Seaborn**.

---

## 🎯 Objetivo

O objetivo é treinar:

- Leitura e inspeção de dados com `pandas`
- Tratamento de valores **ausentes** e **duplicados**
- Conversão de tipos (datas, numéricos)
- Criação de variáveis derivadas (ex: `tempo_casa`)
- Análise de correlação entre:
  - **Idade**
  - **Tempo de casa**
  - **Salário**
- Criação de visualizações com `seaborn`:
  - Histograma
  - Boxplot
  - Heatmap
  - Scatterplot

---

## 🛠️ Tecnologias utilizadas

- Python 3.x  
- Pandas  
- NumPy  
- Seaborn  
- Matplotlib  
- Jupyter Notebook

---

## 📂 Estrutura do projeto

```text
analise_rh/
│
├── dados/
│   ├── funcionarios.csv          # Base de dados original (sintética)
│   └── funcionarios_limpo.csv    # Base tratada/limpa (gerada pelo código)
│
├── relatorios/
│   └── graficos/
│       ├── distribuicao_salario.png
│       ├── salario_por_cargo.png
│       ├── correlacao.png
│       └── idade_vs_salario.png
│
├── main.py           # Versão em script Python (opcional)
└── analise_rh.ipynb  # Notebook Jupyter com toda a análise passo a passo

⚙️ Como rodar o projeto
1. Clonar o repositório
git clone https://github.com/SEU-USUARIO/analise-rh.git
cd analise-rh

2. Criar ambiente virtual (opcional, mas recomendado)
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# Linux/Mac:
# source .venv/bin/activate

3. Instalar dependências
pip install -r requirements.txt


Obs: caso não exista o requirements.txt, você pode instalar manualmente:

pip install pandas seaborn matplotlib numpy

🧪 Como executar
🔹 Rodar via Notebook

Abrir o projeto no VS Code ou Jupyter

Abrir o arquivo analise_rh.ipynb

Executar célula por célula na ordem

🔹 Rodar via Script (main.py)
python main.py


Os gráficos serão salvos na pasta:

relatorios/graficos/


E o dataset limpo será salvo como:

dados/funcionarios_limpo.csv

📈 Análises realizadas

Tratamento de dados:

Remoção de linhas duplicadas

Preenchimento de:

salario com a mediana

idade com a média

Conversão de data_admissao para datetime

Criação da coluna tempo_casa (em anos)

Estatísticas descritivas:

Média, mediana, desvio padrão de idade, salário e tempo de casa

Correlação:

Matriz de correlação entre:

idade

tempo_casa

salario

Visualizações:

Histograma da distribuição de salários

Boxplot de salário por cargo

Heatmap da correlação

Scatterplot de idade x salário

🚀 Possíveis melhorias futuras

Adicionar segmentação por departamento/setor

Calcular turnover e tempo médio na empresa

Criar dashboard em Streamlit ou Power BI

Comparar salários por gênero, região, nível de cargo (em um dataset mais completo)
