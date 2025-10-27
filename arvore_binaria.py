class NodoBST:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def insert(self, chave, valor):
        self.raiz = self._insert(self.raiz, chave, valor)

    def _insert(self, nodo, chave, valor):
        if nodo is None:
            return NodoBST(chave, valor)
        if chave < nodo.chave:
            nodo.esquerda = self._insert(nodo.esquerda, chave, valor)
        elif chave > nodo.chave:
            nodo.direita = self._insert(nodo.direita, chave, valor)
        return nodo

    def search(self, chave):
        return self._search(self.raiz, chave)

    def _search(self, nodo, chave):
        if nodo is None or nodo.chave == chave:
            return nodo
        if chave < nodo.chave:
            return self._search(nodo.esquerda, chave)
        return self._search(nodo.direita, chave)

    def inorder(self):
        resultado = []
        self._inorder(self.raiz, resultado)
        return resultado

    def _inorder(self, nodo, resultado):
        if nodo:
            self._inorder(nodo.esquerda, resultado)
            resultado.append((nodo.chave, nodo.valor))
            self._inorder(nodo.direita, resultado)

    def preorder(self):
        resultado = []
        self._preorder(self.raiz, resultado)
        return resultado

    def _preorder(self, nodo, resultado):
        if nodo:
            resultado.append((nodo.chave, nodo.valor))
            self._preorder(nodo.esquerda, resultado)
            self._preorder(nodo.direita, resultado)

    def postorder(self):
        resultado = []
        self._postorder(self.raiz, resultado)
        return resultado

    def _postorder(self, nodo, resultado):
        if nodo:
            self._postorder(nodo.esquerda, resultado)
            self._postorder(nodo.direita, resultado)
            resultado.append((nodo.chave, nodo.valor))
