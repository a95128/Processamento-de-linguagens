import ply.lex as lex

tokens = ['PA', 'PF', 'VIRG', 'NUM', 'ALFANUM']

t_PA = r'\['
t_PF = r'\]'
t_VIRG = r','
t_NUM = r'\d+'
t_ALFANUM = r'[A-Za-z]\w*'

t_ignore = " \t\n"

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()