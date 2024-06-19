class Mueble:
    def __init__(self, canvas):
        self.canvas = canvas
        self.mueble_ids = {"cama": 0, "sofa": 0, "lampara": 0, "mesa": 0, "silla": 0, "inodoro": 0, "horno": 0}
        self.muebles = {}
        self.estructura = None

    def dibujar_mueble(self, tipo, mx, my, cuarto_id):
        id = self.mueble_ids[tipo] = self.mueble_ids.get(tipo, 0) + 1
        etiqueta = f"{tipo} {id}"
        coordenadas_cuarto = self.estructura.obtener_coordenadas_cuarto(cuarto_id)
        if coordenadas_cuarto:
            x1_cuarto, y1_cuarto, x2_cuarto, y2_cuarto = coordenadas_cuarto
            x1 = x1_cuarto + mx  
            y1 = y1_cuarto + my  


            partes = []
            if tipo == "cama":
                x1 -= 25
                y1 -= 90
                partes = [self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 80, fill="white", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_rectangle(x1 + 10, y1, x1 + 40, y1 + 20, fill="lightgray", outline="black", tags=(etiqueta, cuarto_id))]
            elif tipo == "sofa":
                x1 -= 30
                y1 -= 50
                partes = [self.canvas.create_rectangle(x1, y1, x1 + 60, y1 + 20, fill="maroon", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_rectangle(x1, y1 + 80, x1 + 60, y1 + 100, fill="maroon", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_rectangle(x1, y1 + 20, x1 + 20, y1 + 80, fill="maroon", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_rectangle(x1 + 40, y1 + 20, x1 + 60, y1 + 80, fill="maroon", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_rectangle(x1 + 20, y1 + 20, x1 + 40, y1 + 80, fill="maroon", outline="black", tags=(etiqueta, cuarto_id))]
            elif tipo == "lampara":
                x1 -= 15
                y1 += 45
                partes = [self.canvas.create_oval(x1, y1, x1 + 20, y1 + 20, fill="yellow", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_oval(x1 + 5, y1 + 5, x1 + 15, y1 + 15, fill="yellow", outline="black", tags=(etiqueta, cuarto_id))]
            elif tipo == "mesa":
                x1 -= 10
                y1 -= 15
                partes = [self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 30, fill="brown", outline="black", tags=(etiqueta, cuarto_id))]
            elif tipo == "silla":
                x1 -= 5
                y1 -= 10
                partes = [self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + 30, fill="purple", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_rectangle(x1, y1 + 20, x1 + 20, y1 + 30, fill="purple", outline="black", tags=(etiqueta, cuarto_id))]
            elif tipo == "inodoro":
                x1 -= 35
                y1 -= 70
                partes = [self.canvas.create_rectangle(x1, y1, x1 + 20, y1 + 30, fill="white", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_oval(x1 - 5, y1 - 10, x1 + 25, y1 + 10, fill="white", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_oval(x1 + 2, y1 - 7, x1 + 18, y1 + 7, fill="grey", outline="black", tags=(etiqueta, cuarto_id))]
            elif tipo == "horno":
                x1 -= 15
                y1 -= 10
                partes = [self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 50, fill="grey", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_oval(x1 + 10, y1 + 10, x1 + 20, y1 + 20, fill="black", outline="black", tags=(etiqueta, cuarto_id)),
                          self.canvas.create_oval(x1 + 30, y1 + 10, x1 + 40, y1 + 20, fill="black", outline="black", tags=(etiqueta, cuarto_id))]
            self.muebles[etiqueta] = partes
            return etiqueta
        else:
            return None    
    def dibujar_cama(self, x1, y1):
        id = self.mueble_ids["cama"] = self.mueble_ids.get("cama", 0) + 1
        etiqueta = f"cama {id}"
        cuerpo = self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 80, fill="white", outline="black", tags=(etiqueta,))
        almohadas = self.canvas.create_rectangle(x1 + 10, y1, x1 + 40, y1 + 20, fill="lightgray", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [cuerpo, almohadas]
        return etiqueta

    def dibujar_sofa(self, x1, y1):
        id = self.mueble_ids["sofa"] = self.mueble_ids.get("sofa", 0) + 1
        etiqueta = f"sofa {id}"
        partes = [
            self.canvas.create_rectangle(x1, y1, x1 + 60, y1 + 20, fill="maroon", outline="black", tags=(etiqueta,)),  # Parte superior
            self.canvas.create_rectangle(x1, y1 + 80, x1 + 60, y1 + 100, fill="maroon", outline="black", tags=(etiqueta,)),  # Parte inferior
            self.canvas.create_rectangle(x1, y1 + 20, x1 + 20, y1 + 80, fill="maroon", outline="black", tags=(etiqueta,)),  # Parte izquierda
            self.canvas.create_rectangle(x1 + 40, y1 + 20, x1 + 60, y1 + 80, fill="maroon", outline="black", tags=(etiqueta,)),  # Parte derecha
            self.canvas.create_rectangle(x1 + 20, y1 + 20, x1 + 40, y1 + 80, fill="maroon", outline="black", tags=(etiqueta,))  # Parte central
        ]
        self.muebles[etiqueta] = partes
        return etiqueta

    def dibujar_lampara(self, x1, y1):
        id = self.mueble_ids["lampara"] = self.mueble_ids.get("lampara", 0) + 1
        etiqueta = f"lampara {id}"
        base = self.canvas.create_oval(x1, y1, x1 + 20, y1 + 20, fill="yellow", outline="black", tags=(etiqueta,))
        foco = self.canvas.create_oval(x1 + 5, y1 + 5, x1 + 15, y1 + 15, fill="yellow", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [base, foco]
        return etiqueta

    def dibujar_mesa(self, x1, y1):
        id = self.mueble_ids["mesa"] = self.mueble_ids.get("Mesa", 0) + 1
        etiqueta = f"mesa {id}"
        mesa = self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 30, fill="brown", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [mesa]
        return etiqueta

    def dibujar_silla(self, x1, y1):
        id = self.mueble_ids["silla"] = self.mueble_ids.get("silla", 0) + 1
        etiqueta = f"silla {id}"
        respaldo = self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + 30, fill="purple", outline="black", tags=(etiqueta,))
        asiento = self.canvas.create_rectangle(x1, y1 + 20, x1 + 20, y1 + 30, fill="purple", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [respaldo, asiento]
        return etiqueta

    def dibujar_inodoro(self, x1, y1):
        id = self.mueble_ids["inodoro"] = self.mueble_ids.get("inodoro", 0) + 1
        etiqueta = f"inodoro {id}"
        base = self.canvas.create_rectangle(x1, y1, x1 + 20, y1 + 30, fill="white", outline="black", tags=(etiqueta,))
        tapa = self.canvas.create_oval(x1 - 5, y1 - 10, x1 + 25, y1 + 10, fill="white", outline="black", tags=(etiqueta,))
        interior = self.canvas.create_oval(x1 + 2, y1 - 7, x1 + 18, y1 + 7, fill="grey", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [base, tapa, interior]
        return etiqueta

    def dibujar_horno(self, x1, y1):
        id = self.mueble_ids["horno"] = self.mueble_ids.get("horno", 0) + 1
        etiqueta = f"horno {id}"
        base = self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 50, fill="grey", outline="black", tags=(etiqueta,))
        quemador1 = self.canvas.create_oval(x1 + 10, y1 + 10, x1 + 20, y1 + 20, fill="black", outline="black", tags=(etiqueta,))
        quemador2 = self.canvas.create_oval(x1 + 30, y1 + 10, x1 + 40, y1 + 20, fill="black", outline="black", tags=(etiqueta,))
        self.muebles[etiqueta] = [base, quemador1, quemador2]
        return etiqueta