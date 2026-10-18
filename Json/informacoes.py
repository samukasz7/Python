import json


json_string = """{
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo",
    "profissao": "Engenheiro"
}"""

dados = json.loads(json_string)
print(dados)