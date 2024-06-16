from tkinter import messagebox
from vista.vista_cuartos import VistaCuartos
from modelo.cuarto import Cuarto
from modelo.elemento import Elemento

class Controlador:
    def __init__(self):
        self.vista = VistaCuartos(self)
        self.cuartos = []

    def agregar_cuarto(self):
        ancho, alto = self.vista.obtener_dimensiones_cuarto()
        if ancho is None or alto is None:
            return

        nombre = "Cuarto " + str(len(self.cuartos) + 1)
        cuarto = Cuarto(nombre, ancho, alto)
        self.cuartos.append(cuarto)
        self.vista.mostrar_cuarto(self.cuartos)

    def agregar_elemento(self):
        id_cuarto = self.vista.solicitar_id_cuarto()
        tipo_elemento = self.vista.solicitar_tipo_elemento()

        if id_cuarto is None or tipo_elemento not in ["Ventana", "Puerta"]:
            messagebox.showerror("Error", "ID de cuarto o tipo de elemento no válido.")
            return

        cuarto = self.obtener_cuarto_por_id(id_cuarto)
        if cuarto is None:
            messagebox.showerror("Error", "Cuarto no encontrado.")
            return

        x = self.vista.solicitar_posicion("X")
        y = 0  # elementos en la pared superior

        if x is None:
            messagebox.showerror("Error", "Posiciones no válidas.")
            return

        cuarto.agregar_elemento(tipo_elemento, x, y)
        self.vista.mostrar_cuarto(self.cuartos)

    def eliminar_cuarto(self):
        id_cuarto = self.vista.solicitar_id_cuarto_para_eliminar()

        if id_cuarto is None:
            messagebox.showerror("Error", "ID de cuarto no válido.")
            return

        cuarto = self.obtener_cuarto_por_id(id_cuarto)
        if cuarto is None:
            messagebox.showerror("Error", "Cuarto no encontrado.")
            return

        self.cuartos.remove(cuarto)
        self.vista.mostrar_cuarto(self.cuartos)

    def obtener_cuarto_por_id(self, id_cuarto):
        if id_cuarto < 1 or id_cuarto > len(self.cuartos):
            return None
        return self.cuartos[id_cuarto - 1]

    def procesar_click(self, x, y):
        id_cuarto = self.vista.solicitar_id_cuarto()
        if id_cuarto is None:
            return

        cuarto = self.obtener_cuarto_por_id(id_cuarto)
        if cuarto is None:
            messagebox.showerror("Error", "Cuarto no encontrado.")
            return

        tipo_mueble = self.vista.solicitar_tipo_mueble()
        if tipo_mueble not in ["Cama", "Sofá"]:
            messagebox.showerror("Error", "Tipo de mueble no válido.")
            return

        if tipo_mueble == "Cama":
            self.vista.dibujar_cama(x, y)
        elif tipo_mueble == "Sofá":
            self.vista.dibujar_sofa(x, y)

    def ejecutar(self):
        self.vista.mainloop()
