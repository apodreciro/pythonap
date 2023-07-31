listexemplo = [3,3,3,4,5,6,7,3, 10 ]
#função que soma valores em uma lista
def somalist(s):
    soma = 0
    for i in s:
        soma = soma + i 
    return soma

#função que acha o maior valor em uma lista 

def maiorlist(v):
    maior = 0
    for i in v:
        if (i > maior):
            maior = i
    return maior

#função que cria uma lista a partir de uma lista mas que exclui os valores diferentes

def diflist(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b
#função fatorial de um número
def factorial(n):
    fact = 1
    if (n < 0):
        return "aí não dá né irmão"
    for i in range (1, n+1):
        fact = i * fact
    return fact


print(factorial(100))
