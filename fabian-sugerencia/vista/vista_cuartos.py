import tkinter as tk
from tkinter import simpledialog, messagebox

class VistaCuartos(tk.Tk):
    def __init__(self, controlador):
        super().__init__()
        self.controlador = controlador
        self.title("Diseñador de Planos Arquitectónicos")
        self.geometry("800x600")

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Crear labels y entries para el ancho y alto
        self.label_ancho = tk.Label(self, text="Ancho del cuarto (px):")
        self.label_ancho.pack()
        self.entry_ancho = tk.Entry(self)
        self.entry_ancho.pack()

        self.label_alto = tk.Label(self, text="Alto del cuarto (px):")
        self.label_alto.pack()
        self.entry_alto = tk.Entry(self)
        self.entry_alto.pack()

        # Botones para agregar y eliminar cuartos y elementos
        self.boton_agregar_cuarto = tk.Button(self, text="Agregar Cuarto", command=self.controlador.agregar_cuarto)
        self.boton_agregar_cuarto.pack()

        self.boton_agregar_elemento = tk.Button(self, text="Agregar Elemento", command=self.controlador.agregar_elemento)
        self.boton_agregar_elemento.pack()
        
        self.boton_eliminar_cuarto = tk.Button(self, text="Eliminar Cuarto", command=self.controlador.eliminar_cuarto)
        self.boton_eliminar_cuarto.pack()

    def obtener_dimensiones_cuarto(self):
        try:
            ancho = int(self.entry_ancho.get())
            alto = int(self.entry_alto.get())
            if ancho <= 0 or alto <= 0:
                raise ValueError
            return ancho, alto
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos positivos para las dimensiones.")
            return None, None

    def dibujar_pared(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#6F4E37", outline="")

    def dibujar_cuarto(self, x1, y1, x2, y2, grosor):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#F6FAB9", outline="")
        self.canvas.create_rectangle(x1, y1, x2, y1 + grosor, fill="#6F4E37", outline="")
        self.canvas.create_rectangle(x1, y1, x1 + grosor, y2, fill="#6F4E37", outline="")
        self.canvas.create_rectangle(x1, y2, x2, y2 + grosor, fill="#6F4E37", outline="")
        self.canvas.create_rectangle(x2, y1, x2 + grosor, y2 + grosor, fill="#6F4E37", outline="")

    def dibujar_ventana(self, x1, y1, longitud):
        self.canvas.create_rectangle(x1, y1, x1 + longitud, y1 + 16, fill="white")
        self.canvas.create_line(x1, y1 + 8, x1 + longitud, y1 + 8, fill="black")

    def dibujar_puerta(self, x1, y1, longitud):
        # Dibuja la puerta como un rectángulo
        self.canvas.create_rectangle(x1, y1, x1 + 16, y1 + longitud, fill="white", outline="black")
        # arco de la puerta como aleta de tiburón
        self.canvas.create_arc(x1 - longitud, y1, x1 + longitud, y1 + 2 * longitud, start=0, extent=90, style=tk.ARC, outline="black")

    def mostrar_cuarto(self, cuartos):
        self.canvas.delete("all")
        x_offset = 50
        y_offset = 50
        separation = 30

        for i, cuarto in enumerate(cuartos):
            x1, y1 = x_offset, y_offset
            x2, y2 = x1 + cuarto.ancho, y1 + cuarto.alto
            grosor = 16

            self.dibujar_cuarto(x1, y1, x2, y2, grosor)

            id_text = f"Cuarto {i + 1}"
            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=id_text, font=("Arial", 16), fill="black")

            for elemento in cuarto.elementos:
                if elemento.tipo == "Ventana":
                    self.dibujar_ventana(x1 + elemento.x, y1 + elemento.y, 80)
                    self.canvas.create_text(x1 + elemento.x + 40, y1 + elemento.y - 10, text="Ventana", font=("Arial", 10), fill="blue")
                elif elemento.tipo == "Puerta":
                    self.dibujar_puerta(x1 + elemento.x, y1 + elemento.y, 70)
                    self.canvas.create_text(x1 + elemento.x + 10, y1 + elemento.y + 35, text="Puerta", font=("Arial", 10), fill="green")

            x_offset += cuarto.ancho + separation
            if x_offset + cuarto.ancho > self.canvas.winfo_width():
                x_offset = 50
                y_offset += cuarto.alto + separation

    def solicitar_id_cuarto(self):
        return simpledialog.askinteger("ID del Cuarto", "Ingrese el ID del cuarto al que desea agregar el elemento:")

    def solicitar_tipo_elemento(self):
        tipos = ["Ventana", "Puerta"]
        return simpledialog.askstring("Tipo de Elemento", "Ingrese el tipo de elemento a agregar (Ventana/Puerta):", initialvalue=tipos[0])

    def solicitar_id_cuarto_para_eliminar(self):
        return simpledialog.askinteger("Eliminar Cuarto", "Ingrese el ID del cuarto que desea eliminar:")
