import re

texto = "Ola bom dia  ola dia ola bom"

palavras = re.findall("(\w+)", texto)

lista_minuscula = [palavra.lower() for palavra in palavras]

palavrassemrep = []

for palavra in lista_minuscula:
    if not (palavra in palavrassemrep):
        palavrassemrep.append(palavra)

palavrassemrep = ' '.join(palavrassemrep)
print(palavrassemrep)