import re

matriculas = [
    "AA-AA-AA", # inválida
    "LR-RB-32", # válida
    "1234LX", # inválida
    "PL 22 23", # válida
    "ZZ-99-ZZ", # válida
    "54-tb-34", # inválida
    "12 34 56", # inválida
    "42-HA BQ" # válida, mas inválida com o requisito extra
]

def valida(codigo):
    countletras = 0
    countnumeros = 0
    padrao = re.compile(r"(\w{2})([-\s])(\w{2})\2(\w{2})")
    m = re.match(padrao, codigo)

    if m: 
        for i in range(1, 5):
            if re.match(r"\d{2}", m.group(i)):
                countnumeros += 1
            elif re.match(r"[A-Z]{2}", m.group(i)):
                countletras +=1

    #print(countletras)
    #print(countnumeros)
    if abs(countletras - countnumeros) == 1:
        return "Válido"
    else:
        return "Inválido"
    
for matricula in matriculas:
    print(valida(matricula))
