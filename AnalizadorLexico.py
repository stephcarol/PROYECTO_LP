import ply.lex as lex
import os
from datetime import datetime

# Lista de tokens seleccionados
tokens = (
    'PLUS', 'MINUS', 'MINUSMINUS', 'POINT', 'TIMES', 'DIVIDE', 'EQUAL',
    'LESS', 'GREATER', 'SEMICOLON', 'COMMA', 'LPAREN', 'RPAREN', 'LBRACKET',
    'RBRACKET', 'LBLOCK', 'RBLOCK', 'QUOTES', 'MODULE', 'NOT', 'AND', 'OR',
    'BITAND', 'BITOR', 'BITXOR', 'BITNOT', 'PLUSEQUAL', 'MINUSEQUAL',
    'TIMESEQUAL', 'DIVIDEEQUAL', 'COLON', 'APOSTROPHE', 'BACKSLASH',
    'WHITESPACE', 'CLASS', 'BOOL', 'INCLUDE', 'USING', 'NAMESPACE', 'STD',
    'COUT', 'CIN', 'GET', 'ENDL', 'ELSE', 'IF', 'INT', 'RETURN', 'VOID',
    'WHILE', 'FOR', 'NUMBER', 'FLOAT', 'DOUBLE', 'CHAR', 'DO', 'CONTINUE',
    'PUBLIC', 'PRIVATE', 'STATIC', 'CONST', 'EXPLICIT', 'DELETE', 'TYPEDEF',
    'TRY', 'CATCH', 'SIZEOF', 'ID', 'STRING', 'HASH', 'PLUSPLUS', 'LESSEQUAL',
    'GREATEREQUAL', 'DEQUAL', 'LGREATER', 'RGREATER', 'DISTINT'
)

# Reglas de expresiones regulares para tokens seleccionados
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
t_CLASS = r'class'
t_BOOL = r'bool'
t_INCLUDE = r'include'
t_USING = r'using'
t_NAMESPACE = r'namespace'
t_STD = r'std'
t_COUT = r'cout'
t_CIN = r'cin'
t_GET = r'get'
t_ENDL = r'endl'
t_ELSE = r'else'
t_IF = r'if'
t_INT = r'int'
t_RETURN = r'return'
t_VOID = r'void'
t_WHILE = r'while'
t_FOR = r'for'
t_NUMBER = r'\d+'
t_FLOAT = r'float'
t_DOUBLE = r'double'
t_CHAR = r'char'
t_DO = r'do'
t_CONTINUE = r'continue'
t_PUBLIC = r'public'
t_PRIVATE = r'private'
t_STATIC = r'static'
t_CONST = r'const'
t_EXPLICIT = r'explicit'
t_DELETE = r'delete'
t_TYPEDEF = r'typedef'
t_TRY = r'try'
t_CATCH = r'catch'
t_SIZEOF = r'sizeof'
t_ID = r'\w+(_\d\w)*'
t_STRING = r'\"?(\w+ \ *\w*\d* \ *)\"?'
t_HASH = r'\#'
t_PLUSPLUS = r'\+\+'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_DEQUAL = r'=='
t_LGREATER = r'<<'
t_RGREATER = r'>>'
t_DISTINT = r'!='

# Ignorar caracteres de espacio en blanco y tabulación
t_ignore = ' \t'


# Función para manejar saltos de línea y contar números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Función para manejar comentarios de múltiples líneas
def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Función para manejar comentarios de una línea
def t_COMMENT_LINE(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1


# Función para manejar errores léxicos
def t_error(t):
    print(f"Error léxico: Carácter inesperado '{t.value[0]}'")
    t.lexer.skip(1)


# Construir el analizador léxico
lexer = lex.lex()


# Función para probar el analizador léxico
def test(data, lexer):
    lexer.input(data)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append(tok)
    return tokens_list


# Función principal para el análisis léxico
def Analizador_lexico():
    # Nombre de usuario para el log (puedes modificar esta línea según tu necesidad)
    username = input("Ingrese su nombre de usuario para el log: ")

    # Nombre y ruta del archivo a analizar (puedes modificar esta línea según tu necesidad)
    filename = input("Ingrese la direccion del archivo: ")

    # Verificar si el archivo existe
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = f.read()
        lexer = lex.lex()
        tokens_list = test(data, lexer)

        # Crear carpeta de log si no existe
        if not os.path.exists('log'):
            os.makedirs('log')

        # Formatear la fecha y hora actual
        now = datetime.now()
        timestamp = now.strftime("%d%m%Y-%Hh%M")

        # Crear nombre de archivo de log
        log_filename = f'log/lexico-{username}-{timestamp}.txt'

        # Escribir tokens al archivo de log
        with open(log_filename, 'w') as log_file:
            for token in tokens_list:
                log_file.write(str(token) + '\n')

        print(f"Análisis léxico completado. Archivo de tokens generado: {log_filename}")

    else:
        print("El archivo no existe")


# Ejecutar el analizador léxico al correr el script
if __name__ == '__main__':
    Analizador_lexico()
