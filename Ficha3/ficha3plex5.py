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
    countletras = 0;
    countnumeros = 0;
    if(re.match(r"(\w{2}([-\s])\w{2}\1\w{2}",codigo)): return True
    else: return False


for matricula in matriculas:
    (valida(matricula))