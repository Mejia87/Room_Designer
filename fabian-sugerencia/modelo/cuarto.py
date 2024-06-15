from .elemento import Elemento

class Cuarto:
    def __init__(self, nombre, ancho, alto):
        self.nombre = nombre
        self.ancho = ancho
        self.alto = alto
        self.elementos = []

    def agregar_elemento(self, tipo, x, y):
        elemento = Elemento(tipo, x, y)
        self.elementos.append(elemento)

    def eliminar_elemento(self, elemento):
        self.elementos.remove(elemento)

    def mover_elemento(self, elemento, nuevo_x, nuevo_y):
        elemento.x = nuevo_x
        elemento.y = nuevo_y
