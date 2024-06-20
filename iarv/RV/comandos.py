
comandos = {"añadir": "objetosuperior",
            "eliminar": {"objetosuperior": "numero", "objetoinferior": "numero"},
            "crear": {"objetoinferior": {"objetosuperior":"numero"}},
            "mover": {"objetoinferior": {"numero": "direccion"}, "objetosuperior": {"numero": "direccion"}}
            }


class IteradorComando(object):
    def __init__(self):
        self.actual = comandos
        self.key_actual = ""

    def iterarComando(self, tipo):
        if isinstance(self.actual, dict):
            self.actual = self.actual[tipo]
            if isinstance(self.actual, dict):
                return list(self.actual.keys())
            else:
                return [self.actual]
        return None
