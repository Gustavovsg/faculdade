from collections import defaultdict, deque
import heapq

class Grafo:
    def __init__(self):
        self.adj = defaultdict(list)

    def adicionar_aresta(self, origem, destino, peso=1):
        self.adj[origem].append((destino, peso))
        self.adj[destino].append((origem, peso))

    def bfs(self, inicio):
        visitados = set()
        fila = deque([inicio])
        resultado = []

        while fila:
            atual = fila.popleft()
            if atual not in visitados:
                visitados.add(atual)
                resultado.append(atual)
                for vizinho, _ in self.adj[atual]:
                    fila.append(vizinho)
        return resultado

    def dfs(self, inicio):
        visitados = set()
        resultado = []

        def _dfs(v):
            visitados.add(v)
            resultado.append(v)
            for vizinho, _ in self.adj[v]:
                if vizinho not in visitados:
                    _dfs(vizinho)

        _dfs(inicio)
        return resultado

    def dijkstra(self, inicio):
        dist = {v: float('inf') for v in self.adj}
        dist[inicio] = 0
        heap = [(0, inicio)]

        while heap:
            atual_dist, atual = heapq.heappop(heap)
            if atual_dist > dist[atual]:
                continue
            for vizinho, peso in self.adj[atual]:
                nova_dist = atual_dist + peso
                if nova_dist < dist[vizinho]:
                    dist[vizinho] = nova_dist
                    heapq.heappush(heap, (nova_dist, vizinho))
        return dist
