import re

lista = [
    "4700-000", # válido
    "9876543", # inválido
    "1234-567", # válido
    "8x41-5a3", # inválido
    "84234-12", # inválido
    "4583--321", # inválido
    "9481-025" # válido
]

def valida(codigo):
    if(re.match(r"\d{4}-\d{3}",codigo)): return True
    else: return False

def separa(codigo):
    if(valida(codigo)==True):
        print(codigo.split("-"))


for codigo in lista:
    (separa(codigo))