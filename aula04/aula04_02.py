# Biblioteca: lista de livros (titulo, autor, ano)
# A lista está ordenada alfabeticamente pelo título
BIBLIOTECA = [
    ("A Hora da Estrela", "Clarice Lispector", 1977),
    ("Capitães da Areia", "Jorge Amado", 1937),
    ("Dom Casmurro", "Machado de Assis", 1899),
    ("Grande Sertão: Veredas", "João Guimarães Rosa", 1956),
    ("Iracema", "José de Alencar", 1865),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881),
    ("O Cortiço", "Aluísio Azevedo", 1890),
    ("O Guarani", "José de Alencar", 1857),
    ("Senhora", "José de Alencar", 1875),
    ("Vidas Secas", "Graciliano Ramos", 1938)
]

# Função de busca binária para encontrar um livro pelo título
def busca_binaria(titulo_procurado, biblioteca):
    esquerda = 0
    direita = len(biblioteca) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        titulo_meio = biblioteca[meio][0]

        # Compara ignorando maiúsculas/minúsculas para evitar erros
        if titulo_procurado.lower() == titulo_meio.lower():
            return meio  # livro encontrado
        elif titulo_procurado.lower() < titulo_meio.lower():
            direita = meio - 1
        else:
            esquerda = meio + 1

    return -1  # livro não encontrado

# Pergunta para o usuário qual título deseja buscar
v = input("Digite o título do livro que você procura: ")

# Executa a busca
resultado = busca_binaria(v, BIBLIOTECA)

# Verifica o resultado e imprime
if resultado != -1:
    livro = BIBLIOTECA[resultado]
    print(f"Livro encontrado: {livro[0]} - Autor: {livro[1]} - Ano: {livro[2]}")
else:
    print("Livro não encontrado")