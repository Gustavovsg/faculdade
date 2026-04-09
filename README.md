# 📊 Atividade 3 - Dashboard de Análise de Funcionários

## 🧾 Descrição

Este projeto é um dashboard interativo desenvolvido com **Streamlit** para análise de dados de funcionários. Ele permite visualizar informações, aplicar filtros e gerar insights de forma simples e rápida.

---

## ▶️ Como executar a aplicação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar as dependências

Certifique-se de ter o Python 3.8 ou superior instalado.

```bash
pip install streamlit pandas numpy
```

### 3. Executar o projeto

```bash
streamlit run app.py
```

### 4. Acessar no navegador

O app abrirá automaticamente em:

```
http://localhost:8501
```

---

## ⚙️ Funcionalidades

### 🔎 Filtros na Sidebar

* Seleção de **cidade** (multiselect)
* Filtro de **faixa salarial**
* Filtro por **categoria de salário** (Baixo, Médio, Alto ou Todas)

---

### 📊 Indicadores (KPIs)

* 💰 Salário médio
* 👥 Total de funcionários
* 📈 Salário máximo

---

### 📋 Tabela de dados

Visualização dos dados filtrados em tabela interativa.

---

### 📊 Gráficos

* Média salarial por cidade
* Distribuição por categoria salarial

---

### 📌 Tabela dinâmica (Pivot Table)

Resumo dos salários por cidade e categoria.

---

### ⬇️ Download de dados

Permite baixar os dados filtrados em formato CSV.

---

### 📂 Upload de CSV

Permite enviar um arquivo CSV para visualização.

---

## 🧠 Observações

* O sistema realiza tratamento automático dos dados:

  * Preenchimento de valores ausentes
  * Criação de novas colunas (salário anual, categoria, etc.)
* Os dados são atualizados dinamicamente conforme os filtros.

---

## 🚀 Tecnologias utilizadas

* Python
* Streamlit
* Pandas
* NumPy

---

## 📌 Autor

Gustavo Vinicius de Sousa Galvao - 202308423304
