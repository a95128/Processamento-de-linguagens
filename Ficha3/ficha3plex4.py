import re

import re
abreviaturas = {
    "UM": "Universidade do Minho",
    "LEI": "Licenciatura em Engenharia Informática",
    "UC": "Unidade Curricular",
    "PL": "Processamento de Linguagens"
}

texto = "A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."

def subabrev(match):
    abreviatura = match.group(1)
    if abreviatura in abreviaturas:
        return abreviaturas[abreviatura]

padrao = re.compile(r"/abrev{(\w+)}")
texto_final = re.sub(padrao, subabrev, texto)

print(texto_final)
