import json

json_string = """{
    "livros": [
        {
            "titulo": "A Revolução dos Bichos",
            "autor": "George Orwell",
            "ano_publicacao": 1945,
            "genero": "Ficção política",
            "editora": "Companhia das Letras"
        },
        {
            "titulo": "1984",
            "autor": "George Orwell",
            "ano_publicacao": 1949,
            "genero": "Ficção distópica",
            "editora": "Companhia das Letras"
        },
        {
            "titulo": "Dom Quixote",
            "autor": "Miguel de Cervantes",
            "ano_publicacao": 1605,
            "genero": "Romance",
            "editora": "Editora Nova Fronteira"
        }
    ]
}
"""

dados = json.loads(json_string)
for livros in dados['livros']:
    nome = livros['titulo']
    autor = livros['autor']
    print(f'Nome: {nome} \nAutor: {autor}  ')