import tkinter as tk
from tkinter import ttk

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

class Elemento:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ventana_count = 0
        self.puerta_count = 0

    def dibujar_Ventana(self, x1, y1, longitud, text, cuarto_id):
        self.canvas.create_rectangle(x1, y1, x1 + longitud, y1 + 10, fill="#EEEEEE", tags=(text, cuarto_id))
        self.canvas.create_line(x1, y1 + 4, x1 + longitud, y1 + 4, fill="black", tags=(text, cuarto_id))
        self.canvas.create_text(x1 + longitud // 2, y1 - 8, text=text, tags=(text, cuarto_id), fill='red')
    
    def dibujar_Ventana_Vertical(self, x1, y1, longitud, text, cuarto_id):
        self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + longitud, fill="#EEEEEE", tags=(text, cuarto_id))
        self.canvas.create_line(x1+4, y1, x1 + 4, y1 + longitud, fill="black", tags=(text, cuarto_id))
        y1 -= 5
        for i, char in enumerate(text):
            self.canvas.create_text(x1 + 15, y1 + i * 10, text=char, tags=(text, cuarto_id), fill='red')
    
    
    def dibujar_Puerta(self, x1, y1, longitud, text, cuarto_id):
        self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + longitud, fill="#A7E6FF", tags=(text, cuarto_id))
        self.canvas.create_line(x1 - longitud, y1 + longitud, x1, y1 + longitud, width="2", tags=(text, cuarto_id))
        self.canvas.create_arc(x1 - longitud, y1 + 5, x1 + 60, y1 + 110, start=90, extent=90, style=tk.PIESLICE, width=1, outline='black', tags=(text, cuarto_id))
        y1 -= 5
        for i, char in enumerate(text):
            self.canvas.create_text(x1 + 25, y1 + i * 10, text=char, tags=(text, cuarto_id), fill='red')
    
    def dibujar_Puerta_Vertical(self, x1, y1, longitud, text, cuarto_id):
        self.canvas.create_rectangle(x1, y1, x1+longitud, y1 + 10, fill="#A7E6FF", tags=(text, cuarto_id))
        self.canvas.create_line(x1 + longitud, y1 - longitud, x1+longitud, y1 , width="2", tags=(text, cuarto_id))
        self.canvas.create_arc(x1 +5, y1 - longitud, x1 + 110, y1 + 60, start=90, extent=90, style=tk.PIESLICE, width=1, outline='black', tags=(text, cuarto_id))
        y1 -= 5
        self.canvas.create_text(x1 + longitud // 2, y1 - 8, text=text, tags=(text, cuarto_id), fill='red')
        
    

class Mueble:
    def __init__(self, canvas):
        self.canvas = canvas
        self.mueble_ids = {"cama": 0, "sofa": 0, "lampara": 0, "mesa": 0, "silla": 0, "inodoro": 0, "horno": 0}
        self.muebles = {}

    def dibujar_mueble(self, tipo, x1, y1, cuarto_id):
        id = self.mueble_ids[tipo] = self.mueble_ids.get(tipo, 0) + 1
        etiqueta = f"{tipo} {id}"
        partes = []
        if tipo == "cama":
            partes = [self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 80, fill="white", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_rectangle(x1 + 10, y1, x1 + 40, y1 + 20, fill="lightgray", outline="black", tags=(etiqueta, cuarto_id))]
        elif tipo == "sofa":
            partes = [self.canvas.create_rectangle(x1, y1, x1 + 60, y1 + 20, fill="maroon", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_rectangle(x1, y1 + 80, x1 + 60, y1 + 100, fill="maroon", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_rectangle(x1, y1 + 20, x1 + 20, y1 + 80, fill="maroon", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_rectangle(x1 + 40, y1 + 20, x1 + 60, y1 + 80, fill="maroon", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_rectangle(x1 + 20, y1 + 20, x1 + 40, y1 + 80, fill="maroon", outline="black", tags=(etiqueta, cuarto_id))]
        elif tipo == "lampara":
            partes = [self.canvas.create_oval(x1, y1, x1 + 20, y1 + 20, fill="yellow", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_oval(x1 + 5, y1 + 5, x1 + 15, y1 + 15, fill="yellow", outline="black", tags=(etiqueta, cuarto_id))]
        elif tipo == "mesa":
            partes = [self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 30, fill="brown", outline="black", tags=(etiqueta, cuarto_id))]
        elif tipo == "silla":
            partes = [self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + 30, fill="purple", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_rectangle(x1, y1 + 20, x1 + 20, y1 + 30, fill="purple", outline="black", tags=(etiqueta, cuarto_id))]
        elif tipo == "inodoro":
            partes = [self.canvas.create_rectangle(x1, y1, x1 + 20, y1 + 30, fill="white", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_oval(x1 - 5, y1 - 10, x1 + 25, y1 + 10, fill="white", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_oval(x1 + 2, y1 - 7, x1 + 18, y1 + 7, fill="grey", outline="black", tags=(etiqueta, cuarto_id))]
        elif tipo == "horno":
            partes = [self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 50, fill="grey", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_oval(x1 + 10, y1 + 10, x1 + 20, y1 + 20, fill="black", outline="black", tags=(etiqueta, cuarto_id)),
                      self.canvas.create_oval(x1 + 30, y1 + 10, x1 + 40, y1 + 20, fill="black", outline="black", tags=(etiqueta, cuarto_id))]
        self.muebles[etiqueta] = partes
        return etiqueta

    
    def dibujar_cama(self, x1, y1):
        id = self.mueble_ids["cama"] = self.mueble_ids.get("cama", 0) + 1
        etiqueta = f"cama {id}"
        cuerpo = self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 80, fill="white", outline="black", tags=(etiqueta,))
        almohadas = self.canvas.create_rectangle(x1 + 10, y1, x1 + 40, y1 + 20, fill="lightgray", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [cuerpo, almohadas]
        return etiqueta

    def dibujar_sofa(self, x1, y1):
        id = self.mueble_ids["sofa"] = self.mueble_ids.get("sofa", 0) + 1
        etiqueta = f"sofa {id}"
        partes = [
            self.canvas.create_rectangle(x1, y1, x1 + 60, y1 + 20, fill="maroon", outline="black", tags=(etiqueta,)),  # Parte superior
            self.canvas.create_rectangle(x1, y1 + 80, x1 + 60, y1 + 100, fill="maroon", outline="black", tags=(etiqueta,)),  # Parte inferior
            self.canvas.create_rectangle(x1, y1 + 20, x1 + 20, y1 + 80, fill="maroon", outline="black", tags=(etiqueta,)),  # Parte izquierda
            self.canvas.create_rectangle(x1 + 40, y1 + 20, x1 + 60, y1 + 80, fill="maroon", outline="black", tags=(etiqueta,)),  # Parte derecha
            self.canvas.create_rectangle(x1 + 20, y1 + 20, x1 + 40, y1 + 80, fill="maroon", outline="black", tags=(etiqueta,))  # Parte central
        ]
        self.muebles[etiqueta] = partes
        return etiqueta

    def dibujar_lampara(self, x1, y1):
        id = self.mueble_ids["lampara"] = self.mueble_ids.get("lampara", 0) + 1
        etiqueta = f"lampara {id}"
        base = self.canvas.create_oval(x1, y1, x1 + 20, y1 + 20, fill="yellow", outline="black", tags=(etiqueta,))
        foco = self.canvas.create_oval(x1 + 5, y1 + 5, x1 + 15, y1 + 15, fill="yellow", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [base, foco]
        return etiqueta

    def dibujar_mesa(self, x1, y1):
        id = self.mueble_ids["mesa"] = self.mueble_ids.get("Mesa", 0) + 1
        etiqueta = f"mesa {id}"
        mesa = self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 30, fill="brown", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [mesa]
        return etiqueta

    def dibujar_silla(self, x1, y1):
        id = self.mueble_ids["silla"] = self.mueble_ids.get("silla", 0) + 1
        etiqueta = f"silla {id}"
        respaldo = self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + 30, fill="purple", outline="black", tags=(etiqueta,))
        asiento = self.canvas.create_rectangle(x1, y1 + 20, x1 + 20, y1 + 30, fill="purple", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [respaldo, asiento]
        return etiqueta

    def dibujar_inodoro(self, x1, y1):
        id = self.mueble_ids["inodoro"] = self.mueble_ids.get("inodoro", 0) + 1
        etiqueta = f"inodoro {id}"
        base = self.canvas.create_rectangle(x1, y1, x1 + 20, y1 + 30, fill="white", outline="black", tags=(etiqueta,))
        tapa = self.canvas.create_oval(x1 - 5, y1 - 10, x1 + 25, y1 + 10, fill="white", outline="black", tags=(etiqueta,))
        interior = self.canvas.create_oval(x1 + 2, y1 - 7, x1 + 18, y1 + 7, fill="grey", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [base, tapa, interior]
        return etiqueta

    def dibujar_horno(self, x1, y1):
        id = self.mueble_ids["horno"] = self.mueble_ids.get("horno", 0) + 1
        etiqueta = f"horno {id}"
        base = self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 50, fill="grey", outline="black", tags=(etiqueta,))
        quemador1 = self.canvas.create_oval(x1 + 10, y1 + 10, x1 + 20, y1 + 20, fill="black", outline="black", tags=(etiqueta,))
        quemador2 = self.canvas.create_oval(x1 + 30, y1 + 10, x1 + 40, y1 + 20, fill="black", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [base, quemador1, quemador2]
        return etiqueta
    

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Diseñador de cuartos")
        self.canvas = tk.Canvas(root, width=800, height=550)
        self.canvas.pack()

        self.estructura = Estructura(self.canvas)
        self.elemento = Elemento(self.canvas)
        self.mueble = Mueble(self.canvas)
        
        self.label = tk.Label(root, text="Selecciona una estructura")
        self.label.pack(pady=10)
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=10)

        opciones = ["cuarto", "ventana", "ventana vertical", "puerta", "puerta vertical"]
        self.seleccion = tk.StringVar()

        self.combo_box = ttk.Combobox(self.control_frame, textvariable=self.seleccion)
        self.combo_box['values'] = opciones
        self.combo_box.pack(side=tk.LEFT, padx=5)
        self.combo_box.bind("<<ComboboxSelected>>", self.handle_selection)

        mueble_combobox = ttk.Combobox(self.control_frame, values=["cama", "sofa","lampara","mesa","silla","inodoro","horno"])
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

    def handle_selection(self, event):
        self.selected_structure = self.combo_box.get()

    def on_canvas_click(self, event):
        x1, y1 = event.x, event.y
        if self.selected_structure == 'ventana':
            self.elemento.ventana_count += 1
            text = f"ventana{self.elemento.ventana_count}"
            self.elemento.dibujar_Ventana(x1, y1, 60, text, "")
        elif self.selected_structure == 'ventana vertical':
            self.elemento.ventana_count += 1
            text = f"ventana{self.elemento.ventana_count}"
            self.elemento.dibujar_Ventana_Vertical(x1, y1, 60, text, "")
        elif self.selected_structure == 'puerta':
            self.elemento.puerta_count += 1
            text = f"puerta{self.elemento.puerta_count}"
            self.elemento.dibujar_Puerta(x1, y1, 60, text, "")
        elif self.selected_structure == 'puerta vertical':
            self.elemento.puerta_count += 1
            text = f"puerta{self.elemento.puerta_count}"
            self.elemento.dibujar_Puerta_Vertical(x1, y1, 60, text, "")
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
        if self.current_item:
            self.canvas.delete(self.current_item)
            self.label.config(text=f"Se eliminó: {self.current_item}")
            self.current_item = None

    def process_command(self, event):
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
                    self.elemento.dibujar_Ventana(x1 + 20, y1 + 20, 60, text, cuarto_id)
                elif tipo == "puerta":
                    self.elemento.puerta_count += 1
                    text = f"puerta{self.elemento.puerta_count}"
                    self.elemento.dibujar_Puerta(x1 + 20, y1 + 50, 60, text, cuarto_id)
            elif tipo in ["cama", "sofa", "lampara", "mesa", "silla", "inodoro", "horno"]:
                self.crear_mueble_comando(tipo, nombre)
        elif action == "eliminar" and len(parts) == 3:
            nombre = parts[1]
            tipo = parts[2]
            et = f"{nombre} {tipo}"
            self.canvas.delete(et)
            self.label.config(text=f"Se eliminó: {et}")
        elif action == "mover":
            self.label.config(text="Funcionalidad de mover no implementada.")
        else:
            self.label.config(text="Acción no reconocida. Usa 'crear', 'eliminar' o 'mover'.")
    def crear_mueble_comando(self, tipo, cuarto_id):
        if cuarto_id not in self.estructura.cuartos:
            self.label.config(text="Cuarto no encontrado.")
            return
        x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
        pos_x, pos_y = x1 + 20, y1 + 20
        self.mueble.dibujar_mueble(tipo, pos_x, pos_y, cuarto_id)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()