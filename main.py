import ply.yacc as yacc
from AnalizadorLexico import tokens
import logging
from datetime import datetime
import os

# Configuración del logger
userGit = input("Ingrese su nombre de usuario para el log: ")
now = datetime.now()
timestamp = now.strftime("%d%m%Y-%Hh%M")

# Asegurarse de que la carpeta "log" exista
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

log_filename = os.path.join(log_dir, f'sintactico-{userGit}-{timestamp}.txt')

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
#Semantica Sebastian Ceballos
# Tabla de símbolos
symbol_table = {
    'variables': {},
    'classes': {}
}

errores_semantica = []
# Reglas de la gramática

def p_programa(p):
    '''programa : declaracion_lista'''
    logging.info("Reconocido programa con declaración lista")

def p_declaracion_lista(p):
    '''declaracion_lista : declaracion_lista declaracion
                         | declaracion'''
    if len(p) == 3:
        logging.info("Reconocida declaración lista: {}, {}".format(p[1], p[2]))
    else:
        logging.info("Reconocida declaración: {}".format(p[1]))

def p_declaracion(p):
    '''declaracion : declaracion_var
                   | declaracion_funcion
                   | declaracion_EC
                   | declaracion_clase'''
    logging.info("Reconocida declaración: {}".format(p[1]))

#Semantica Sebastian Ceballos
def p_declaracion_var(p):
    '''declaracion_var : especificador ID SEMICOLON
                       | especificador ID EQUAL expresion SEMICOLON
                       | especificador ID EQUAL estructura_dato SEMICOLON'''
    if len(p) == 4:
        if p[2] in symbol_table['variables']:
            errores_semantica.append(f"Error: Variable '{p[2]}' ya declarada.")
        else:
            symbol_table['variables'][p[2]] = {'type': p[1], 'value': None}
    else:
        if p[2] in symbol_table['variables']:
            errores_semantica.append(f"Error: Variable '{p[2]}' ya declarada.")
        else:
            symbol_table['variables'][p[2]] = {'type': p[1], 'value': p[4]}
    if len(p) == 4:
        logging.info("Reconocida declaración de variable: {} {};".format(p[1], p[2]))
    elif len(p) == 6 and isinstance(p[4], str):
        logging.info("Reconocida declaración de variable con asignación: {} {} = {};".format(p[1], p[2], p[4]))
    else:
        logging.info("Reconocida declaración de variable con estructura de datos: {} {} = {};".format(p[1], p[2], p[4]))

def p_especificador(p):
    '''especificador : INT
                     | FLOAT
                     | DOUBLE
                     | CHAR
                     | STRING
                     | BOOL'''
    p[0] = p[1]
    logging.info("Reconocido especificador: {}".format(p[1]))

def p_declaracion_funcion(p):
    '''declaracion_funcion : especificador ID LPAREN parametro RPAREN compound_stmt
                           | VOID ID LPAREN parametro RPAREN compound_stmt'''
    if p[1] == 'void':
        logging.info("Reconocida declaración de función void: {}({}) {}".format(p[2], p[4], p[6]))
    else:
        logging.info("Reconocida declaración de función: {} {}({}) {}".format(p[1], p[2], p[4], p[6]))

def p_parametro(p):
    '''parametro : parametro_lista
                 | VOID'''
    logging.info("Reconocidos parámetros: {}".format(p[1]))

def p_parametro_lista(p):
    '''parametro_lista : parametro_lista COMMA param
                       | param'''
    if len(p) == 4:
        logging.info("Reconocida lista de parámetros: {}, {}".format(p[1], p[3]))
    else:
        logging.info("Reconocido parámetro: {}".format(p[1]))

def p_param(p):
    '''param : especificador ID
             | especificador ID LBRACKET RBRACKET'''
    if len(p) == 3:
        logging.info("Reconocido parámetro: {} {}".format(p[1], p[2]))
    else:
        logging.info("Reconocido parámetro array: {} {}[]".format(p[1], p[2]))

#Semantica Sebastian Ceballos
def p_expresion(p):
    '''expresion : ID
                 | NUMBER
                 | ID EQUAL expresion
                 | expresion_simple
                 | LPAREN expresion RPAREN'''
    if len(p) == 2 and p[1] not in symbol_table['variables']:
        errores_semantica.append(f"Error: Variable '{p[1]}' no declarada.")
    elif len(p) == 4 and p[1] not in symbol_table['variables']:
        errores_semantica.append(f"Error: Variable '{p[1]}' no declarada.")
    if len(p) == 2:
        logging.info("Reconocida expresión: {}".format(p[1]))
    elif len(p) == 4 and p[2] == '=':
        logging.info("Reconocida expresión de asignación: {} = {}".format(p[1], p[3]))
    elif len(p) == 4:
        logging.info("Reconocida expresión con paréntesis: ({})".format(p[2]))

def p_expresion_simple(p):
    '''expresion_simple : expresion_aditiva igualdad expresion_aditiva
                        | expresion_aditiva'''
    if len(p) == 4:
        logging.info("Reconocida expresión simple con igualdad: {} {} {}".format(p[1], p[2], p[3]))
    else:
        logging.info("Reconocida expresión aditiva: {}".format(p[1]))

def p_igualdad(p):
    '''igualdad : LESS
                | LESSEQUAL
                | GREATER
                | GREATEREQUAL
                | DEQUAL
                | DISTINT'''
    logging.info("Reconocido operador de igualdad: {}".format(p[1]))

def p_expresion_aditiva(p):
    '''expresion_aditiva : expresion_aditiva sumorest termino
                         | termino'''
    if len(p) == 4:
        logging.info("Reconocida expresión aditiva: {} {} {}".format(p[1], p[2], p[3]))
    else:
        logging.info("Reconocido término: {}".format(p[1]))

def p_sumorest(p):
    '''sumorest : PLUS
                | MINUS'''
    logging.info("Reconocido operador aditivo: {}".format(p[1]))

def p_termino(p):
    '''termino : termino multodiv factor
               | factor'''
    if len(p) == 4:
        logging.info("Reconocido término con multiplicación/división: {} {} {}".format(p[1], p[2], p[3]))
    else:
        logging.info("Reconocido factor: {}".format(p[1]))

def p_multodiv(p):
    '''multodiv : TIMES
                | DIVIDE'''
    logging.info("Reconocido operador de multiplicación/división: {}".format(p[1]))

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | declaracion_var
              | NUMBER'''
    if len(p) == 4:
        logging.info("Reconocido factor con paréntesis: ({})".format(p[2]))
    elif len(p) == 2 and isinstance(p[1], str):
        logging.info("Reconocido variable: {}".format(p[1]))
    elif len(p) == 2 and isinstance(p[1], (int, float)):
        logging.info("Reconocido número: {}".format(p[1]))

def p_estructura_dato(p):
    '''estructura_dato : array_init
                       | tuple_init
                       | vector_init'''
    logging.info("Reconocida estructura de datos: {}".format(p[1]))

def p_array_init(p):
    '''array_init : LBRACKET expresion_list RBRACKET'''
    logging.info("Reconocido inicializador de array: [{}]".format(p[2]))

def p_tuple_init(p):
    '''tuple_init : LPAREN expresion_list RPAREN'''
    logging.info("Reconocido inicializador de tupla: ({})".format(p[2]))

def p_vector_init(p):
    '''vector_init : LGREATER expresion_list RGREATER'''
    logging.info("Reconocido inicializador de vector: <{}>".format(p[2]))

def p_expresion_list(p):
    '''expresion_list : expresion_list COMMA expresion
                      | expresion
                      | empty'''
    if len(p) == 4:
        logging.info("Reconocida lista de expresiones: {}, {}".format(p[1], p[3]))
    elif len(p) == 2:
        logging.info("Reconocida expresión: {}".format(p[1]))
    else:
        logging.info("Reconocida lista vacía")

def p_declaracion_EC(p):
    '''declaracion_EC : selection_stmt
                      | iteration_stmt'''
    logging.info("Reconocida declaración de estructura de control: {}".format(p[1]))

def p_selection_stmt(p):
    '''selection_stmt : IF LPAREN expresion RPAREN statement
                      | IF LPAREN expresion RPAREN statement ELSE statement
                      | SWITCH LPAREN expresion RPAREN statement'''
    if len(p) == 6 and p[1] == 'if':
        logging.info("Reconocida sentencia if: if ({}) {}".format(p[3], p[5]))
    elif len(p) == 8:
        logging.info("Reconocida sentencia if-else: if ({}) {} else {}".format(p[3], p[5], p[7]))
    else:
        logging.info("Reconocida sentencia switch: switch ({}) {}".format(p[3], p[5]))

def p_iteration_stmt(p):
    '''iteration_stmt : WHILE LPAREN expresion RPAREN statement'''
    logging.info("Reconocida sentencia while: while ({}) {}".format(p[3], p[5]))

def p_statement(p):
    '''statement : expresion_stmt
                 | compound_stmt'''
    logging.info("Reconocida sentencia: {}".format(p[1]))

def p_expresion_stmt(p):
    '''expresion_stmt : expresion SEMICOLON
                      | SEMICOLON'''
    if len(p) == 3:
        logging.info("Reconocida sentencia de expresión: {};".format(p[1]))
    else:
        logging.info("Reconocida sentencia vacía")

def p_compound_stmt(p):
    '''compound_stmt : LBLOCK statement_list RBLOCK'''
    logging.info("Reconocida sentencia compuesta: {{ {} }}".format(p[2]))

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        logging.info("Reconocida lista de sentencias: {}, {}".format(p[1], p[2]))
    else:
        logging.info("Reconocida sentencia: {}".format(p[1]))

def p_declaracion_clase(p):
    '''declaracion_clase : class_header LBLOCK class_body RBLOCK'''
    logging.info("Reconocida declaración de clase: {} {{ {} }}".format(p[1], p[3]))

#Semantica Sebastian Ceballos
def p_class_header(p):
    '''class_header : CLASS ID
                    | CLASS ID COLON especificador'''
    if p[2] in symbol_table['classes']:
        errores_semantica.append(f"Error: Clase '{p[2]}' ya declarada.")
    else:
        symbol_table['classes'][p[2]] = {'base': p[4] if len(p) == 5 else None, 'members': {}}
    if len(p) == 3:
        logging.info("Reconocido encabezado de clase: class {}".format(p[2]))
    else:
        logging.info("Reconocido encabezado de clase: class {} : {}".format(p[2], p[4]))

def p_class_body(p):
    '''class_body : class_body class_member
                  | class_member'''
    if len(p) == 3:
        logging.info("Reconocido cuerpo de clase: {}, {}".format(p[1], p[2]))
    else:
        logging.info("Reconocido miembro de clase: {}".format(p[1]))

#Semantica Sebastian Ceballos
def p_class_member(p):
    '''class_member : especificador ID SEMICOLON
                    | especificador ID EQUAL expresion SEMICOLON
                    | especificador ID LPAREN parametro RPAREN compound_stmt
                    | VOID ID LPAREN parametro RPAREN compound_stmt
                    | declaracion_EC'''
    if p[2] in symbol_table['classes'][current_class]['members']:
        errores_semantica.append(f"Error: Miembro '{p[2]}' ya declarado en la clase '{current_class}'.")
    else:
        if len(p) == 4:
            symbol_table['classes'][current_class]['members'][p[2]] = {'type': p[1], 'value': None}
        elif len(p) == 6 and p[3] == '=':
            symbol_table['classes'][current_class]['members'][p[2]] = {'type': p[1], 'value': p[4]}
        else:
            symbol_table['classes'][current_class]['members'][p[2]] = {'type': p[1], 'params': p[4], 'body': p[6]}
    if len(p) == 4:
        logging.info("Reconocido miembro de clase: {} {};".format(p[1], p[2]))
    elif len(p) == 6 and p[3] == '=':
        logging.info("Reconocido miembro de clase con asignación: {} {} = {};".format(p[1], p[2], p[4]))
    elif len(p) == 7:
        if p[1] == 'void':
            logging.info("Reconocida función miembro void: {}({}) {}".format(p[2], p[4], p[6]))
        else:
            logging.info("Reconocida función miembro: {} {}({}) {}".format(p[1], p[2], p[4], p[6]))
    else:
        logging.info("Reconocida declaración de estructura de control en clase: {}".format(p[1]))

def p_empty(p):
    '''empty :'''
    logging.info("Reconocida producción vacía")

# Error rule for syntax errors
def p_error(p):
    logging.error("Error de sintaxis en la entrada: {}".format(p))
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
    if errores_semantica:
        print("Errores semánticos encontrados:")
        for error in errores_semantica:
            print(error)
        errores_semantica.clear()
