import ply.lex as lex
import sys

states = (
    ('codeativo', 'exclusive'),
    ('boldativo', 'exclusive'),
    ('italativo', 'exclusive'),
    ('blockqativo', 'exclusive'),
    ('inlinecode', 'exclusive'),
    ('list', 'exclusive'),
)

tokens = (
    'HEADING',
    'BOLD',
    'ITALIC',
    'BULLET_POINT',
    'NUMBERED_LIST',
    'BLOCKQUOTE',
    'INLINE_CODE',
    'CODE_BLOCK',
    'NEWLINE',
    'TEXT'
)

t_ANY_ignore = r' '

def t_NEWLINE(t):
    r'\n'
    return t

def t_HEADING(t):
    r'\#{1,6}\s.*'
    return t

def t_BOLD(t):
    r'\*\*'
    t.lexer.begin('boldativo')
    return t

def t_boldativo_BOLD(t):
    r'\*\*'
    t.lexer.begin('INITIAL')
    return t

def t_ITALIC(t):
    r'\*'
    t.lexer.begin('italativo')
    return t

def t_italativo_ITALIC(t):
    r'\*'
    t.lexer.begin('INITIAL')
    return t

def t_BULLET_POINT(t):
    r'-\s.*'
    t.lexer.begin('list')
    return t

def t_NUMBERED_LIST(t):
    r'\d+\.\s.*'
    t.lexer.begin('list')
    return t

def t_list_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t

def t_BLOCKQUOTE(t):
    r'>\s.*'
    t.lexer.begin('blockqativo')
    return t

def t_blockqativo_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return t

def t_INLINE_CODE(t):
    r'`[^`]+`'
    t.value = t.value[1:-1]  # Remover as crases do valor do token
    return t

def t_CODE_BLOCK(t):
    r'```.*?```'
    t.lexer.begin('CODE_BLOCK')
    return t

def t_ANY_TEXT(t):
    r'.+'
    return t

def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

data = '''

# This is a heading

## This is a subheading

This is some **bold** text.

This is some *italic* text.

- This is a bullet point
- This is another bullet point

1. This is a numbered list
2. This is another numbered list item

> This is a blockquote.

`This is some inline code.`

```python
# This is some code block
print("Hello, world!")
```

'''

lexer = lex.lex()

lexer.input(data)

for token in lexer:
    print(token)