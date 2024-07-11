# AnalizadorSintactico.py

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

# Reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LESS', 'LESSEQUAL', 'GREATER', 'GREATEREQUAL', 'DEQUAL', 'DISTINT'),
    ('right', 'EQUAL')
)

# Tabla de símbolos
symbol_table = {
    'variables': {},
    'classes': {}
}
current_class = None

# Errores sintácticos
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


# Verificar declaración de funciones
def p_declaracion_funcion(p):
    '''declaracion_funcion : especificador ID LPAREN parametro RPAREN compound_stmt
                           | VOID ID LPAREN parametro RPAREN compound_stmt'''
    if p[1] == 'void':
        logging.info("Reconocida declaración de función void: {}({}) {}".format(p[2], p[4], p[6]))
    else:
        logging.info("Reconocida declaración de función: {} {}({}) {}".format(p[1], p[2], p[4], p[6]))


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
    '''expresion_aditiva : expresion_aditiva sumorest termino
                         | termino'''
    if len(p) == 4:
        logging.info("Reconocida expresión aditiva: {} {} {}".format(p[1], p[2], p[3]))
    else:
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


# Regla para errores sintácticos
def p_error(p):
    logging.error("Error sintáctico en la entrada: {}".format(p))
    print("Error sintáctico en la entrada!")


# Construir el analizador sintáctico
parser = yacc.yacc()


# Función principal para analizar código de entrada
def analyze_code(input_code):
    result = parser.parse(input_code)
    return result


# Código de prueba
if __name__ == '__main__':
    input_code = '''
    int a = 5;
    float b = 3.14;

    void sum(int x, int y) {
        int result = x + y;
    }

    a = 10;
    b = a + 2.5;
    sum(a, 5);
    '''

    result = analyze_code(input_code)
    if not errores_sintacticos:
        print("Análisis sintáctico completado sin errores.")
    else:
        print("Se encontraron errores sintácticos:")
        for error in errores_sintacticos:
            print(error)
