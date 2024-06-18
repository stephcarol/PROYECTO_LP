# -*- coding: utf-8 -*-
import ply.lex as lex
import os 
from datetime import datetime

#Lista de tokens 
#Stephany Cabezas
tokens =(
    # Palabras Reservadas
    'INCLUDE',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
    'GET',
    'ENDL',
    'ELSE',
    'IF',
    'INT',
    'STRING',
    'RETURN',
    'VOID',
    'WHILE',
    'FOR',

    # Symbolos
    'HASH',
    'POINT',
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'SEMICOLON',
    'COMMA',
    'LGREATER',
    'RGREATER',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'QUOTES',
    
    #Otros
    'ID',
    'NUMBER',

    # Rafael Merchan ini
    # Palabras reservadas
    'FLOAT',
    'DOUBLE',
    'CHAR',
    'DO',
    'SWITCH',
    'CASE',
    'DEFAULT',
    'BREAK',
    'CONTINUE',
    'PUBLIC',
    'PRIVATE',
    'STATIC',
    'CONST',
    'EXPLICIT',
    'DELETE',
    'TYPEDEF',
    'TRY',
    'CATCH',
    'SIZEOF',
    # Simbolos
    'MODULE',
    'NOT',
    'AND',
    'OR',
    'BITAND',
    'BITOR',
    'BITXOR',
    'BITNOT',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'TIMESEQUAL',
    'DIVIDEEQUAL',
    'COLON',
    'APOSTROPHE',
    'BACKSLASH',
    # Otros
    'WHITESPACE',
    # Rafael Merchan fin

    #Sebastian Ceballos ini
    # Palabras reservadas
    'CLASS',  
    'ENUM', 
    'INLINE', 
    'FRIEND', 
    'VIRTUAL', 
    'PROTECTED', 
    'THIS', 
    'THROW',
    'GOTO', 
    'LONG', 
    'SHORT', 
    'BOOL', 
    'FINAL',
    #Simbolos
    'QUESTION', 
    'ELLIPSIS' ,
    #Otros
    'COMMENT',
    'COMMMENT_LINE',
    #Sebastian Ceballos fin
)



# Reglas de Expresiones Regualres para token de Contexto simple

t_PLUS = r'\+'
t_MINUS = r'-'
t_MINUSMINUS = r'\-\-'
t_POINT = r'\.'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_QUOTES = r'\"'
# Stephany Cabezas

# Rafael Merchan ini
t_MODULE = r'%'
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_BITAND = r'&'
t_BITOR = r'\|'
t_BITXOR = r'\^'
t_BITNOT = r'~'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVIDEEQUAL = r'/='
t_COLON = r':'
t_APOSTROPHE = r"'"
t_BACKSLASH = r'\\'
t_WHITESPACE = r'\s+'
# Rafael Merchan fin
#Sebastian Ceballos ini
t_QUESTION = r'\?'
t_ELLIPSIS = r'\.\.\.'
#Sebastian Ceballos fin

def t_INCLUDE(t):
    r'include'
    return t


def t_USING(t):
    r'using'
    return t


def t_NAMESPACE(t):
    r'namespace'
    return t


def t_STD(t):
    r'std'
    return t


def t_COUT(t):
    r'cout'
    return t


def t_CIN(t):
    r'cin'
    return t


def t_GET(t):
    r'get'
    return t


def t_ENDL(t):
    r'endl'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_IF(t):
    r'if'
    return t


def t_INT(t):
    r'int'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_VOID(t):
    r'void'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_FOR(t):
    r'for'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_ENUM(t):
    r'enum'
    return t

def t_INLINE(t):
    r'inline'
    return t

def t_FRIEND(t):
    r'friend'
    return t

def t_VIRTUAL(t):
    r'virtual'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_THIS(t):
    r'this'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_LONG(t):
    r'long'
    return t

def t_SHORT(t):
    r'short'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_DEFAULT(t):
    r'deafult'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_CASE(t):
    r'case'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
# Rafael Merchan ini
def t_FLOAT(t):
    r'float'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_DO(t):
    r'do'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_CONST(t):
    r'const'
    return t

def t_EXPLICIT(t):
    r'explicit'
    return t

def t_DELETE(t):
    r'delete'
    return t

def t_TYPEDEF(t):
    r'typedef'
    return t

def t_TRY(t):
    r'try'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_SIZEOF(t):
    r'sizeof'
    return t
# Rafael Merchan fin

#exprecion regular para reconocer los identificadores


def t_ID(t):
    r'\w+(_\d\w)*'
    return t


def t_STRING(t):
#expresion RE para reconocer los String
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t


def t_HASH(t):
    r'\#'
    return t


def t_PLUSPLUS(t):
    r'\+\+'
    return t


def t_LESSEQUAL(t):
    r'<='
    return t    


def t_GREATEREQUAL(t):
    r'>='
    return t


def t_DEQUAL(t):
    r'=='
    return t


def t_LGREATER(t):
    r'<<'
    return t


def t_RGREATER(t):
    r'>>'
    return t


def t_DISTINT(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_COMMENT_LINE(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1


def t_error(t):
    print (("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)


#Sebastian Ceballos
       
def test(data, lexer):
    lexer.input(data)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)
    return tokens_list


# Stephany Cabezas
# Función principal para el análisis léxico
def Analizador_lexico():
    
    username = input("Ingrese su nombre de usuario para el log: ")
    
    
    filename = 'test/prueba.cpp'
    filename2 = 'test/pruebaRM.cpp'
    filename3 = 'test/prueba3.cpp'
    
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = f.read()
        lexer = lex.lex()
        tokens_list = test(data, lexer)
        
        
        if not os.path.exists('log'):
            os.makedirs('log')
        
        
        now = datetime.now()
        timestamp = now.strftime("%d%m%Y-%Hh%M")
        
        
        log_filename = f'log/lexico1-{username}-{timestamp}.txt'

        # Escribir tokens al archivo de log
        with open(log_filename, 'w') as log_file:
            for token in tokens_list:
                log_file.write(str(token) + '\n')

        print(f"Análisis léxico completado. Archivo de tokens generado: {log_filename}")

    else:
        print("El archivo no existe")

    # Stephany Cabezas

    # Ejecutar el analizador léxico al correr el script
    if _name_ == '_main_':
        Analizador_lexico()
        
        
