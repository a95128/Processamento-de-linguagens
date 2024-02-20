line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

import re


print("Linhas que contêm a palavra: hello no início (à esquerda)")
inputFromUser = input(">> ")
while inputFromUser != "":
 #EXERCICIO 1.1
 #x=re.compile("hello")
 #print(x.match(inputFromUser)) #verifica o inicio do input
 #EXERCICIO 1.2
 #print(re.search("hello",inputFromUser)) #verifica o input todo
 #EXERCICIO 1.3
 #print(re.findall("hello", inputFromUser, re.IGNORECASE))
 #EXERCICIO 1.4
 #resultado = re.sub("hello", "*YEP*", inputFromUser)
 #print(resultado)
 #EXERCICIO 1.5
 #print(re.split(",", inputFromUser))
 inputFromUser = input(">>")
