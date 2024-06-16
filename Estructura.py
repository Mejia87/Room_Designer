import tkinter as tk
from tkinter import ttk

def dibujar_pared(canvas, x1, y1, x2, y2):
    canvas.create_rectangle(x1, y1, x2, y2, fill="#6F4E37",outline="")

def dibujar_Cuarto(canvas, x1,y1,x2,y2,grosor):
    canvas.create_rectangle(x1, y1, x2, y2, fill="#F6FAB9",outline="")
    canvas.create_rectangle(x1, y1, x2, y1+grosor, fill="#6F4E37",outline="")
    canvas.create_rectangle(x1, y1, x1+grosor, y2, fill="#6F4E37",outline="")
    canvas.create_rectangle(x1, y2, x2, y2+grosor, fill="#6F4E37",outline="")
    canvas.create_rectangle(x2, y1, x2+grosor, y2+grosor, fill="#6F4E37",outline="")
    
def dibujar_Ventana(canvas, x1, y1, longitud):
    canvas.create_rectangle(x1,y1,x1+longitud,y1+16,fill="#EEEEEE")
    canvas.create_line(x1, y1+8, x1+longitud, y1+8, fill="black")
    
def dibujar_Puerta(canvas,x1,y1,longitud):  
    canvas.create_rectangle(x1,y1,x1+16,y1+longitud,fill="#A7E6FF")
    
     
    canvas.create_line(x1-longitud,y1+longitud,x1,y1+longitud,width="2")
    
    canvas.create_arc(x1-longitud, y1+5, x1+65, y1+128, start=90, extent=90, style=tk.PIESLICE, width=1, outline='black')
#funcion para manejar la seleccion del combo-box
def handle_selection(event):
    global estructura
    estructura = combo_box.get() 
    label.config(text=f"Seleccionado: {estructura}")
    
#funcion para manejar el mouse
def on_canvas_click(event):
    x1, y1 = event.x, event.y
    if(estructura == 'ventana'):
        dibujar_Ventana(canvas,x1,y1,80)
    elif(estructura == 'puerta'): 
        dibujar_Puerta(canvas,x1,y1,70)
    elif(estructura == 'cuarto'):
        x2, y2 = x1+200, y1+200
        grosor=16
        dibujar_Cuarto(canvas,x1,y1,x2,y2,grosor)
#crea la ventana principal     
root = tk.Tk()
root.title("Diseñador de cuartos")
#crea el lienzo
canvas = tk.Canvas(root, width=650, height=450)
canvas.pack()

#dibujar cuarto
x1, y1 = 50, 50
x2, y2 = 250, 250
grosor = 16
dibujar_Cuarto(canvas, x1, y1, x2, y2,grosor)
    
#creando componente de seleccion
label = tk.Label(root, text = "selecciona una estructura")
label.pack(pady=10)

opciones = ["cuarto", "ventana","puerta"]

seleccion = tk.StringVar()

combo_box = ttk.Combobox(root, textvariable = seleccion)
combo_box['values'] = opciones
combo_box.pack(pady=10)

combo_box.bind("<<ComboboxSelected>>",handle_selection)

#inicializa la estructura seleccionada
estructura = None

#Vincula el evento del clic del raton al lienzo
canvas.bind("<Button-1>", on_canvas_click)

#ejecuta la aplicacion
root.mainloop()



