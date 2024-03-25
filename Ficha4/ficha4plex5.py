import ply.lex as lex
import sys

states = (
    ('multiativo', 'exclusive'),
    ('inlativo', 'exclusive'),
)


tokens = (
    'CONTEUDO',
    'ABRIR_COMMENT',
    'ABRIR_COMMENT_I',
    'FECHAR_COMMENT',
    'NEWLINE'
)

t_ANY_ignore = r' '

def t_NEWLINE(t):
    r'\n'
    return t

def t_multiativo_NEWLINE(t):
    r'\n'
    return t

def t_CONTEUDO(t):
    r'\w+'
    print(t.value)
    return t

def t_inlativo_multiativo_CONTEUDO(t):
    r'\w+\**'
    return t

def t_ABRIR_COMMENT(t):
    r'/\*{1,4}'
    t.lexer.begin('multiativo')
    return t

def t_ABRIR_COMMENT_I(t):
    r'//\s*'
    t.lexer.begin('inlativo')
    return t

def FECHAR_COMMENT(t):
    r'\*+/'
    return t

def t_multiativo_FECHAR_COMMENT(t):
    r'\*+/'
    t.lexer.begin('INITIAL')
    return t

def  t_inlativo_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t

def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

data = '''
/* comment */ ola1

/* comment****comment */ ola2 /*
comment
comment
****/ ola3

/*********/

ola4
 mais um pouco // remover comentário inline
FIM
'''

lexer = lex.lex()

lexer.input(data)

for token in lexer:
    print(token)
