import re

def codigos(listaCPs):
    if isinstance(listaCPs, str):  # Se a entrada for uma string
        return re.findall(r'4\d{3}-\d{3}', listaCPs)
    else:  # Se a entrada for uma lista
        return [codigo for codigo in listaCPs if re.match(r'4\d{3}-\d{3}', codigo)]

# Exemplo de uso com a lista
lista = [
    "4700-000",
    "1234-567",
    "8541-543",
    "4123-974",
    "9481-025"
]
print(codigos(lista))

# Exemplo de uso com a string
lista2 = "1100-3#1234-777#1198-999#4715-012"
print(codigos(re.split(r'#', lista2)))