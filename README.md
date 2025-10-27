# 🌳 Sistema de Cidades com Árvores AVL e Grafos

Este projeto implementa uma estrutura de dados combinando **Árvores AVL**, **Árvores Binárias de Busca (BST)** e **Grafos**, permitindo o **cadastro e gerenciamento de cidades e conexões entre seus bairros**.

## ⚙️ Funcionalidades

### 🌆 Gestão de Cidades (usando Árvore AVL)
- Inserção de cidades de forma balanceada.
- Armazenamento de dados com `ID` e `nome`.
- Visualização dos percursos:
  - **Pré-ordem**
  - **Em-ordem**
  - **Pós-ordem**

### 🗺️ Gestão de Bairros e Conexões (usando Grafos)
Cada cidade possui um grafo interno, que permite:
- Adicionar conexões entre bairros com pesos (distâncias);
- Executar os algoritmos:
  - **BFS (Busca em Largura)**  
  - **DFS (Busca em Profundidade)**  
  - **Dijkstra (Caminho mais curto)**  

## 🖥️ Execução

### 🔧 Pré-requisitos
- Python **3.8+**
- Nenhuma biblioteca externa é necessária (somente módulos padrão).

### ▶️ Rodar o programa
No terminal, execute:
python main.py

### 📜 Menu Principal
=== MENU ===
1. Cadastrar Cidade
2. Mostrar Percursos
3. Gerenciar Grafo de Cidade
0. Sair

## 💡 Exemplo de Uso

Cadastrar uma cidade:
ID da cidade: 1
Nome da cidade: Caruaru
Cidade 'Caruaru' cadastrada com sucesso.

Gerenciar grafo da cidade:
1. Adicionar conexão
2. BFS
3. DFS
4. Dijkstra

Adicionar conexão:
Bairro origem: Centro
Bairro destino: Boa Vista
Distância: 5

Executar Dijkstra:
Bairro inicial: Centro
Centro → Centro = 0
Centro → Boa Vista = 5

## 🧠 Estruturas Implementadas

### 🔹 Árvore Binária de Busca (BST)
Arquivo: arvore_binaria.py  
Permite inserir e buscar nós com base em chaves únicas, além de percursos em diferentes ordens.

### 🔹 Árvore AVL
Arquivo: arvore_avl.py  
Extensão da BST com balanceamento automático por rotações (direita/esquerda).

### 🔹 Grafo
Arquivo: grafo.py  
Usa listas de adjacência e implementa:
- **BFS**
- **DFS**
- **Dijkstra (com heap de prioridade)**

## 🧑‍💻 Autor
**Gustavo Vinícius de Sousa Galvão**  
📍 Projeto acadêmico em Python para estudo de **estruturas de dados e algoritmos de grafos**.
