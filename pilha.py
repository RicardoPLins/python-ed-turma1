class Pilha:
    def __init__(self):
        self.itens = []
    
    def empilhar(self, item):
        self.itens.insert(0, item)

    def desempilhar(self):
        if not self.esta_vazia():
            return f"O item {self.itens.pop(0)} foi desempilhado"
        return None
    
    def esta_vazia(self):
        return len(self.itens) == 0
    
    def topo(self):
        if not self.esta_vazia():
            return self.itens[0]
        return None
    
    def tamanho(self):
        return len(self.itens)
    
    def __str__(self):
        return str(self.itens)
    


pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
print(pilha.topo()) # 3
pilha.empilhar(4) 
pilha.desempilhar()
print(pilha.topo()) # 3
pilha.empilhar(5)
pilha.empilhar(6)
pilha.empilhar(7)
print(pilha) # 
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
print(pilha.topo()) #2
print(pilha) # 1 2