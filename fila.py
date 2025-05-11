class fila():
    def __init__(self):
        self.data = []

    def inserir(self,x):
        self.data.append(x) #concatena um elemento no final da lista

    def remover(self):
        if len(self.data) > 0: #verifica se há elementos na lista
            return self.data.pop(0) #retorna o elemento que está mais há esquerda

    def top(self):
       if len(self.data) > 0:
        return self.data.pop(0)

    def empty(self):
        return not len(self.data) > 0 #retorna verdadeiro em caso de fila vazia


#EXERCÍCIO
# Implementar um programa de gerenciamento de duas filas em um banco: prioritária e normal.
# Seu programa deverá permitir que pessoas sejam inseridas no fim de cada fila, dependendo
# da idade de cada uma (acima de 60 anos entra na fila prioritária). A saída de pessoas da
# fila deve ocorrer da seguinte forma: a cada duas pessoas que saem da fila prioritária, uma
# sai da fila normal.

class gerenciar_filas():
    def __init__(self): #iniciar as filas!!
      self.fila_prioritaria = fila()
      self.normal = fila()
      self.contador_prioritaria = 0 #controlar as saídas

    def adicionar_pessoa(self, idade):
        if idade >= 60:
            self.fila_prioritaria.inserir(idade)

        else:
            self.normal.inserir(idade)

    def saida_fila(self, idade):
        while not self.fila_prioritaria.empty() or not self.normal.empty():
            if self.contador_prioritaria < 2:
                self.contador_prioritaria += 1
                return self.fila_prioritaria.remover()

            else:
                self.contador_prioritaria = 0 #zera a contagem dos prioritarios
                return self.normal.remover()

    def mostrar_listas(self):
        print("Fila prioritária:", self.fila_prioritaria.data)
        print("Fila normal:", self.normal.data)


sistema = gerenciar_filas() #instanciar objeto == tornar ele concreto
sistema.adicionar_pessoa(30)
sistema.adicionar_pessoa(59)
sistema.adicionar_pessoa(70)
sistema.adicionar_pessoa(77)

sistema.saida_fila(30)
sistema.saida_fila(77)

sistema.mostrar_listas()

