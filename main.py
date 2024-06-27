import ply.yacc as yacc
from AnalizadorLexico import tokens

# Reglas de la gramática

def p_programa(p):
    '''programa : declaracion_lista'''
    pass

def p_declaracion_lista(p):
    '''declaracion_lista : declaracion_lista declaracion
                         | declaracion'''
    pass

def p_declaracion(p):
    '''declaracion : declaracion_var
                   | declaracion_funcion
                   | declaracion_EC
                   | declaracion_clase'''
    pass

def p_declaracion_var(p):
    '''declaracion_var : especificador ID SEMICOLON
                       | especificador ID EQUAL expresion SEMICOLON
                       | especificador ID EQUAL estructura_dato SEMICOLON'''
    pass

def p_especificador(p):
    '''especificador : INT
                     | FLOAT
                     | DOUBLE
                     | CHAR
                     | STRING
                     | BOOL'''
    pass

def p_declaracion_funcion(p):
    '''declaracion_funcion : especificador ID LPAREN parametro RPAREN compound_stmt
                           | VOID ID LPAREN parametro RPAREN compound_stmt'''
    pass

def p_parametro(p):
    '''parametro : parametro_lista
                 | VOID'''
    pass

def p_parametro_lista(p):
    '''parametro_lista : parametro_lista COMMA param
                       | param'''
    pass

def p_param(p):
    '''param : especificador ID
             | especificador ID LBRACKET RBRACKET'''
    pass

def p_expresion(p):
    '''expresion : ID
                 | NUMBER
                 | ID EQUAL expresion
                 | expresion_simple
                 | LPAREN expresion RPAREN'''
    pass

def p_expresion_simple(p):
    '''expresion_simple : expresion_aditiva igualdad expresion_aditiva
                        | expresion_aditiva'''
    pass

def p_igualdad(p):
    '''igualdad : LESS
                | LESSEQUAL
                | GREATER
                | GREATEREQUAL
                | DEQUAL
                | DISTINT'''
    pass

def p_expresion_aditiva(p):
    '''expresion_aditiva : expresion_aditiva sumorest termino
                         | termino'''
    pass

def p_sumorest(p):
    '''sumorest : PLUS
                | MINUS'''
    pass

def p_termino(p):
    '''termino : termino multodiv factor
               | factor'''
    pass

def p_multodiv(p):
    '''multodiv : TIMES
                | DIVIDE'''
    pass

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | declaracion_var
              | NUMBER'''
    pass

def p_estructura_dato(p):
    '''estructura_dato : array_init
                       | tuple_init
                       | vector_init'''
    pass

def p_array_init(p):
    '''array_init : LBRACKET expresion_list RBRACKET'''
    pass

def p_tuple_init(p):
    '''tuple_init : LPAREN expresion_list RPAREN'''
    pass

def p_vector_init(p):
    '''vector_init : LGREATER expresion_list RGREATER'''
    pass

def p_expresion_list(p):
    '''expresion_list : expresion_list COMMA expresion
                      | expresion
                      | empty'''
    pass

# Estructuras de control (if/if-else, switch, while)
def p_declaracion_EC(p):
    '''declaracion_EC : selection_stmt
                      | iteration_stmt'''
    pass

def p_selection_stmt(p):
    '''selection_stmt : IF LPAREN expresion RPAREN statement
                      | IF LPAREN expresion RPAREN statement ELSE statement
                      | SWITCH LPAREN expresion RPAREN statement'''
    pass

def p_iteration_stmt(p):
    '''iteration_stmt : WHILE LPAREN expresion RPAREN statement'''
    pass

def p_statement(p):
    '''statement : expresion_stmt
                 | compound_stmt'''
    pass

def p_expresion_stmt(p):
    '''expresion_stmt : expresion SEMICOLON
                      | SEMICOLON'''
    pass

def p_compound_stmt(p):
    '''compound_stmt : LBLOCK statement_list RBLOCK'''
    pass

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

# Declaraciones de clases
def p_declaracion_clase(p):
    '''declaracion_clase : class_header LBLOCK class_body RBLOCK'''
    pass

def p_class_header(p):
    '''class_header : CLASS ID
                    | CLASS ID COLON especificador'''
    pass

def p_class_body(p):
    '''class_body : class_body class_member
                  | class_member'''
    pass

def p_class_member(p):
    '''class_member : especificador ID SEMICOLON
                    | especificador ID EQUAL expresion SEMICOLON
                    | especificador ID LPAREN parametro RPAREN compound_stmt
                    | VOID ID LPAREN parametro RPAREN compound_stmt
                    | declaracion_EC'''
    pass

def p_empty(p):
    '''empty :'''
    pass

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
