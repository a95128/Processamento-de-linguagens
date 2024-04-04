import ply.lex as lex

tokens = ['CATEGORIA','STRING', 'PONTOS', 'NUM', 'PONTOVIRGULA']

t_CATEGORIA = r'(CARNE|BEBIDA|FRUTA|LEGUMES|PASTELARIA)'
t_PONTOVIRGULA = r';'
t_PONTOS = r'(:{1,2}|-)'
t_NUM = r'\d+(.\d+)?'
t_STRING = r'[A-Za-z]+'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()