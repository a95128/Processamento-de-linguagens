import re

def palavra_magica(frase):
    padrao = r'por favor[.?!]$'
    return re.search(padrao, frase, re.IGNORECASE | re.UNICODE) is not None

print(palavra_magica("Posso ir à casa de banho, por favor?"))
print(palavra_magica("Preciso de um favor."))

