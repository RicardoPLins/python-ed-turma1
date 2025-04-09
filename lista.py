class Item:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaSimplesmenteEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor):
        novo_item = Item(valor)
        if not self.cabeca:
            self.cabeca = novo_item
        else:
            item_atual = self.cabeca
            while item_atual.proximo:
                item_atual = item_atual.proximo
            item_atual.proximo = novo_item

    def percorrer(self):
        valores = []
        item_atual = self.cabeca
        while item_atual:
            valores.append(item_atual.valor)
            item_atual = item_atual.proximo
        return valores
    
    def remover(self, valor):
        if not self.cabeca:
            return
        if self.cabeca.valor == valor:
            self.cabeca = self.cabeca.proximo
            return
        
        anterior = self.cabeca
        atual = self.cabeca.proximo

        while atual:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

        
    
    

lista = ListaSimplesmenteEncadeada()
lista.inserir(1)
lista.inserir("Iago")
lista.inserir(True)
lista.inserir('Aula ED - Turma 1')
print("A lista é: ", lista.percorrer())
lista.remover(1)
print("A lista é: ", lista.percorrer())
lista.remover(True)
print("A lista é: ", lista.percorrer())


