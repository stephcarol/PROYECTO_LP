from AnalizadorSintactico import parser, symbol_table, analyze_syntax

# Lista para almacenar errores semánticos
errores_semanticos = []

# Función para realizar análisis semántico
def analyze_semantics(input_code):
    global errores_semanticos
    errores_semanticos = []  # Reiniciar la lista de errores semánticos
    parser.parse(input_code)
    errores_sintacticos = analyze_syntax(input_code)
    if not errores_sintacticos:
        check_variable_scope()
        check_variable_assignment()
        check_function_calls()
        check_type_consistency()
    return errores_semanticos

# Verificar el alcance de las variables
def check_variable_scope():
    for var in symbol_table['variables']:
        if not symbol_table['variables'][var]['value']:
            errores_semanticos.append(f"Warning: Variable '{var}' declarada pero no inicializada.")

# Verificar la asignación de variables
def check_variable_assignment():
    for var in symbol_table['variables']:
        if symbol_table['variables'][var]['value'] is None:
            errores_semanticos.append(f"Error: Variable '{var}' utilizada antes de asignarle un valor.")

# Verificar llamadas a funciones definidas
def check_function_calls():
    for func in symbol_table['functions']:
        if func not in symbol_table['functions']:
            errores_semanticos.append(f"Error: Llamada a función no definida: '{func}'.")

# Verificar consistencia de tipos en asignaciones y expresiones
def check_type_consistency():
    for var in symbol_table['variables']:
        if symbol_table['variables'][var]['value'] is not None:
            var_type = type(symbol_table['variables'][var]['value'])
            if var_type != symbol_table['variables'][var]['type']:
                errores_semanticos.append(f"Error: Tipo incorrecto para variable '{var}'. Esperado '{symbol_table['variables'][var]['type']}', recibido '{var_type}'.")
