import tkinter as tk

def draw_full_circle_in_quadrants(canvas, x0, y0, x1, y1, width):
    # Primer cuadrante (superior derecho)
    #canvas.create_arc(x0, y0, x1, y1, start=0, extent=90, style=tk.PIESLICE, width=width, outline='black', fill='red')
    
    # # Segundo cuadrante (superior izquierdo)
     canvas.create_arc(x0, y0, x1, y1, start=90, extent=90, style=tk.PIESLICE, width=width, outline='black', fill='green')
    
    # # Tercer cuadrante (inferior izquierdo)
     #canvas.create_arc(x0, y0, x1, y1, start=180, extent=90, style=tk.PIESLICE, width=width, outline='black', fill='blue')
    
    # # Cuarto cuadrante (inferior derecho)
    #canvas.create_arc(x0, y0, x1, y1, start=270, extent=90, style=tk.PIESLICE, width=width, outline='black', fill='yellow')

# Crear la ventana principal
root = tk.Tk()
root.title("Canvas Demo - Full Circle in Quadrants")

# Definir las dimensiones del canvas
canvas_width = 400
canvas_height = 400

# Crear el canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Dibujar los arcos en los cuatro cuadrantes
draw_full_circle_in_quadrants(canvas, 100, 100, 300, 300, width=2)

# Iniciar el bucle principal de la ventana
root.mainloop()
