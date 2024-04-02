from ficha5plex1_analex import tokens
import ply.yacc as yacc

def p_expression_PA_PF(p):
   'expression : PA conteudo PF'
   p[0] = p[2]

def p_conteudo(p):
   '''conteudo :  
            | variavel
            | variavel VIRG conteudo'''

def p_variavel(p):
    ''' variavel : NUM
              | ALFANUM'''
    p[0] = p[1]

def p_error(p):
    print("Erro sintático no input!")

parser = yacc.yacc()

while s := input():
   result = parser.parse(s)

# expression : [conteudo]
# conteudo : 
#          | variavel
#          | variavel , conteudo
# variavel : NUM
#          | STRING