import tkinter as tk

def dibujar_pared(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="#6F4E37",outline="")

def dibujar_Cuarto(canvas, x1,y1,x2,y2,grosor):
    canvas.create_rectangle(x1, y1, x2, y2, fill="#F6FAB9",outline="")
    canvas.create_rectangle(x1, y1, x2, y1+grosor, fill="#6F4E37",outline="")
    canvas.create_rectangle(x1, y1, x1+grosor, y2, fill="#6F4E37",outline="")
    canvas.create_rectangle(x1, y2, x2, y2+grosor, fill="#6F4E37",outline="")
    canvas.create_rectangle(x2, y1, x2+grosor, y2+grosor, fill="#6F4E37",outline="")
    
def dibujar_Ventana(canvas, x1, y1, longitud):
    canvas.create_rectangle(x1,y1,x1+longitud,y1+16,fill="white")
    canvas.create_line(x1, y1+8, x1+longitud, y1+8, fill="black")
    
def dibujar_Puerta(canvas,x1,y1,longitud):  
    canvas.create_rectangle(x1,y1,x1+16,y1+longitud,fill="white")
    # canvas.create_rectangle(x1-longitud, y1, x1,y1+longitud,fill="white")
     
    canvas.create_line(x1-longitud,y1+longitud,x1,y1+longitud,width="5")
    canvas.create_line(x1-3,y1,x1-3,y1+longitud)
    # canvas.create_arc(x1-longitud, y1-longitud, x1,y1+longitud, start=-90, extent=-90, style=tk.ARC)

root = tk.Tk()
root.title("Diseñador de cuartos")
canvas = tk.Canvas(root, width=650, height=450)
canvas.pack()

# Coordenadas del rectángulo (x1, y1, x2, y2)
x1, y1 = 50, 50
x2, y2 = 250, 250
grosor = 16

dibujar_Cuarto(canvas, x1, y1, x2, y2,grosor)
x1, y1 = 125, 50
dibujar_Ventana(canvas,x1,y1,80)
x1, y1 = 250, 120
dibujar_Puerta(canvas,x1,y1,70)
root.mainloop()
