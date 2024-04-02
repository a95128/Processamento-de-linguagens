import ply.lex as lex

tokens = ['NOME', 'NUM', 'PONTOS', 'NUM', 'PONTOVIRGULA']

t_PONTOVIRGULA = r';'
t_PONTOS = r':{1,2}'
t_NUM = r'\d+(.\d+)?'
t_NOME = r'[A-Za-z]\w*'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()