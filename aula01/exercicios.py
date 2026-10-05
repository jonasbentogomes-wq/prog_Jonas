"""Aula 01 - De C para Python.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.
"""


def soma_lista(lista):
    """Devolve a soma de todos os numeros da lista. Lista vazia devolve 0."""
    soma = 0
    for n in lista:
        soma = soma + n 
    return soma
    return 0


def conta_pares(lista):
    """Devolve quantos numeros da lista sao pares."""
    qtd_pares = 0
    for n in lista:
        if n % 2 == 0:
            qtd_pares += 1
    return qtd_pares


def maior_valor(lista):
    """Devolve o maior numero da lista. A lista nao esta vazia."""
    maior = lista[0]
    for n in lista:
        if n > maior:
            maior = n
    return maior  


def existe(lista, alvo):
    """Devolve True se o alvo esta na lista, False se nao esta."""
    for n in lista:
        if n == alvo:
            return True
    return False

def busca_linear(lista, alvo):
    """Devolve a posicao do alvo na lista, ou -1 se ele nao estiver."""
    for indice, elemento in enumerate(lista):
        if elemento == alvo:
            return indice  
    return -1
   
    


def segundo_maior(lista):
    maior, segundo = float('-inf'), float('-inf')
    for n in lista:
        if n > maior:
            maior, segundo = n, maior
        elif n > segundo and n != maior:
            segundo = n
    return segundo
    
