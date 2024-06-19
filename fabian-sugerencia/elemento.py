import tkinter as tk

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
        
