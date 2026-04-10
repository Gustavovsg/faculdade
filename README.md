# 📊 Atividade 3 - Análise de Dataset de Livros

## 🧾 Descrição

Este projeto realiza uma análise exploratória e tratamento de dados de um dataset de livros utilizando **Python** e **Pandas**. O objetivo é limpar, organizar e extrair informações relevantes a partir dos dados.

---

## ▶️ Como executar o projeto

### 1. Baixar o projeto pelo GitHub

1. Acesse o repositório no GitHub  
2. Clique no botão verde **"Code"**  
3. Clique em **"Download ZIP"**  
4. Extraia o arquivo no seu computador  

---

### 2. Acessar a pasta do projeto

Abra a pasta extraída.

---

### 3. Instalar as dependências

Certifique-se de ter o Python 3.8 ou superior instalado.

Abra o terminal dentro da pasta do projeto e execute:

pip install pandas numpy openpyxl

---

### 4. Executar o projeto

No terminal:

python main.py

---

## ⚙️ Funcionalidades

### 📥 Carregamento de dados

* Leitura do arquivo `livros.csv` utilizando separador `;`
* Visualização inicial dos dados

---

### 🔍 Análise exploratória

* Estrutura do dataset (`info()`)
* Estatísticas descritivas (`describe()`)

---

### 🧹 Tratamento de dados

* Identificação de valores nulos  
* Remoção de registros com `paginas == 0`  
* Preenchimento de valores nulos na coluna `ano` com a mediana  
* Ajuste de tipos de dados  

---

### 🏷️ Engenharia de atributos

* Criação da coluna **faixa_paginas**:
  - Curto (<150)  
  - Médio (150–350)  
  - Longo (>350)  

* Criação da coluna **decada** com base no ano de publicação  

---

### 📊 Análises realizadas

* Média de páginas por década  
* Top 10 autores com mais livros  
* Distribuição de livros por faixa de páginas após 2010  

---

### 📤 Exportação

* Geração do arquivo `livros_analisados.xlsx`  

---

## 📁 Estrutura do projeto

📂 projeto  
┣ 📄 livros.csv  
┣ 📄 main.py  
┗ 📄 README.md  

---

## 🧠 Observações

* O sistema realiza tratamento automático dos dados  
* Registros inválidos (como páginas iguais a zero) são removidos  
* Valores ausentes são tratados automaticamente  
* É necessário ter o `openpyxl` instalado para exportar arquivos Excel  

---

## 🚀 Tecnologias utilizadas

* Python  
* Pandas  
* NumPy  
* OpenPyXL  

---

## 📌 Autor

Gustavo Vinicius de Sousa Galvao - 202308423304  
