# carros = ["gol", "celta", "palio"]

# # for carro in carros:
# #     print(carro)


# for indice, carro in enumerate(carros):
#     print(f"{indice}: {carro}")



#     # Filtrar lista
# numeros = [1, 30, 21, 2, 9, 65, 34]
# pares = [numero for numero in numeros if numero % 2 == 0]
# print(pares)

# # Modificar valores
# numeros = [1, 30, 21, 2, 9, 65, 34]
# quadrado = [numero**2 for numero in numeros]
# print(quadrado)

#set
# numeros = set([1, 2, 3, 1, 3, 4])
# print(numeros)  # {1, 2, 3, 4}

# letras = set("abacaxi")
# print(letras)  # {"b", "a", "c", "x", "i"}

# carros = set(("palio", "gol", "celta", "palio"))
# print(carros)  # {"gol", "celta", "palio"}

# #dict
# pessoa = {"nome": "Caroline", "idade": 31}
# print(pessoa)

# pessoa = dict(nome="Caroline", idade=31)
# print(pessoa)

# pessoa["telefone"] = "3333-1234"  
# print(pessoa)


# dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# print(dados["nome"])  # "Guilherme"
# print(dados["idade"])  # 28
# print(dados["telefone"])  # "3333-1234"

# dados["nome"] = "Maria"
# dados["idade"] = 18
# dados["telefone"] = "9988-1781"

# print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

# contatos = {
#     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
#     "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#     "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
#     "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
# }

# nome = contatos["giovanna@gmail.com"]["nome"]
# telefone = contatos["chappie@gmail.com"]["telefone"]
# print(nome)
# print(telefone)

# contatos = {
#     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
#     "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#     "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
#     "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
# }

# for chave in contatos:
#     print(chave, contatos[chave])

# print("=" * 100)

# for chave, valor in contatos.items():
#     print(chave, valor)

# contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# # contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
# # print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

# contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", }})
# # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
# print(contatos)

# contatos = {
#     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
#     "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
#     "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
#     "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
# }

# resultado = "guilher@gmail.com" in contatos  # True
# print(resultado)

# resultado = "megui@gmail.com" in contatos  # False
# print(resultado)

# resultado = "idade" in contatos["guilherme@gmail.com"]  # False
# print(resultado)

# resultado = "telefoni" in contatos["giovanna@gmail.com"]  # True
# print(resultado)

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)