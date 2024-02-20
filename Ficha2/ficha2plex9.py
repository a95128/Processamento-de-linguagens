import re

def underscores( frase ):
  return re.sub(r'\s',r'_', frase)

print(underscores("Aqui temos   um belo  exemplo   de frase!"))