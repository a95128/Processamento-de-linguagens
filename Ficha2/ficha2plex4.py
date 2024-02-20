import re

def troca_de_curso(linha, novo_curso):
  return re.sub("LEI",novo_curso, linha)

fonte = "LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei."
curso = input("Novo curso? ")
print(troca_de_curso(fonte, curso))
