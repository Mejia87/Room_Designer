import tkinter as tk
from tkinter import ttk

cuarto_count = 0
ventana_count = 0
puerta_count = 0

# Funciones para dibujar diferentes estructuras
def dibujar_pared(canvas, x1, y1, x2, y2, tag):
    return canvas.create_rectangle(x1, y1, x2, y2, fill="#6F4E37", outline="", tags=tag)

def dibujar_Dormitorio(canvas, x1, y1, x2, y2, grosor, tag, text):
    cuarto_id = canvas.create_rectangle(x1, y1, x2, y2, fill="#F6FAB9", outline="", tags=tag)
    canvas.create_rectangle(x1, y1, x2, y1 + grosor, fill="#6F4E37", outline="", tags=tag)
    canvas.create_rectangle(x1, y1, x1 + grosor, y2, fill="#6F4E37", outline="", tags=tag)
    canvas.create_rectangle(x1, y2, x2, y2 + grosor, fill="#6F4E37", outline="", tags=tag)
    canvas.create_rectangle(x2, y1, x2 + grosor, y2 + grosor, fill="#6F4E37", outline="", tags=tag)
    canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=text, tags=tag, fill='blue')
    return cuarto_id

def dibujar_Ventana(canvas, x1, y1, longitud, tag, text):
    ventana_id = canvas.create_rectangle(x1, y1, x1 + longitud, y1 + 16, fill="#EEEEEE", tags=tag)
    canvas.create_line(x1, y1 + 8, x1 + longitud, y1 + 8, fill="black", tags=tag)
    canvas.create_text(x1 + longitud // 2, y1 - 8, text=text, tags=tag, fill='red')
    return ventana_id

def dibujar_Puerta(canvas, x1, y1, longitud, tag, text):
    puerta_id = canvas.create_rectangle(x1, y1, x1 + 16, y1 + longitud, fill="#A7E6FF", tags=tag)
    canvas.create_line(x1 - longitud, y1 + longitud, x1, y1 + longitud, width="2", tags=tag)
    canvas.create_arc(x1 - longitud, y1 + 5, x1 + 65, y1 + 128, start=90, extent=90, style=tk.PIESLICE, width=1, outline='black', tags=tag)
    for i, char in enumerate(text):
        canvas.create_text(x1 + 25, y1 + i * 11, text=char, tags=tag, fill='red')  
    return puerta_id

# Función para manejar la selección del ComboBox
def handle_selection(event):
    global selected_structure
    selected_structure = combo_box.get()
    
    canvas.focus_set()  # Cambiar el enfoque al lienzo después de seleccionar una estructura

# Función para dibujar con el clic derecho del ratón en el lienzo
def on_canvas_click(event):
    global current_item, cuarto_count, ventana_count, puerta_count
    x1, y1 = event.x, event.y
    tag = f"struct_{event.x}_{event.y}"
    if selected_structure == 'ventana':
        ventana_count += 1
        text = f"ventana{ventana_count}"
        current_item = dibujar_Ventana(canvas, x1, y1, 80, tag, text)
    elif selected_structure == 'puerta':
        puerta_count += 1
        text = f"puerta{puerta_count}"
        current_item = dibujar_Puerta(canvas, x1, y1, 70, tag, text)
    elif selected_structure == 'cuarto':
        cuarto_count += 1
        text = f"cuarto{cuarto_count}"
        x2, y2 = x1 + 200, y1 + 200
        grosor = 16
        current_item = dibujar_Dormitorio(canvas, x1, y1, x2, y2, grosor, tag, text)

# Funciones para mover las estructuras
def start_move(event):
    global current_item, start_x, start_y
    items = canvas.find_closest(event.x, event.y)
    if items:
        current_item = items[0]
        tags = canvas.gettags(current_item)
        if tags:
            current_item = tags[0]
        start_x = event.x
        start_y = event.y
        label.config(text=f"Seleccionado: {current_item}")
        canvas.tag_raise(current_item)

def move(event):
    global start_x, start_y
    if current_item:
        dx = event.x - start_x
        dy = event.y - start_y
        canvas.move(current_item, dx, dy)
        start_x = event.x
        start_y = event.y

def stop_move(event):
    global current_item
    

# Función para eliminar la estructura seleccionada
def delete_structure():
    global current_item
    label.config(text=f"se elimino: {current_item}")
    if current_item:
        canvas.delete(current_item)
        label.config(text=f"se elimino: {current_item}")
        current_item = None

# Crear la ventana principal
root = tk.Tk()
root.title("Diseñador de cuartos")

# Crear el lienzo
canvas = tk.Canvas(root, width=650, height=450)
canvas.pack()

# Dibujar un cuarto inicial
x1, y1 = 50, 50
x2, y2 = 250, 300
grosor = 16
current_item = dibujar_Dormitorio(canvas, x1, y1, x2, y2, grosor, "initial_room", "cuarto0")

# Crear el componente de selección
label = tk.Label(root, text="Selecciona una estructura")
label.pack(pady=10)

opciones = ["cuarto", "ventana", "puerta"]
seleccion = tk.StringVar()

combo_box = ttk.Combobox(root, textvariable=seleccion)
combo_box['values'] = opciones
combo_box.pack(pady=10)

combo_box.bind("<<ComboboxSelected>>", handle_selection)

# Crear el botón de eliminar
delete_button = tk.Button(root, text="Eliminar", command=delete_structure)
delete_button.pack(pady=10)

# Inicializar la estructura seleccionada
selected_structure = None

# Inicializar variables para movimiento
current_item = None
start_x = 0
start_y = 0

# Vincular los eventos de clic y arrastre del ratón al lienzo
canvas.bind("<Button-3>", on_canvas_click)
canvas.bind("<ButtonPress-1>", start_move)
canvas.bind("<B1-Motion>", move)
canvas.bind("<ButtonRelease-1>", stop_move)

# Ejecutar la aplicación
root.mainloop()

