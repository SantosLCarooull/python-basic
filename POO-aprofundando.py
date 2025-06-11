# class Estudante:
#     escola = "DIO"

#     def __init__(self, nome, matricula):
#         self.nome = nome
#         self.matricula = matricula

#     def __str__(self) -> str:
#         return f"{self.nome} - {self.matricula} - {self.escola}"


# def mostrar_valores(*objs): #método generico pra mostrar valores: 
#     for obj in objs:
#         print(obj)


# aluno_1 = Estudante("Caroline", 1)
# aluno_2 = Estudante("Santos", 2)
# mostrar_valores(aluno_1, aluno_2)

# aluno_2.escola = "Acordado"
# aluno_3 = Estudante("Lopes", 3)
# mostrar_valores(aluno_1, aluno_2, aluno_3)


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     @classmethod #transf. em metodo de classe
    
#     def criar_de_data_nascimento(cls, ano, mes, dia, nome):# usa cls ao inves de self por convenção
#         idade = 2022 - ano
#         return cls(nome, idade)

#     @staticmethod #transf. em metodo estático
#     def e_maior_idade(idade):
#         return idade >= 18


# p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme") #primeiro cria o obj pessoa depois faz o metodo 'criar_de_data_nascimento'
# print(p.nome, p.idade)

# print(Pessoa.e_maior_idade(18))
# print(Pessoa.e_maior_idade(8))


# from abc import ABC, abstractmethod, abstractproperty


# class ControleRemoto(ABC):
#     @abstractmethod
#     def ligar(self):
#         pass

#     @abstractmethod
#     def desligar(self):
#         pass

#     @property
#     @abstractproperty
#     def marca(self):
#         pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self): #contrato
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self): #contrato
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property #todas as classes filhas de controleremoto tem que implementar marca - por conta do @property 
    def marca(self):
        return "LG"


controle = ControleTV() #instanciando o metodo
controle.ligar() #chamar o metodo
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

