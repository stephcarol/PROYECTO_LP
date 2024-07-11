# AnalizadorSemantico.py

from AnalizadorSintactico import parser, symbol_table, errores_sintacticos
import logging

# Configuración del logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Errores semánticos
errores_semanticos = []

# Función para realizar análisis semántico
def analyze_semantics(input_code):
    parser.parse(input_code)
    if not errores_sintacticos:
        check_variable_scope()
        check_variable_assignment()
    else:
        logging.error("Errores sintácticos encontrados, no se realizó el análisis semántico.")

# Verificar el alcance de las variables
def check_variable_scope():
    for var in symbol_table['variables']:
        if not symbol_table['variables'][var]['value']:
            logging.warning(f"Variable '{var}' declarada pero no inicializada.")

# Verificar la asignación de variables
def check_variable_assignment():
    for var in symbol_table['variables']:
        if symbol_table['variables'][var]['value'] is None:
            errores_semanticos.append(f"Error: Variable '{var}' utilizada antes de asignarle un valor.")

# Función para imprimir errores semánticos
def print_semantic_errors():
    if errores_semanticos:
        print("Se encontraron errores semánticos:")
        for error in errores_semanticos:
            print(error)
    else:
        print("Análisis semántico completado sin errores.")

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

    analyze_semantics(input_code)
    print_semantic_errors()
