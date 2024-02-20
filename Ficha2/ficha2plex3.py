import re

def narcissismo(linha):
    return len(re.findall("eu", linha,re.IGNORECASE))

print(narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."))