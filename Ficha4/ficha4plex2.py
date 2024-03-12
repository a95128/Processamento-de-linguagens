import ply.lex as lex

data = '''

@techreport{Camila,
  author ={{projecto Camila}},
  editor ={L.S. Barbosa and J.J. Almeida and J.N. Oliveira and Luís Neves},
  title = "\textsc{Camila} - A Platform for Software Mathematical Development",
  url="http://camila.di.uminho.pt",
  type="(Páginas do projecto)",
  institution = umdi,
  year=1998,
  keyword = "FS",
}
'''

tokens = (
   'SIGN',
   'STRING',
   'COMMA',
   'EQUAL',
   'QUOTE',
   'NUMBER',
   'LEFT_BRACE',  # Corrigido para LEFT_BRACE
   'RIGHT_BRACE'  # Corrigido para RIGHT_BRACE
)

t_SIGN = r'@'
t_STRING   = r'[a-zA-Z.áàâéèêíïóôúüç\s]+'
t_COMMA   = r','
t_EQUAL   = r'='
t_QUOTE = r'"[^"]*"'
t_NUMBER = r'\d+'
t_LEFT_BRACE = r'{'
t_RIGHT_BRACE = r'}'

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
lexer.input(data)

for tok in lexer:
    print(tok)
