class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)
    
    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = Node(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = Node(valor)
            else: 
                self._inserir_recursivo(no.direita, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, no, valor):
        if no is None or no.valor == valor:
            return no is not None
        if valor < no.valor:
            return self._buscar_recursivo(no.esquerda, valor)
        return self._buscar_recursivo(no.direita, valor)
    
    def em_ordem(self):
        return self._em_ordem_recursivo(self.raiz)
    
    def _em_ordem_recursivo(self, no):
        if no is None:
            return []
        return self._em_ordem_recursivo(no.esquerda) + [no.valor] + self._em_ordem_recursivo(no.direita)
    
    def pre_ordem(self):
        return self._pre_ordem_recursivo(self.raiz)
    
    def _pre_ordem_recursivo(self, no):
        if no is None:
            return []
        return [no.valor] + self._pre_ordem_recursivo(no.esquerda) + self._pre_ordem_recursivo(no.direita)
    

    def pos_ordem(self):
        return self._pos_ordem_recursivo(self.raiz)
    
    def _pos_ordem_recursivo(self, no):
        if no is None:
            return []
        return self._pos_ordem_recursivo(no.esquerda) + self._pos_ordem_recursivo(no.direita) + [no.valor]
    


arvore = Arvore() 
arvore.inserir(7)       
arvore.inserir(6)
arvore.inserir(5)
arvore.inserir(2)
arvore.inserir(1)
arvore.inserir(4)
arvore.inserir(4)
arvore.inserir(3)

print('Arvore em Ordem')
print(arvore.em_ordem()) # 
print('----------------')
print('Arvore pre Ordem')
print(arvore.pre_ordem()) #
print('----------------')
print('Arvore Pós Ordem')
print(arvore.pos_ordem())
print('----------------')

print(arvore.buscar(7))
print(arvore.buscar(22))





    


