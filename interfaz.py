import tkinter as tk
from tkinter import filedialog, messagebox
from AnalizadorLexico import analyze_lexical, errores_lexicos
from AnalizadorSintactico import analyze_syntax, errores_sintacticos
from AnalizadorSemantico import analyze_semantics, print_semantic_errors

class InterfazAnalizador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Analizador Completo")
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill='both', expand=True)

        # Cuadro de texto grande a la izquierda
        self.text_area = tk.Text(main_frame, wrap='word')
        self.text_area.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        # Frame a la derecha
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side='right', fill='y', padx=10, pady=10)

        # Botón "Analizar" en la parte superior derecha
        self.analyze_button = tk.Button(right_frame, text="Analizar", command=self.analyze_all)
        self.analyze_button.pack(side='top', pady=5)

        # Cuadro para los resultados del análisis debajo del botón
        self.result_area = tk.Text(right_frame, wrap='word', height=20)
        self.result_area.pack(side='bottom', fill='both', expand=True, pady=5)

    def analyze_all(self):
        input_code = self.text_area.get("1.0", tk.END)

        # Análisis léxico
        analyze_lexical(input_code)
        errores_lexicos = errores_lexicos if errores_lexicos else []

        if errores_lexicos:
            self.show_errors("Errores léxicos encontrados:", errores_lexicos)
            return

        # Análisis sintáctico
        analyze_syntax(input_code)
        errores_sintacticos = errores_sintacticos if errores_sintacticos else []

        if errores_sintacticos:
            self.show_errors("Errores sintácticos encontrados:", errores_sintacticos)
            return

        # Análisis semántico
        analyze_semantics(input_code)
        errores_semanticos = errores_semanticos if errores_semanticos else []

        if errores_semanticos:
            self.show_errors("Errores semánticos encontrados:", errores_semanticos)
        else:
            self.result_area.insert(tk.END, "Análisis semántico completado sin errores.")

    def show_errors(self, title, errors):
        self.result_area.delete("1.0", tk.END)
        self.result_area.insert(tk.END, f"{title}\n")
        for error in errors:
            self.result_area.insert(tk.END, f"{error}\n")

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                code = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, code)

    def run(self):
        self.root.mainloop()

# Ejemplo de uso
if __name__ == "__main__":
    interfaz = InterfazAnalizador()
    interfaz.run()
