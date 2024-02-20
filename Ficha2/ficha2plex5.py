import re

def soma_string(linha):
    return sum(list(map(int,(re.split(",", linha)))))
    

print(soma_string("4,10,-6,2,3,8,-3,0,2,-5,1"))