import re
file_names = [
  "document.txt", # válido
  "file name.docx", # inválido
  "image_001.jpg", # válido
  "script.sh.txt", # válido
  "test_file.txt", # válido
  "file_name.", # inválido
  "my_resume.docx", # válido
  ".hidden-file.txt", # válido
  "important-file.text file", # inválido
  "file%name.jpg" # inválido
]

#EXERCICIO 2

def valida(file) :
    if(re.match(r"([\w\.\-_]+)(\.)(txt|docx|png|jpg$)", file)): return True
    else: return False

for file in file_names: 
    print(valida(file))

#EXERCICIO 2.1
    
def validados(files):
    validados=[]
    for file in files:
        if(valida(file)==True): validados.append(file)
    return validados
    
def agrupa(files): 
    agrupotxt = []
    agrupodocx = []
    agrupojpg = []
    
    for file in files:
        if re.match(r"([\w\.\-_]+)\.txt$", file):
            agrupotxt.append(file)
        elif re.match(r"([\w\.\-_]+)\.docx$", file):
            agrupodocx.append(file)
        elif re.match(r"([\w\.\-_]+)\.jpg$", file):
            agrupojpg.append(file)

    print("Arquivos .txt: = {" + ", ".join(agrupotxt) + "}")
    print("Arquivos .docx = {" + ", ".join(agrupodocx) + "}")
    print("Arquivos .jpg = {" + ", ".join(agrupojpg) + "}")


arquivos_validos = validados(file_names)
agrupa(arquivos_validos)