# Exercício
#  Implementar uma função recursiva para calcular o n-ésimo termo da sequência de Fibonacci.
#  Considere os três pontos definidos para o problema:
#  1) f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2) p/ n>=2
#  2) n=0 ou n=1
#  3) n deve ser decrementado a cada chamada

def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        seq = fibonacci(n - 1) + fibonacci(n - 2)
        return seq


print(fibonacci(16))


#prof
#def	fib_rec(n):
#if	n	<	2:
# return	n
#else:
#return	fib_rec(n-1)	+	fib_rec(n-2)


m =	dict()
def	fib_mem(n):
 if	n	<	2:
    return	n
 elif m.get(n)	!=	None:
    return	m[n]
 else:
    m[n]	=	fib_mem(n-1)	+	fib_mem(n-2)
    return	m[n]

fib_mem(10)