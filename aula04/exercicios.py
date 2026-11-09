"""Aula 04 - Por que ordenar?

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Hoje voce NAO escreve algoritmo de ordenacao. Use sorted(lista), que
devolve uma lista nova e ordenada sem mexer na original. Evite lista.sort(),
que altera a lista de quem chamou a funcao.
"""


def custo_binaria(n):
    """PRONTA. Nao mexa.
    Pior caso da busca binaria numa lista de n elementos.
    E a quantas_divisoes da aula passada mais 1."""
    divisoes = 0
    while n > 1:
        n = n // 2
        divisoes = divisoes + 1
    return divisoes + 1


def tem_repetido_ordenando(lista):
    """Devolve (True, comparacoes) ou (False, comparacoes). Ordene uma copia e compare so os vizinhos. Conte 1 comparacao por par de vizinhos comparado. Pare no primeiro repetido. A ordenacao em si nao entra na contagem. tem_repetido_ordenando([1, 2, 1, 3]) -> (True, 1)"""
    lista_ordenada = sorted(lista)
    comparacoes = 0
    
    for i in range(len(lista_ordenada) - 1):
        comparacoes += 1
        if lista_ordenada[i] == lista_ordenada[i+1]:
            return (True, comparacoes)
            
    return (False, comparacoes)

def mediana(lista):
    """Valor do meio da lista ordenada. Tamanho par: media dos dois do meio. Lista vazia: None. Nao altere a lista recebida. mediana([4, 1, 3, 2]) -> 2.5"""
    if not lista:
        return None
        
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2
    
    if n % 2 != 0:
        return lista_ordenada[meio]
    else:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2.0

def buscas_para_compensar(n, custo_ordenar):
    """Menor numero de buscas k tal que ordenar sai estritamente mais barato: custo_ordenar + k * custo_binaria(n) < k * n Devolve -1 se nunca compensa. buscas_para_compensar(100, 10000) -> 108"""
    c_binaria = custo_binaria(n)
    
    # Se a busca sequencial (n) for menor ou igual à busca binária, 
    # ordenar nunca vai compensar independentemente do número de buscas.
    if n <= c_binaria:
        return -1
        
    # Isolando k na inequação: k * (n - custo_binaria) > custo_ordenar
    # k > custo_ordenar / (n - custo_binaria)
    # Como queremos o menor inteiro k estritamente maior, fazemos a divisão inteira + 1
    ganho_por_busca = n - c_binaria
    k = (custo_ordenar // ganho_por_busca) + 1
    
    return k

def menor_diferenca(lista):
    """(Desafio) Menor diferenca, em valor absoluto, entre quaisquer dois elementos. Menos de 2 elementos: None. Existe um teste com 20 mil elementos que da tempo limite se voce olhar todos os pares. menor_diferenca([10, 3, 8, 14]) -> 2"""
    if len(lista) < 2:
        return None
        
    # Ordenando a lista primeiro, os elementos mais próximos obrigatoriamente 
    # ficarão vizinhos. Isso reduz a complexidade de O(N²) para O(N log N).
    lista_ordenada = sorted(lista)
    min_dif = abs(lista_ordenada[1] - lista_ordenada[0])
    
    for i in range(1, len(lista_ordenada) - 1):
        dif = abs(lista_ordenada[i+1] - lista_ordenada[i])
        if dif < min_dif:
            min_dif = dif
            
    return min_dif