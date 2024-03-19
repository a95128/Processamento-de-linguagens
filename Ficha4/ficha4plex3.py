import ply.lex as lex

data = '''
{
  "name": "John Doe",
  "age": 21,
  "gender": "male",
  "height": 1.68,
  "address": {
    "street": "123 Main Street",
    "city": "New York",
    "country": "USA",
    "zip": "10001"
  },
  "married": false,
  "hobbies": [
    {
      "name": "reading",
      "books": [
        {
          "title": "Heartstopper: Volume 1",
          "author": "Alice Oseman",
          "genres": ["Graphic Novels", "Romance", "Queer"]
        },
        {
          "title": "1984",
          "author": "George Orwell",
          "genres": ["Science Fiction", "Dystopia", "Politics"]
        }
      ]
    },
    {
      "name": "gaming",
      "games": [
        {
          "title": "Portal 2",
          "platform": ["PC", "PlayStation 3", "Xbox 360"]
        },
        {
          "title": "Synth Riders",
          "platform": ["PSVR", "PSVR2", "PCVR", "Oculus Quest"]
        }
      ]
    }
  ]
}
'''

tokens = (
   'STRING',
   'COMMA',
   'POINTS',
   'QUOTE',
   'BOOL',
   'NUMBER',
   'RIGHT_BRACKET',
   'LEFT_BRACKET',
   'LEFT_BRACE', 
   'RIGHT_BRACE' 
)

states = (
    ('parens', 'exclusive'),
    ('bracket', 'exclusive'),
)

paren_count = 0
bracket_count = 0

def t_STRING(t):
    r'[a-zA-Z]+'
    return t

def t_COMMA(t):
    r','
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ANY_ignore  = ' \t\n'

def t_POINTS(t):
    r':'
    return t

def t_QUOTE(t):
    r'"'
    return t

def t_BOOL(t):
    r'true|false'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return t

def t_LEFT_BRACKET(t):
    r'\['
    return t

def t_RIGHT_BRACKET(t):
    r'\]'
    return t

def t_LEFT_BRACE(t):
    r'\{'
    return t

def t_RIGHT_BRACE(t):
    r'\}'
    return t

def t_parens_LEFT_BRACE(t):
    r'{'
    global paren_count
    paren_count+=1
    t.lexer.begin('parens')  # Mudar para o estado 'parens'
    return t

def t_parens_RIGHT_BRACE(t):
    r'\}'
    global paren_count
    paren_count -= 1
    t.lexer.pop_state()  # Voltar para o estado anterior
    return t

def t_bracket_LEFT_BRACKET(t):
    r'\['
    global bracket_count
    bracket_count+=1
    t.lexer.begin('bracket')  # Mudar para o estado 'bracket'
    return t

def t_bracket_RIGHT_BRACKET(t):
    r'\]'
    global bracket_count
    bracket_count -= 1
    t.lexer.pop_state()  # Voltar para o estado anterior
    return t

def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(data)

for tok in lexer:
    print(tok)

if paren_count != 0:
    print("ERROR: Number of opening and closing parentheses does not match.")
else:
    print("Number of opening and closing parentheses match.")

if bracket_count != 0:
    print("ERROR: Number of opening and closing brackets does not match.")
else:
    print("Number of opening and closing brackets match.")
