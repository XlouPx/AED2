# Biblioteca: lista de livros como dicionários (titulo, autor, ano)
# A lista está ordenada alfabeticamente pelo título
indice_biblioteca = [
    {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977},
    {"titulo": "Capitães da Areia", "autor": "Jorge Amado", "ano": 1937},
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"titulo": "Grande Sertão: Veredas", "autor": "João Guimarães Rosa", "ano": 1956},
    {"titulo": "Iracema", "autor": "José de Alencar", "ano": 1865},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "ano": 1881},
    {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890},
    {"titulo": "O Guarani", "autor": "José de Alencar", "ano": 1857},
    {"titulo": "Senhora", "autor": "José de Alencar", "ano": 1875},
    {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "ano": 1938}
]

def buscar_livro_indice(indice_livros, titulo_livro):
    baixo = 0
    alto = len(indice_livros) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        titulo_meio = indice_livros[meio]['titulo'].lower()
        titulo_procurado = titulo_livro.lower()
        if titulo_meio == titulo_procurado:
            return indice_livros[meio]
        elif titulo_meio < titulo_procurado:
            baixo = meio + 1
        else:
            alto = meio - 1
    return None

# Entrada do usuário
titulo_busca = input("Digite o título do livro que você procura: ")

# Executa a busca
livro_encontrado = buscar_livro_indice(indice_biblioteca, titulo_busca)

# Resultado
if livro_encontrado:
    print(f"Livro encontrado: {livro_encontrado['titulo']}")
    print(f"Autor: {livro_encontrado['autor']}")
    print(f"Ano de publicação: {livro_encontrado['ano']}")
else:
    print(f"O livro com o título '{titulo_busca}' não foi encontrado na biblioteca.")