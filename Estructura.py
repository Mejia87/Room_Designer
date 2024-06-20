import tkinter as tk

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

    def actualizar_posicion_cuarto(self, text, dx, dy):
        if text in self.cuartos:
            x1, y1, x2, y2 = self.cuartos[text]
            self.cuartos[text] = (x1 + dx, y1 + dy, x2 + dx, y2 + dy)
    def obtener_coordenadas_cuarto(self, cuarto_id):
        return self.cuartos.get(cuarto_id, None)