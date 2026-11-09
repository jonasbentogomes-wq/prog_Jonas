def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                auxiliar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = auxiliar
                
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_do_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_do_menor]:
                indice_do_menor = j
        auxiliar = lista[i]
        lista[i] = lista[indice_do_menor]
        lista[indice_do_menor] = auxiliar
        
    return lista

def insertion_sort(lista):
    n = len(lista)
    
    for i in range(1, n):
        numero_atual = lista[i]
        posicao_anterior = i - 1
        
        while posicao_anterior >= 0 and lista[posicao_anterior] > numero_atual:
            lista[posicao_anterior + 1] = lista[posicao_anterior]
            posicao_anterior = posicao_anterior - 1
            
        lista[posicao_anterior + 1] = numero_atual
        
    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
        
    indice_do_meio = len(lista) // 2
    pivo = lista[indice_do_meio]
    
    menores = []
    maiores = []
    iguais = []
    
    for numero in lista:
        if numero < pivo:
            menores.append(numero)
        elif numero > pivo:
            maiores.append(numero)
        else:
            iguais.append(numero)
            
    lista_ordenada = quicksort(menores) + iguais + quicksort(maiores)
    return lista_ordenada

