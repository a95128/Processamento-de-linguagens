import re

def toupper(lista):
  return re.sub(r"\.*",lista.upper(),lista)

def pronomes(frase):
    x = re.compile("eu|tu|ele|ela|nós|vós|eles|elas", re.IGNORECASE)
    return x.findall(frase)

pslist = pronomes("Ola eu vou de certeza. Tu tu e ele, vêm? Eu não espero por vós. Eu estou com pressa, ele tem de vir!")
print(pslist)
