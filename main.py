from arvore_avl import ArvoreAVL
from grafo import Grafo

avl = ArvoreAVL()

def formatar_percurso(percurso):
    return [(chave, valor["nome"]) for chave, valor in percurso]

def cadastrar_cidade():
    id_cidade = int(input("ID da cidade: "))
    nome = input("Nome da cidade: ")
    grafo = Grafo()
    avl.insert(id_cidade, {"nome": nome, "grafo": grafo})
    print(f"Cidade '{nome}' cadastrada com sucesso.")

def mostrar_percursos():
    print("Pré-Ordem:", formatar_percurso(avl.preorder()))
    print("In-Ordem:", formatar_percurso(avl.inorder()))
    print("Pós-Ordem:", formatar_percurso(avl.postorder()))

def gerenciar_grafo():
    id_cidade = int(input("ID da cidade: "))
    nodo = avl.search(id_cidade)
    if nodo is None:
        print("Cidade não encontrada.")
        return

    grafo = nodo.valor["grafo"]
    while True:
        print("\n--- Gerenciar Grafo ---")
        print("1. Adicionar conexão")
        print("2. BFS")
        print("3. DFS")
        print("4. Dijkstra")
        print("0. Voltar")
        op = input("Opção: ")

        if op == "1":
            origem = input("Bairro origem: ")
            destino = input("Bairro destino: ")
            peso = int(input("Distância: "))
            grafo.adicionar_aresta(origem, destino, peso)
        elif op == "2":
            inicio = input("Bairro inicial: ")
            print("BFS:", grafo.bfs(inicio))
        elif op == "3":
            inicio = input("Bairro inicial: ")
            print("DFS:", grafo.dfs(inicio))
        elif op == "4":
            inicio = input("Bairro inicial: ")
            resultado = grafo.dijkstra(inicio)
            for destino, custo in resultado.items():
                print(f"{inicio} → {destino} = {custo}")
        elif op == "0":
            break
        else:
            print("Opção inválida.")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar Cidade")
        print("2. Mostrar Percursos")
        print("3. Gerenciar Grafo de Cidade")
        print("0. Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            cadastrar_cidade()
        elif escolha == "2":
            mostrar_percursos()
        elif escolha == "3":
            gerenciar_grafo()
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
