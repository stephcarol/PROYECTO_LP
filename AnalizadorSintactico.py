import ply.yacc as yacc
from AnalizadorLexico import tokens
import logging
from datetime import datetime
import os

# # Configuración del logger
# userGit = input("Ingrese su nombre de usuario para el log: ")
# now = datetime.now()
# timestamp = now.strftime("%d%m%Y-%Hh%M")

# # Asegurarse de que la carpeta "log" exista
# log_dir = "log"
# os.makedirs(log_dir, exist_ok=True)

# log_filename = os.path.join(log_dir, f'sintactico-{userGit}-{timestamp}.txt')

# logging.basicConfig(
#     filename=log_filename,
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# Tabla de símbolos
symbol_table = {
    'variables': {},
    'classes': {},
    'functions': {}
}

current_class = None

# Lista para almacenar errores sintácticos
errores_sintacticos = []

# Reglas de la gramática
def p_programa(p):
    '''programa : declaracion_lista'''
    logging.info("Reconocido programa con declaración lista")

def p_declaracion_lista(p):
    '''declaracion_lista : declaracion_lista declaracion
                         | declaracion'''
    if len(p) == 2:
        logging.info("Reconocida declaración: {}".format(p[1]))
    else:
        logging.info("Reconocida declaración lista: {} {}".format(p[1], p[2]))

def p_declaracion(p):
    '''declaracion : declaracion_var
                   | declaracion_funcion'''
    logging.info("Reconocida declaración: {}".format(p[1]))

def p_especificador(p):
    '''especificador : INT
                     | FLOAT'''
    p[0] = p[1]
    logging.info("Reconocido especificador: {}".format(p[1]))

# Verificar declaración de variables
def p_declaracion_var(p):
    '''declaracion_var : especificador ID SEMICOLON
                       | especificador ID EQUAL expresion SEMICOLON
                       | especificador ID EQUAL estructura_dato SEMICOLON'''
    if len(p) == 4:
        if p[2] in symbol_table['variables']:
            errores_sintacticos.append(f"Error: Variable '{p[2]}' ya declarada.")
        else:
            symbol_table['variables'][p[2]] = {'type': p[1], 'value': None}
    else:
        if p[2] in symbol_table['variables']:
            errores_sintacticos.append(f"Error: Variable '{p[2]}' ya declarada.")
        else:
            symbol_table['variables'][p[2]] = {'type': p[1], 'value': p[4]}
    if len(p) == 4:
        logging.info("Reconocida declaración de variable: {} {};".format(p[1], p[2]))
    elif len(p) == 6 and isinstance(p[4], str):
        logging.info("Reconocida declaración de variable con asignación: {} {} = {};".format(p[1], p[2], p[4]))
    else:
        logging.info("Reconocida declaración de variable con estructura de datos: {} {} = {};".format(p[1], p[2], p[4]))

def p_estructura_dato(p):
    '''estructura_dato : expresion
                       | estructura_compuesta'''
    p[0] = p[1]
    logging.info("Reconocida estructura de dato: {}".format(p[1]))

def p_estructura_compuesta(p):
    '''estructura_compuesta : declaracion_lista
                            | compound_stmt
                            | tupla'''
    p[0] = p[1]
    logging.info("Reconocida estructura compuesta: {}".format(p[1]))

def p_tupla(p):
    '''tupla : LPAREN elementos RPAREN'''
    p[0] = {'tipo': 'tupla', 'elementos': p[2]}
    logging.info("Reconocida tupla: {}".format(p[0]))

def p_elementos(p):
    '''elementos : elementos COMMA NUMBER
                 | NUMBER'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_igualdad(p):
    '''igualdad : DEQUAL'''
    p[0] = p[1]
    logging.info("Reconocido operador de igualdad: {}".format(p[1]))

# Verificar declaración de funciones
def p_declaracion_funcion(p):
    '''declaracion_funcion : especificador ID LPAREN parametro RPAREN compound_stmt'''
    if p[1] == 'void':
        logging.info("Reconocida declaración de función void: {}({}) {}".format(p[2], p[4], p[6]))
    else:
        logging.info("Reconocida declaración de función: {} {}({}) {}".format(p[1], p[2], p[4], p[6]))

def p_parametro(p):
    '''parametro : especificador ID
                 | parametro COMMA especificador ID'''
    if len(p) == 3:
        p[0] = [{'type': p[1], 'name': p[2]}]
        logging.info("Reconocido parámetro: {} {}".format(p[1], p[2]))
    elif len(p) == 5:
        p[0] = p[1] + [{'type': p[3], 'name': p[4]}]
        logging.info("Reconocido parámetro: {}, {} {}".format(p[1], p[3], p[4]))

def p_compound_stmt(p):
    '''compound_stmt : LBLOCK declaracion_lista RBLOCK'''
    p[0] = p[2]
    logging.info("Reconocido bloque de declaración: {{ {} }}".format(p[2]))

# Verificar asignaciones y expresiones
def p_expresion(p):
    '''expresion : ID
                 | NUMBER
                 | ID EQUAL expresion
                 | expresion_simple
                 | LPAREN expresion RPAREN'''
    if len(p) == 2 and p[1] not in symbol_table['variables']:
        errores_sintacticos.append(f"Error: Variable '{p[1]}' no declarada.")
    elif len(p) == 4 and p[1] not in symbol_table['variables']:
        errores_sintacticos.append(f"Error: Variable '{p[1]}' no declarada.")
    if len(p) == 2:
        logging.info("Reconocida expresión: {}".format(p[1]))
    elif len(p) == 4 and p[2] == '=':
        logging.info("Reconocida expresión de asignación: {} = {}".format(p[1], p[3]))
    elif len(p) == 4:
        logging.info("Reconocida expresión con paréntesis: ({})".format(p[2]))

# Validar expresiones simples y operadores
def p_expresion_simple(p):
    '''expresion_simple : expresion_aditiva igualdad expresion_aditiva
                        | expresion_aditiva'''
    if len(p) == 4:
        logging.info("Reconocida expresión simple con igualdad: {} {} {}".format(p[1], p[2], p[3]))
    else:
        logging.info("Reconocida expresión aditiva: {}".format(p[1]))

# Validar tipos en operaciones aditivas
def p_expresion_aditiva(p):
    '''expresion_aditiva : termino sumorest expresion_aditiva
                         | termino'''
    if len(p) > 1:
        if len(p) == 4:
            if p[1] != p[3]:
                errores_sintacticos.append(f"Error: Tipos incompatibles en operación aditiva: '{p[1]}' y '{p[3]}'.")
            p[0] = p[1]
            logging.info("Reconocida expresión aditiva: {} {} {}".format(p[1], p[2], p[3]))
        else:
            p[0] = p[1]
            logging.info("Reconocido término: {}".format(p[1]))

# Validar tipos en operadores aditivos
def p_sumorest(p):
    '''sumorest : PLUS
                | MINUS'''
    logging.info("Reconocido operador aditivo: {}".format(p[1]))

# Verificar alcance de variables
def p_variable_scope(p):
    '''variable_scope : ID'''
    if p[1] not in symbol_table['variables']:
        errores_sintacticos.append(f"Error: Variable '{p[1]}' utilizada fuera de su alcance.")
    logging.info("Reconocido acceso a variable: {}".format(p[1]))

def p_termino(p):
    '''termino : factor'''
    p[0] = p[1]
    logging.info("Reconocido término: {}".format(p[1]))

def p_factor(p):
    '''factor : ID
              | NUMBER
              | LPAREN expresion RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
        logging.info("Reconocido factor: {}".format(p[1]))
    elif len(p) == 4:
        p[0] = p[2]
        logging.info("Reconocido factor con paréntesis: ({})".format(p[2]))

# Regla para errores sintácticos
def p_error(p):
    error_msg = f"Error sintáctico en la entrada: {p}"
    logging.error(error_msg)
    errores_sintacticos.append(error_msg)
    print(error_msg)

# Construir el parser
parser = yacc.yacc()

# Función principal para analizar código de entrada
def analyze_syntax(input_code):
    global errores_sintacticos
    errores_sintacticos = []  # Resetear la lista de errores
    parser.parse(input_code)
    return errores_sintacticos

# Ejemplo de uso
# input_code = "int a; float b; int a = 5;"
# errores = analyze_syntax(input_code)
# print("Errores sintácticos encontrados:", errores)
