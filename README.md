# 📊 Projeto – Limpeza e Exploração de Dados de RH (Python + Seaborn)

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

