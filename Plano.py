import tkinter as tk
from tkinter import ttk

# Clase para manejar cuartos
class Estructura:
    def __init__(self, canvas):
        self.canvas = canvas
        self.cuarto_count = 0
        self.cuartos = {}

    def dibujar_Cuarto(self, x1, y1, x2, y2, grosor, text):
        
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#F6FAB9", outline="", tags=(text, text))
        self.canvas.create_rectangle(x1, y1, x2, y1 + grosor, fill="#6F4E37", outline="", tags=(text, text))
        self.canvas.create_rectangle(x1, y1, x1 + grosor, y2, fill="#6F4E37", outline="", tags=(text, text))
        self.canvas.create_rectangle(x1, y2, x2, y2 + grosor, fill="#6F4E37", outline="", tags=(text, text))
        self.canvas.create_rectangle(x2, y1, x2 + grosor, y2 + grosor, fill="#6F4E37", outline="", tags=(text, text))
        self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=text, tags=(text, text), fill='blue')
        self.cuartos[text] = (x1, y1, x2, y2)
        

# Clase para manejar ventanas y puertas
class Elemento:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ventana_count = 0
        self.puerta_count = 0

    def dibujar_Ventana(self, x1, y1, longitud, text, cuarto_id):
        self.canvas.create_rectangle(x1, y1, x1 + longitud, y1 + 10, fill="#EEEEEE", tags=(text, cuarto_id))
        self.canvas.create_line(x1, y1 + 4, x1 + longitud, y1 + 4, fill="black", tags=(text, cuarto_id))
        self.canvas.create_text(x1 + longitud // 2, y1 - 8, text=text, tags=(text, cuarto_id), fill='red')

    def dibujar_Puerta(self, x1, y1, longitud, text, cuarto_id):
        self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + longitud, fill="#A7E6FF", tags=(text, cuarto_id))
        self.canvas.create_line(x1 - longitud, y1 + longitud, x1, y1 + longitud, width="2", tags=(text, cuarto_id))
        self.canvas.create_arc(x1 - longitud, y1 + 5, x1 + 65, y1 + 128, start=90, extent=90, style=tk.PIESLICE, width=1, outline='black', tags=(text, cuarto_id))
        for i, char in enumerate(text):
            self.canvas.create_text(x1 + 25, y1 + i * 11, text=char, tags=(text, cuarto_id), fill='red')
#incluir aqui la clase mueble para crear muebles

# Clase para manejar la ventana principal, canvas y eventos
class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Diseñador de cuartos")

        self.canvas = tk.Canvas(root, width=800, height=550)
        self.canvas.pack()

        self.estructura = Estructura(self.canvas)
        self.elemento = Elemento(self.canvas)
        
        
        self.label = tk.Label(root, text="Selecciona una estructura")
        self.label.pack(pady=10)
        # Frame para los widgets
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        opciones = ["cuarto", "ventana", "puerta"]
        self.seleccion = tk.StringVar()

        self.combo_box = ttk.Combobox(self.control_frame, textvariable=self.seleccion)
        self.combo_box['values'] = opciones
        self.combo_box.pack(side=tk.LEFT, padx=5)
        self.combo_box.bind("<<ComboboxSelected>>", self.handle_selection)

        label_ancho = tk.Label(self.control_frame, text="Ancho:")
        label_ancho.pack(side=tk.LEFT, padx=5)

        self.entry_ancho = tk.Entry(self.control_frame)
        self.entry_ancho.pack(side=tk.LEFT, padx=5)

        label_largo = tk.Label(self.control_frame, text="Largo:")
        label_largo.pack(side=tk.LEFT, padx=5)

        self.entry_largo = tk.Entry(self.control_frame)
        self.entry_largo.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(self.control_frame, text="Eliminar", command=self.delete_structure)
        delete_button.pack(side=tk.LEFT, padx=5)

        command_entry_label = tk.Label(self.control_frame, text="Introduce un comando:")
        command_entry_label.pack(side=tk.LEFT, padx=5)

        self.command_entry = tk.Entry(self.control_frame)
        self.command_entry.pack(side=tk.LEFT, padx=5)
        self.command_entry.bind("<Return>", self.process_command)

        self.current_item = None
        self.start_x = 0
        self.start_y = 0

        self.canvas.bind("<Button-3>", self.on_canvas_click)
        self.canvas.bind("<ButtonPress-1>", self.start_move)
        self.canvas.bind("<B1-Motion>", self.move)
        

        # Crear un cuarto inicial para probar
        x1, y1 = 300, 50
        x2, y2 = 460, 260
        grosor = 10
        self.estructura.dibujar_Cuarto(x1, y1, x2, y2, grosor, "cuarto0")

    def handle_selection(self, event):
        self.selected_structure = self.combo_box.get()
        

    def on_canvas_click(self, event):
        x1, y1 = event.x, event.y
        if self.selected_structure == 'ventana':
            self.elemento.ventana_count += 1
            text = f"ventana{self.elemento.ventana_count}"
            self.elemento.dibujar_Ventana(x1, y1, 80, text, "")
        elif self.selected_structure == 'puerta':
            self.elemento.puerta_count += 1
            text = f"puerta{self.elemento.puerta_count}"
            self.elemento.dibujar_Puerta(x1, y1, 70, text, "")
        elif self.selected_structure == 'cuarto':
            self.estructura.cuarto_count += 1
            text = f"cuarto{self.estructura.cuarto_count}"
            try:
                ancho = int(self.entry_ancho.get())
                largo = int(self.entry_largo.get())
            except ValueError:
                self.label.config(text="Por favor ingresa valores numéricos válidos para ancho y largo.")
                return
            x2, y2 = x1 + ancho, y1 + largo
            grosor = 10
            self.estructura.dibujar_Cuarto(x1, y1, x2, y2, grosor, text)

    def start_move(self, event):
        items = self.canvas.find_closest(event.x, event.y)
        if items:
            self.current_item = items[0]
            tags = self.canvas.gettags(self.current_item)
            if tags:
                self.current_item = tags[0]
            self.start_x = event.x
            self.start_y = event.y
            self.label.config(text=f"Seleccionado: {self.current_item}")
            self.canvas.tag_raise(self.current_item)

    def move(self, event):
        if self.current_item:
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            self.canvas.move(self.current_item, dx, dy)
            self.start_x = event.x
            self.start_y = event.y

    
    def delete_structure(self):
        self.label.config(text=f"se elimino: {self.current_item}")
        if self.current_item:
            self.canvas.delete(self.current_item)
            self.label.config(text=f"se elimino: {self.current_item}")
            self.current_item = None
#funcion para procesar comandos
    def process_command(self, event):
        """
        para crear estructuras comando=> 'crear cuarto <nombre>', 'crear ventana/puerta <nombre cuarto>'
        para eliminar comando => 'eliminar <nombre>'
        """
        command = self.command_entry.get().strip().lower()
        parts = command.split()
        if len(parts) < 2:
            self.label.config(text="Comando no válido.")
            return

        action = parts[0]
        tipo = parts[1]

        if action == "crear" and len(parts) == 3:
            nombre = parts[2]
            if tipo == "cuarto":
                self.estructura.cuarto_count += 1
                try:
                    ancho = int(self.entry_ancho.get())
                    largo = int(self.entry_largo.get())
                except ValueError:
                    self.label.config(text="Por favor ingresa valores numéricos válidos para ancho y largo.")
                    return
                x1, y1 = 50 + (self.estructura.cuarto_count - 1) * 200, 50  # Coordenadas fijas para la creación de cuartos (se puede mejorar)
                x2, y2 = x1 + ancho, y1 + largo
                grosor = 10
                self.estructura.dibujar_Cuarto(x1, y1, x2, y2, grosor, nombre)
            elif tipo in ["ventana", "puerta"]:
                cuarto_id = nombre
                if cuarto_id not in self.estructura.cuartos:
                    self.label.config(text="Cuarto no encontrado.")
                    return
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                if tipo == "ventana":
                    self.elemento.ventana_count += 1
                    text = f"ventana{self.elemento.ventana_count}"
                    self.elemento.dibujar_Ventana(x1 + 20, y1 + 20, 80, text, cuarto_id)
                elif tipo == "puerta":
                    self.elemento.puerta_count += 1
                    text = f"puerta{self.elemento.puerta_count}"
                    self.elemento.dibujar_Puerta(x1 + 20, y1 + 50, 70, text, cuarto_id)
        elif action == "eliminar" and len(parts) == 2:
            nombre = parts[1]
            self.canvas.delete(nombre)
            self.label.config(text=f"Se eliminó: {nombre}")
        elif action == "mover":
            self.label.config(text="Funcionalidad de mover no implementada.")
        else:
            self.label.config(text="Acción no reconocida. Usa 'crear', 'eliminar' o 'mover'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
