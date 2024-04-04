from ficha5plex2_analex import tokens
import ply.yacc as yacc

def p_lista_compras(p):
   ''' lista_compras : CATEGORIA
                     | lista_compras CATEGORIA'''
  
def p_conteudo(p):
   '''conteudo :  
            | item
            | item PONTOVIRGULA conteudo'''

def p_itens(p):
   ''' itens : item 
             | item PONTOVIRGULA itens '''

def p_item(p):
    ''' item : PONTOS NUM PONTOS STRING PONTOS NUM PONTOS NUM '''
    p[0] = {'id': p[2], 'nome': p[4], 'preco': float(p[6]), 'quantidade': int(p[8])}

def p_error(p):
    print("Erro sintático no input!")

parser = yacc.yacc()

while s := input():
   result = parser.parse(s)

