import tkinter as tk
from tkinter import filedialog, messagebox
from AnalizadorSintactico import analyze_code, errores_sintacticos

class InterfazAnalizador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Analizador Sintáctico")
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

        # Botón "Iniciar" en la parte superior derecha
        self.analyze_button = tk.Button(right_frame, text="Iniciar", command=self.analyze_code)
        self.analyze_button.pack(side='top', pady=5)

        # Cuadro para los resultados del análisis debajo del botón
        self.result_area = tk.Text(right_frame, wrap='word', height=20)
        self.result_area.pack(side='bottom', fill='both', expand=True, pady=5)

    def analyze_code(self):
        input_code = self.text_area.get("1.0", tk.END)
        analyze_code(input_code)
        self.result_area.delete("1.0", tk.END)
        if not errores_sintacticos:
            self.result_area.insert(tk.END, "Análisis sintáctico completado sin errores.")
        else:
            errors = "\n".join(errores_sintacticos)
            self.result_area.insert(tk.END, errors)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                code = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, code)

    def run(self):
        self.root.mainloop()
