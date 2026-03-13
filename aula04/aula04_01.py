# Lista ordenada onde será feita a busca
lista_ord = [1,2,3,4,5,6,7,8,9,10,11,12]

# Valor que queremos encontrar
v = 7

# Função de busca binária
def busca_binaria(v, lista_ord):

    # Define os limites da busca na lista
    esquerda = 0
    direita = len(lista_ord) - 1

    # Continua buscando enquanto houver elementos no intervalo
    while esquerda <= direita:

        # Calcula a posição do meio da lista
        meio = (esquerda + direita) // 2

        # Caso 1: encontrou o valor
        if v == lista_ord[meio]:
            return meio

        # Caso 2: valor está na metade esquerda
        elif v < lista_ord[meio]:
            direita = meio - 1

        # Caso 3: valor está na metade direita
        else:
            esquerda = meio + 1

    # Se não encontrar o valor na lista
    return -1