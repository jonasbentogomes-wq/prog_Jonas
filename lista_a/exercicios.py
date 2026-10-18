"""Lista A - Python, listas, busca e custo.

NAO mude o nome deste arquivo nem a assinatura das funcoes.
Escreva sua solucao no lugar do 'pass'.

Os exercicios do Bloco 3 devolvem DOIS valores: o resultado e a contagem.
"""

# ---------- Bloco 1: listas e percurso ----------

def conta_negativos(lista):
    """Quantos numeros da lista sao menores que zero."""
    MZ = 0
    for n in lista:
        if n < 0:
         MZ = MZ + 1

    return MZ 
        
def media(lista):
    """Media dos numeros. Lista vazia devolve 0."""
    soma = 0
    media = 0
    for n in lista:
        if n == 0:
           return 0
        soma = n + 1
        media = soma / len(lista)
        
    return media

def sem_o_maior(lista):
    """Lista NOVA sem o maior valor. Se o maior repete, tira so o primeiro."""
    Pmaior = lista[0]
    novalista = []
    for n in lista:
        if n > Pmaior:  
         novalista.append(n)

    return novalista

def acumulada(lista):
    """Lista NOVA onde cada posicao e a soma de tudo ate ali.
    acumulada([1, 2, 3]) -> [1, 3, 6]"""
    soma = 0
    listanova = []  
    for n in lista:
        soma += n
        listanova.append(soma)
        
    return listanova

def achata(lista_de_listas):
    """(Desafio) Junta as sublistas numa lista so.
    achata([[1, 2], [3]]) -> [1, 2, 3]"""
    sublistas = []
    LC = 0
    for n in lista_de_listas:
        len(lista_de_listas)
        len(sublistas)
        LC = len(lista_de_listas) + len(sublistas)
    
# ---------- Bloco 2: busca ----------

"""len = elementos, append adiciona um elemento na ultima posição eventualmente adicionando uma posição"""


def busca_ultima(lista, alvo):
    """ULTIMA posicao do alvo, ou -1."""
    posição = -1
    for i in range(len(lista)):
        if lista[i] == alvo:
            posição = i

    return posição

        

def conta_ocorrencias(lista, alvo):
    """Quantas vezes o alvo aparece."""
    pass


def primeiro_maior_que(lista, limite):
    """Posicao do primeiro elemento maior que limite, ou -1."""
    pass


def busca_binaria_primeira(lista, alvo):
    """(Desafio) Lista JA ORDENADA, o alvo pode repetir.
    Devolve a PRIMEIRA posicao do alvo, ou -1. Sem percorrer tudo."""
    pass


# ---------- Bloco 3: custo ----------

def soma_pares_contando(lista):
    """(soma_dos_pares, operacoes). Conte 1 por elemento examinado."""
    soma = 0
    operacoes = 0

    for elemento in lista:
        operacoes += 1
        if elemento % 2 == 0:
            soma += elemento

    return soma, operacoes


def maior_contando(lista):
    """(maior, comparacoes). Lista nao vazia.
    Conte 1 comparacao por elemento a partir do segundo."""
    maior = lista[0]
    comparacoes = 0

    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] > maior:
            maior = lista[i]

    return maior, comparacoes


def tem_soma_contando(lista, alvo):
    """(True/False, comparacoes). Existem dois elementos que somam alvo?
    Conte 1 por par comparado. Pare assim que achar."""
    comparacoes = 0
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[i] + lista[j] == alvo:
                return True, comparacoes

    return False, comparacoes


def ordenada_contando(lista):
    """(Desafio) (True/False, comparacoes). A lista esta em ordem crescente?
    Conte 1 por par de vizinhos comparado. Pare no primeiro fora de ordem."""
    comparacoes = 0

    for i in range(len(lista) - 1):
        comparacoes += 1
        if lista[i] > lista[i + 1]:
            return False, comparacoes

    return True, comparacoes

# ---------- Bloco 4: padroes ----------

def inverte_no_lugar(lista):
    """Inverte a PROPRIA lista recebida. NAO cria lista nova e NAO devolve nada."""
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        lista[esquerda], lista[direita] = lista[direita], lista[esquerda]
        esquerda += 1
        direita -= 1


def eh_palindromo(lista):
    """True se a lista e igual lida de tras para frente."""
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        if lista[esquerda] != lista[direita]:
            return False
        esquerda += 1
        direita -= 1

    return True


def par_que_soma(lista, alvo):
    """Lista JA ORDENADA. Devolve (i, j) das posicoes cujos valores somam alvo,
    ou (-1, -1). Sem laco dentro de laco."""
    esquerda = 0
    direita = len(lista) - 1

    while esquerda < direita:
        soma_atual = lista[esquerda] + lista[direita]

        if soma_atual == alvo:
            return (esquerda, direita)
        elif soma_atual < alvo:
            esquerda += 1
        else:
            direita -= 1

    return (-1, -1)


def soma_maxima_janela(lista, k):
    """Maior soma de k elementos seguidos.
    soma_maxima_janela([1, 2, 3, 4], 2) -> 7"""
    if len(lista) < k or k <= 0:
        return 0

    soma_atual = sum(lista[:k])
    maior_soma = soma_atual

    for i in range(k, len(lista)):
        soma_atual += lista[i] - lista[i - k]
        if soma_atual > maior_soma:
            maior_soma = soma_atual

    return maior_soma


def parenteses_balanceados(texto):
    """(Desafio) True se os ( ) e [ ] do texto abrem e fecham na ordem certa."""
    pilha = []
    mapeamento = {')': '(', ']': '['}

    for caractere in texto:
        if caractere in "([":
            pilha.append(caractere)
        elif caractere in ")]":
            if not pilha or pilha[-1] != mapeamento[caractere]:
                return False
            pilha.pop()

    return len(pilha) == 0