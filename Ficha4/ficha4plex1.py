import re
import ply.lex as lex

tokens = (
   'LETTER',
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'EQUAL',
   'NEWLINE'

)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_EQUAL = r'='


# A regular expression rule with some action code
def t_LETTER(t):
    r'[a-z]'
    t.value = (t.value)    
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
while True:
    data = input("Enter data: ")
    if data == "STOP":
        break
    lexer.input(data)
    for tok in lexer:
        if tok.type == "LETTER" or tok.type == "NUMBER":
            print("variavel", tok.value)
        if tok.type == "PLUS" or tok.type == "MINUS" or tok.type == "EQUAL" or tok.type == "TIMES":
            print("operador encontrado")
        elif tok.type == "NEWLINE":
            print("\n")
        #print(tok.type, tok.value, tok.lineno, tok.lexpos)