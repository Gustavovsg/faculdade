from arvore_binaria import ArvoreBinariaBusca, NodoBST

class NodoAVL(NodoBST):
    def __init__(self, chave, valor):
        super().__init__(chave, valor)
        self.altura = 1

class ArvoreAVL(ArvoreBinariaBusca):
    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _fator_balanceamento(self, nodo):
        return self._altura(nodo.esquerda) - self._altura(nodo.direita)

    def _atualiza_altura(self, nodo):
        nodo.altura = 1 + max(self._altura(nodo.esquerda), self._altura(nodo.direita))

    def insert(self, chave, valor):
        self.raiz = self._insert(self.raiz, chave, valor)

    def _insert(self, nodo, chave, valor):
        if not nodo:
            return NodoAVL(chave, valor)

        if chave < nodo.chave:
            nodo.esquerda = self._insert(nodo.esquerda, chave, valor)
        elif chave > nodo.chave:
            nodo.direita = self._insert(nodo.direita, chave, valor)
        else:
            return nodo  # Ignora duplicatas

        self._atualiza_altura(nodo)
        return self._rebalancear(nodo)

    def _rebalancear(self, nodo):
        balance = self._fator_balanceamento(nodo)

        if balance > 1:
            if self._fator_balanceamento(nodo.esquerda) < 0:
                nodo.esquerda = self._rotacao_esquerda(nodo.esquerda)
            return self._rotacao_direita(nodo)

        if balance < -1:
            if self._fator_balanceamento(nodo.direita) > 0:
                nodo.direita = self._rotacao_direita(nodo.direita)
            return self._rotacao_esquerda(nodo)

        return nodo

    def _rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        self._atualiza_altura(y)
        self._atualiza_altura(x)
        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        self._atualiza_altura(x)
        self._atualiza_altura(y)
        return y
