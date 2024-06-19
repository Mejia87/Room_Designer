import tkinter as tk
from tkinter import ttk
import estructura as EstructuraModule
import elemento as ElementoModule
import mueble as MuebleModule

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Diseñador de cuartos")
        self.canvas = tk.Canvas(root, width=800, height=550)
        self.canvas.pack()

        self.estructura = EstructuraModule.Estructura(self.canvas)
        self.elemento = ElementoModule.Elemento(self.canvas)
        self.mueble = MuebleModule.Mueble(self.canvas)
        
        self.label = tk.Label(root, text="Selecciona una estructura")
        self.label.pack(pady=10)
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        opciones = ["cuarto", "ventana", "puerta"]
        self.seleccion = tk.StringVar()

        self.combo_box = ttk.Combobox(self.control_frame, textvariable=self.seleccion)
        self.combo_box['values'] = opciones
        self.combo_box.pack(side=tk.LEFT, padx=5)
        self.combo_box.bind("<<ComboboxSelected>>", self.handle_selection)

        mueble_combobox = ttk.Combobox(self.control_frame, values=["cama", "sofa", "lampara", "mesa", "silla", "inodoro", "horno"])
        mueble_combobox.pack(side=tk.LEFT, padx=5)
        mueble_combobox.bind("<<ComboboxSelected>>", lambda event: self.crear_mueble(mueble_combobox.get()))
        
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

        x1, y1 = 300, 50
        x2, y2 = 460, 260
        grosor = 10
        self.estructura.dibujar_Cuarto(x1, y1, x2, y2, grosor, "cuarto0")
    def delete_structure(self):
     if self.current_item:
        # Eliminar desde la estructura
        if self.current_item in self.estructura.cuartos:
            del self.estructura.cuartos[self.current_item]
        # Eliminar desde los elementos
        elif self.current_item in self.elemento.elementos:
            del self.elemento.elementos[self.current_item]
        # Eliminar desde los muebles
        elif self.current_item in self.mueble.muebles:
            del self.mueble.muebles[self.current_item]

        # Eliminar del canvas
        self.canvas.delete(self.current_item)
        self.label.config(text=f"Se eliminó: {self.current_item}")
        self.current_item = None
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


    def process_command(self, event):
        command = self.command_entry.get().strip().lower()
        parts = command.split()  # separa la cadena en palabras
        if len(parts) < 2:
            self.label.config(text="Comando no válido.")
            return

        action = parts[0]
        nombre = parts[1]

        if action == "crear" and len(parts) == 3:
            tipo = parts[1]
            nombre = parts[2]
            if tipo == "cuarto":
                self.estructura.cuarto_count += 1
                try:
                    ancho = int(self.entry_ancho.get())
                    largo = int(self.entry_largo.get())
                except ValueError:
                    self.label.config(text="Por favor ingresa valores numéricos válidos para ancho y largo.")
                    return
                x1, y1 = 50 + (self.estructura.cuarto_count - 1) * 200, 50
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
            elif tipo in ["cama", "sofa", "lampara", "mesa", "silla", "inodoro", "horno"]:
                cuarto_id = nombre
                if cuarto_id not in self.estructura.cuartos:
                    self.label.config(text="Cuarto no encontrado.")
                    return
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                pos_x, pos_y = x1 + 20, y1 + 20
                self.mueble.dibujar_mueble(tipo, pos_x, pos_y, cuarto_id)
        elif action == "eliminar" and len(parts) == 2:
            nombre = parts[1]
            if nombre in self.estructura.cuartos:
                del self.estructura.cuartos[nombre]
            elif nombre in self.elemento.elementos:
                del self.elemento.elementos[nombre]
            elif nombre in self.mueble.muebles:
                del self.mueble.muebles[nombre]
            self.canvas.delete(nombre)
            self.label.config(text=f"Se eliminó: {nombre}")
        elif action == "mover":
            self.label.config(text="Funcionalidad de mover no implementada.")
        else:
            self.label.config(text="Acción no reconocida. Usa 'crear', 'eliminar' o 'mover'.")

    def crear_mueble(self, tipo_mueble):
        if tipo_mueble == "cama":
            self.mueble.dibujar_cama(100, 100)
        elif tipo_mueble == "sofa":
            self.mueble.dibujar_sofa(100, 100)
        elif tipo_mueble == "lampara":
            self.mueble.dibujar_lampara(100, 100)
        elif tipo_mueble == "mesa":
            self.mueble.dibujar_mesa(100, 100)
        elif tipo_mueble == "silla":
            self.mueble.dibujar_silla(100, 100)
        elif tipo_mueble == "inodoro":
            self.mueble.dibujar_inodoro(100, 100)
        elif tipo_mueble == "horno":
            self.mueble.dibujar_horno(100, 100)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()

