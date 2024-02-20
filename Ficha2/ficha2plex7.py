import re

def variavel_valida(id):
  padrao = r'^[a-zA-Z0-9_]*$'
  if(re.match(padrao,id)):
    return True
  else:
    return False

print(variavel_valida("aa11_aa aa"))