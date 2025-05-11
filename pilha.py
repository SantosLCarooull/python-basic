#pilha
class pilha():
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x) #add elemento a pilha

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop() #retira elemento da pilha

    def top(self):
        if len(self.data) > 0:
            return self.data[-1] #retorna o elemento da cima da pilha

    def empty(self):
        return not len(self.data) > 0 #retorna True se a pilha está vazia

p = pilha() #converter para binário
num = 39
while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

while not p.empty():
    print(p.pop(), end='') #imprimir a pilha

