import tkinter as tk
import math

def dibujar_arco(canvas, x1, y1, x2, y2, angulo_inicio, angulo_final):
    canvas.create_arc(x1, y1, x2, y2, start=angulo_inicio, extent=angulo_final - angulo_inicio, style=tk.ARC)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Coordenadas del cuadrado y longitud del lado
x1, y1 = 100, 100
longitud = 200
# Dibujar el cuadrado
canvas.create_rectangle(x1, y1, x1+longitud, y1+longitud, fill="white")

# Calcular las coordenadas del punto medio en la diagonal
x_medio = x1 + longitud
y_medio = y1

# Calcular los ángulos de inicio y final para cubrir toda la circunferencia
angulo_inicio = math.degrees(math.atan((longitud/2) / (longitud/2)))
angulo_final = angulo_inicio + 180

# Coordenadas del cuadrado circunscrito y ángulos de inicio y final del arco
x1_arco, y1_arco = x1, y1 + longitud  # Esquina inferior izquierda del cuadrado
x2_arco, y2_arco = x1 + longitud, y1  # Esquina superior derecha del cuadrado

# Dibujar el arco
dibujar_arco(canvas, x1_arco, y1_arco, x2_arco, y2_arco, angulo_inicio, angulo_final)

root.mainloop()
