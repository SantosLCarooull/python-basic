"""" 
Desenvolver um aplicativo de calculadora que funcione via linha de comando 
(terminal). O usuário deve ser capaz de escolher entre diferentes operações 
matemáticas, inserir números para realizar os cálculos, e navegar no menu do 
aplicativo.
Requisitos Funcionais
Menu Principal
Ao iniciar, o aplicativo deve exibir um menu principal com as seguintes 
opções:
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
s - Sair
O usuário escolhe uma operação digitando o número correspondente.
Se o usuário digitar "s", o aplicativo deve exibir uma mensagem de 
agradecimento e encerrar. 
Execução da Operação
Após escolher uma operação, o usuário deve ser solicitado a inserir dois 
números, um por vez, pressionando "Enter" após cada um. O aplicativo calcula 
e exibe o resultado da operação escolhida com os números fornecidos.
Dica: tome cuidado com divisões por zero!
Após exibir o resultado, o aplicativo retorna automaticamente ao menu 
principal

"""""
def calculadora():
    while True:
        print('Calculadora Simples - Por favor escolha uma opcao abaixo: ')
        print('1. Soma ')
        print('2. Subtração ')
        print('3. Multiplicação ')
        print('4. Divisão ')
        print('s. Finalizar a Calculadora simples ')

        operacao =input('Digite abaixo a opção desejada:  ')

        if operacao == 's' or operacao == 'S':
            print('Obrigado por usar nossa Calculadora Simples. ')
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Opção invalida! Por favor confira o menu e tente novamente.")
            continue

        num_1 = float(input('Digite o primeiro numero da operação: '))
        num_2 = float(input('Digite o segundo numero da operação: '))

        if operacao == '1':
            resultado = num_1 + num_2
            print('O resultado da soma e: ', resultado)

        elif operacao == '2':
            resultado = num_1 - num_2
            print('O resultado da subtração e: ', resultado)

        elif operacao == '3':
            resultado = num_1 * num_2
            print('O resultado da multiplicação e: ', resultado)

        else:
            if num_2 == 0:
                print('Não e possivel dividir por ZERO !!')
            else:
                resultado = num_1 / num_2
                print('O resultado da divisão e: ', resultado)

calculadora()
