import ply.yacc as yacc
from AnalizadorLexico import tokens

# Rafael Merchan ini
def p_programa(p):
    '''programa : declaracion_lista'''


def p_declaracion_lista(p):
    '''declaracion_lista : declaracion_lista declaracion
                        | declaracion'''


def p_declaracion(p):
    '''declaracion : declaracion_var
                   | declaracion_funcion'''


def p_declaracion_var(p):
    '''declaracion_var : especificador ID SEMICOLON
                       | especificador ID EQUAL expresion SEMICOLON'''


def p_especificador(p):
    '''especificador : INT
                      | FLOAT
                      | DOUBLE
                      | CHAR
                      | BOOL'''


def p_declaracion_funcion(p):
    '''declaracion_funcion : especificador ID LPAREN parametro RPAREN compound_stmt
                       | VOID ID LPAREN parametro RPAREN compound_stmt'''


def p_parametro(p):
    '''parametro : parametro_lista
              | VOID'''


def p_parametro_lista(p):
    '''parametro_lista : parametro_lista COMMA parametro
                  | parametro'''


def p_param(p):
    '''param : type_specifier ID
             | type_specifier ID LBRACKET RBRACKET'''

def p_expresion(p):
    '''expresion : variable EQUAL expresion
                  | expresion_simple'''

def p_variable(p):
    '''variable : ID
           | ID LBRACKET expresion RBRACKET'''

def p_expresion_simple(p):
    '''expresion_simple : expresion_aditiva igualdad expresion_aditiva
                         | expresion_aditiva'''

def p_igualdad(p):
    '''igualdad : LESS
             | LESSEQUAL
             | GREATER
             | GREATEREQUAL
             | DEQUAL
             | DISTINT'''

def p_expresion_aditiva(p):
    '''expresion_aditiva : expresion_aditiva sumorest termino
                           | termino'''


def p_sumorest(p):
    '''sumorest : PLUS
             | MINUS'''


def p_termino(p):
    '''termino : termino multodiv factor
            | factor'''

def p_multodiv(p):
    '''multodiv : TIMES
             | DIVIDE'''

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | variable
              | NUMBER'''


# Rafael Merchan fin


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('lp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)