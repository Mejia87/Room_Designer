from tkinter import messagebox
from vista.vista_cuartos import VistaCuartos
from modelo.cuarto import Cuarto

class Controlador:
    def __init__(self):
        self.vista = VistaCuartos(self)
        self.cuartos = []

    def agregar_cuarto(self):
        ancho, alto = self.vista.obtener_dimensiones_cuarto()
        if ancho is None or alto is None:
            return

        nombre = "Cuarto " + str(len(self.cuartos) + 1)
        nuevo_cuarto = Cuarto(nombre, ancho, alto)
        self.cuartos.append(nuevo_cuarto)
        self.vista.mostrar_cuarto(self.cuartos)

    def agregar_elemento(self):
        if not self.cuartos:
            messagebox.showerror("Error", "Primero agrega un cuarto")
            return

        tipo_elemento = self.vista.solicitar_tipo_elemento()
        if tipo_elemento is None:
            return

        id_cuarto = self.vista.solicitar_id_cuarto()
        if id_cuarto is None or id_cuarto < 1 or id_cuarto > len(self.cuartos):
            messagebox.showerror("Error", "ID de cuarto no válido")
            return

        cuarto = self.cuartos[id_cuarto - 1]
        if tipo_elemento == "Ventana":
            # Ventana en la pared superior del cuarto
            cuarto.agregar_elemento(tipo_elemento, (cuarto.ancho - 80) // 2, 0)
        elif tipo_elemento == "Puerta":
            # Puerta en la pared inferior del cuarto
            cuarto.agregar_elemento(tipo_elemento, (cuarto.ancho - 70) // 2, cuarto.alto - 16)
        self.vista.mostrar_cuarto(self.cuartos)

    def eliminar_cuarto(self):
        if not self.cuartos:
            messagebox.showerror("Error", "No hay cuartos para eliminar")
            return

        id_cuarto = self.vista.solicitar_id_cuarto_para_eliminar()
        if id_cuarto is None or id_cuarto < 1 or id_cuarto > len(self.cuartos):
            messagebox.showerror("Error", "ID de cuarto no válido")
            return

        del self.cuartos[id_cuarto - 1]
        self.vista.mostrar_cuarto(self.cuartos)

    def ejecutar(self):
        self.vista.mainloop()
