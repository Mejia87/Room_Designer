import tkinter as tk
from tkinter import ttk
import Estructura as EstructuraModule
import Elemento as ElementoModule
import Mueble as MuebleModule
from iarv.RV.RVHMM import reconocer_voz

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Diseñador de cuartos")
        self.root.config(bg='#A0937D')
        self.control_frame = tk.Frame(root,bg='#A0937D')
        self.control_frame.pack(side=tk.TOP, pady=10)

        self.label = tk.Label(root, text="Selecciona una estructura",bg='#A0937D',fg='white')
        self.label.config(font=('Helvetica', 15, 'bold'))
        self.label.pack(side=tk.TOP, pady=10)

        #agregar boton de microfono
        self.icon_microphone = tk.PhotoImage(file='microphone_off.png')
        self.icon_microphone_on = tk.PhotoImage(file='microphone_on.png')
        self.microphone_button = tk.Button(self.control_frame, image=self.icon_microphone, command=self.grabar, bd=0,bg='#A0937D')
        self.microphone_button.pack(side=tk.RIGHT, padx=5)
        self.grabando = False
        
        self.label_elemento = tk.Label(self.control_frame, text="Elemento:",bg='#A0937D',fg='white')
        self.label_elemento.config(font=('Helvetica', 15, 'bold'))
        self.label_elemento.pack(side=tk.LEFT, padx=5)
        
        opciones = ["cuarto", "ventana", "ventana vertical", "puerta", "puerta vertical"]
        self.seleccion = tk.StringVar()

        self.combo_box = ttk.Combobox(self.control_frame, textvariable=self.seleccion)
        self.combo_box['values'] = opciones
        self.combo_box.pack(side=tk.LEFT, padx=5)
        self.combo_box.bind("<<ComboboxSelected>>", self.handle_selection)
        
        self.label_ancho = tk.Label(self.control_frame, text="Ancho:",bg='#A0937D',fg='white')
        self.label_ancho.config(font=('Helvetica', 15, 'bold'))
        self.entry_ancho = tk.Entry(self.control_frame, width=6)
        

        self.label_largo = tk.Label(self.control_frame, text="Largo:",bg='#A0937D',fg='white')
        self.label_largo.config(font=('Helvetica', 15, 'bold'))
        self.entry_largo = tk.Entry(self.control_frame, width=6)
        
        self.label_mueble = tk.Label(self.control_frame, text="mueble:",bg='#A0937D',fg='white')
        self.label_mueble.config(font=('Helvetica', 15, 'bold'))
        self.label_mueble.pack(side=tk.LEFT, padx=5)
        mueble_combobox = ttk.Combobox(self.control_frame, values=["cama", "sofa","lampara","mesa","silla","inodoro","horno"])
        mueble_combobox.pack(side=tk.LEFT, padx=5)
        mueble_combobox.bind("<<ComboboxSelected>>", lambda event: self.crear_mueble(mueble_combobox.get()))
        
        

        delete_button = tk.Button(self.control_frame, text="Eliminar", command=self.delete_structure)
        delete_button.pack(side=tk.LEFT, padx=5)

        command_entry_label = tk.Label(self.control_frame, text="Introduce un comando:",bg='#A0937D',fg='white')
        command_entry_label.config(font=('Helvetica', 15, 'bold'))
        command_entry_label.pack(side=tk.LEFT, padx=5)

        self.command_entry = tk.Entry(self.control_frame, width=25)
        self.command_entry.pack(side=tk.LEFT, padx=5)
        self.command_entry.bind("<Return>", self.process_command)

        self.canvas = tk.Canvas(root, bg = '#F6E6CB')
        self.canvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.estructura = EstructuraModule.Estructura(self.canvas)
        self.elemento = ElementoModule.Elemento(self.canvas)
        self.mueble = MuebleModule.Mueble(self.canvas)
        self.mueble.estructura = self.estructura

        self.current_item = None
        self.start_x = 0
        self.start_y = 0

        self.canvas.bind("<Button-3>", self.on_canvas_click)
        self.canvas.bind("<ButtonPress-1>", self.start_move)
        self.canvas.bind("<B1-Motion>", self.move)

        x1, y1 = 300, 50
        x2, y2 = 460, 260
        grosor = 10
        self.estructura.dibujar_Cuarto(x1, y1, x2, y2, grosor, "cuarto 0")

    def grabar(self):
        self.grabando = not self.grabando
        
        if(self.grabando):
            self.microphone_button.config(image=self.icon_microphone_on) 
            self.label.config(text="...GRABANDO...")
            #llamar a reconocimiento de voz
            comandos = reconocer_voz()
            self.label.config(text=f"Se reconoció: {comandos}")
            for comando in comandos:
                self.process_voice_command(comando)
        else :
            self.microphone_button.config(image=self.icon_microphone)
            self.label.config(text="microfono apagado")
    
    def process_voice_command(self, comando):
        #procesar el comando
        parts = comando.split()
        if len(parts) < 2:
            self.label.config(text="Comando de voz no válido.")
            return

        action = parts[0]
        tipo = parts[1]

        if action == "crear" and len(parts) >= 2:
            if tipo in ["cuarto", "ventana", "ventana vertical", "puerta", "puerta vertical"]:
                self.selected_structure = tipo
                self.on_canvas_click(None)  # Simulamos un clic en el canvas
            elif tipo in ["cama", "sofa", "lampara", "mesa", "silla", "inodoro", "horno"]:
                self.crear_mueble_comando(tipo, "cuarto 0")  # Aquí debes ajustar el cuarto id según el comando de voz
        elif action == "eliminar" and len(parts) == 3:
            nombre = parts[1]
            tipo = parts[2]
            et = f"{nombre} {tipo}"
            self.canvas.delete(et)
            self.estructura.cuartos.pop(et)
            self.label.config(text=f"Se eliminó: {et}")
        elif action == "mover" and len(parts) == 4:
            self.mover_elemento(parts)
        else:
            self.label.config(text="Acción no reconocida. Usa 'crear', 'eliminar' o 'mover'.")

    def handle_selection(self, event):
        self.selected_structure = self.combo_box.get()
        
        
        if self.selected_structure == "cuarto":
            self.label_ancho.pack(side=tk.LEFT, padx=5)
            self.entry_ancho.pack(side=tk.LEFT, padx=5)
            self.label_largo.pack(side=tk.LEFT, padx=5)
            self.entry_largo.pack(side=tk.LEFT, padx=5)
        else:
            self.label_ancho.pack_forget()
            self.entry_ancho.pack_forget()
            self.label_largo.pack_forget()
            self.entry_largo.pack_forget()
            
    def on_canvas_click(self, event):
        x1, y1 = event.x, event.y
        if self.selected_structure == 'ventana':
            self.elemento.ventana_count += 1
            text = f"ventana {self.elemento.ventana_count}"
            self.elemento.dibujar_Ventana(x1, y1, 60, text, "")
        elif self.selected_structure == 'ventana vertical':
            self.elemento.ventana_count += 1
            text = f"ventana {self.elemento.ventana_count}"
            self.elemento.dibujar_Ventana_Vertical(x1, y1, 60, text, "")
        elif self.selected_structure == 'puerta':
            self.elemento.puerta_count += 1
            text = f"puerta {self.elemento.puerta_count}"
            self.elemento.dibujar_Puerta(x1, y1, 60, text, "")
        elif self.selected_structure == 'puerta vertical':
            self.elemento.puerta_count += 1
            text = f"puerta {self.elemento.puerta_count}"
            self.elemento.dibujar_Puerta_Vertical(x1, y1, 60, text, "")
        elif self.selected_structure == 'cuarto':
            self.estructura.cuarto_count += 1
            text = f"cuarto {self.estructura.cuarto_count}"
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
            self.estructura.actualizar_posicion_cuarto(self.current_item, dx, dy)
            self.start_x = event.x
            self.start_y = event.y
                


    def delete_structure(self):
        if self.current_item:
            self.canvas.delete(self.current_item)
            self.estructura.cuartos.pop(self.current_item)
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

        if action == "crear" and len(parts) >= 2:
            
            if tipo in ["cocina","dormitorio","baño"]:
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
                self.estructura.dibujar_Cuarto(x1, y1, x2, y2, grosor, f"{tipo} {self.estructura.cuarto_count}"  )
            elif tipo in ["ventana", "puerta"]:
                nombre = parts[2]
                cuarto_id = f"{nombre} {parts[3]}"
                if cuarto_id not in self.estructura.cuartos:
                    self.label.config(text="Cuarto no encontrado.")
                    return
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                if tipo == "ventana":
                    self.elemento.ventana_count += 1
                    text = f"ventana {self.elemento.ventana_count}"
                    self.elemento.dibujar_Ventana((x1+x2)//2-25, y1 , 60, text, cuarto_id)
                elif tipo == "puerta":
                    self.elemento.puerta_count += 1
                    text = f"puerta {self.elemento.puerta_count}"
                    
                    self.elemento.dibujar_Puerta(x2, y1+10, 60, text, cuarto_id)
            elif tipo in ["cama", "sofa", "lampara", "mesa", "silla", "inodoro", "horno"]:
                nombre = parts[2]
                self.crear_mueble_comando(tipo, f"{nombre} {parts[3]}")
        elif action == "eliminar" and len(parts) == 3:
            nombre = parts[1]
            tipo = parts[2]
            et = f"{nombre} {tipo}"
            self.canvas.delete(et)
            self.estructura.cuartos.pop(et)
            self.label.config(text=f"Se eliminó: {et}")
        elif action == "mover" and len(parts) == 4:
            self.mover_elemento(parts)
        else:
            self.label.config(text="Acción no reconocida. Usa 'crear', 'eliminar' o 'mover'.")
    
    def crear_mueble_comando(self, tipo, cuarto_id):
        # Verificar si el cuarto existe en la estructura
        if cuarto_id not in self.estructura.cuartos:
            self.label.config(text="Cuarto no encontrado.")
            return

        # Obtener las coordenadas del cuarto
        x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]

        # Calcular el punto medio del cuarto para colocar el mueble en el centro
        mx, my = (x2 - x1) // 2, (y2 - y1) // 2

        # Dibujar el mueble en el punto calculado
        etiqueta = self.mueble.dibujar_mueble(tipo, mx, my, cuarto_id)

        if etiqueta:
            self.label.config(text=f"{tipo.capitalize()} agregado con la etiqueta: {etiqueta}")
        else:
            self.label.config(text="Error al dibujar el mueble.")
            
    def mover_elemento(self,comandos):
        if(comandos[1] == 'ventana'):
            if(comandos[3] == 'arriba'):
                et = f"{comandos[1]} {comandos[2]}"
                self.canvas.delete(et)
                cuarto_id = self.elemento.elementos[et]
                self.label.config(text=f"id_cuarto obtenido: {et}")
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                self.elemento.elementos.pop(et)
                self.elemento.dibujar_Ventana((x1+x2)//2-25, y1 , 60, et, cuarto_id)
            elif(comandos[3] == 'abajo'):
                et = f"{comandos[1]} {comandos[2]}"
                self.canvas.delete(et)
                cuarto_id = self.elemento.elementos[et]
                self.label.config(text=f"id_cuarto obtenido: {et}")
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                self.elemento.elementos.pop(et)
                self.elemento.dibujar_Ventana((x1+x2)//2-25, y2 , 60, et, cuarto_id)
            elif(comandos[3] == 'derecha'):
                et = f"{comandos[1]} {comandos[2]}"
                self.canvas.delete(et)
                cuarto_id = self.elemento.elementos[et]
                self.label.config(text=f"id_cuarto obtenido: {cuarto_id}")
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                self.elemento.elementos.pop(et)
                self.elemento.dibujar_Ventana_Vertical(x2, (y1+y2)//2-25 , 60, et, cuarto_id) 
            elif(comandos[3] == 'izquierda' ):
                et = f"{comandos[1]} {comandos[2]}"
                self.canvas.delete(et)
                cuarto_id = self.elemento.elementos[et]
                self.label.config(text=f"id_cuarto obtenido: {cuarto_id}")
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                self.elemento.elementos.pop(et)
                self.elemento.dibujar_Ventana_Vertical(x1, (y1+y2)//2-25 , 60, et, cuarto_id)
        elif(comandos[1] == 'puerta'):
            if(comandos[3] == 'arriba'):
                et = f"{comandos[1]} {comandos[2]}"
                self.canvas.delete(et)
                cuarto_id = self.elemento.elementos[et]
                self.label.config(text=f"id_cuarto obtenido: {et}")
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                self.elemento.elementos.pop(et)
                self.elemento.dibujar_Puerta_Vertical(x1+10, y1 , 60, et, cuarto_id)
            elif(comandos[3] == 'abajo'):
                et = f"{comandos[1]} {comandos[2]}"
                self.canvas.delete(et)
                cuarto_id = self.elemento.elementos[et]
                self.label.config(text=f"id_cuarto obtenido: {et}")
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                self.elemento.elementos.pop(et)
                self.elemento.dibujar_Puerta_Vertical(x1+10, y2 , 60, et, cuarto_id)
            elif(comandos[3] == 'derecha'):
                et = f"{comandos[1]} {comandos[2]}"
                self.canvas.delete(et)
                cuarto_id = self.elemento.elementos[et]
                self.label.config(text=f"id_cuarto obtenido: {cuarto_id}")
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                self.elemento.elementos.pop(et)
                self.elemento.dibujar_Puerta(x2, y1+10 , 60, et, cuarto_id) 
            elif(comandos[3] == 'izquierda' ):
                et = f"{comandos[1]} {comandos[2]}"
                self.canvas.delete(et)
                cuarto_id = self.elemento.elementos[et]
                self.label.config(text=f"id_cuarto obtenido: {cuarto_id}")
                x1, y1, x2, y2 = self.estructura.cuartos[cuarto_id]
                self.elemento.elementos.pop(et)
                self.elemento.dibujar_Puerta(x1, y1+10 , 60, et, cuarto_id)  
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()