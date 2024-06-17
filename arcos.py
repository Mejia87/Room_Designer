import tkinter as tk

def draw_arcs_in_quadrants(canvas):
    # Primer cuadrante (superior derecho)
    canvas.create_arc(10, 200, 150, 100, start=0, extent=90, style=tk.PIESLICE, width=2, outline='black', fill='red')
    
    # Segundo cuadrante (superior izquierdo)
    canvas.create_arc(100, 100, 300, 300, start=90, extent=90, style=tk.PIESLICE, width=2, outline='black', fill='green')
    
    # # Tercer cuadrante (inferior izquierdo)
    # canvas.create_arc(100, 300, 300, 500, start=180, extent=90, style=tk.PIESLICE, width=2, outline='black', fill='blue')
    
    # # Cuarto cuadrante (inferior derecho)
    # canvas.create_arc(300, 300, 500, 500, start=270, extent=90, style=tk.PIESLICE, width=2, outline='black', fill='yellow')

# Crear la ventana principal
root = tk.Tk()
root.title("Canvas Arcs in Quadrants")

# Definir las dimensiones del canvas
canvas_width = 600
canvas_height = 600

# Crear el canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Dibujar los arcos en los cuatro cuadrantes
draw_arcs_in_quadrants(canvas)

# Iniciar el bucle principal de la ventana
root.mainloop()
