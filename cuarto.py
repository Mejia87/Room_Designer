import tkinter as tk

class Cuarto:
    def __init__(self, x1, y1, x2, y2, color="lightblue"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def dibujar(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.color)

class PlanosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Diseñador de Planos Arquitectónicos")

        self.canvas = tk.Canvas(master, width=800, height=600, bg="white")
        self.canvas.pack()

        self.cuartos = []

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)

        self.start_x = None
        self.start_y = None
        self.rect = None

    def on_click(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

    def on_drag(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.delete(self.rect)

        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, x, y, outline="black")

    def crear_cuarto(self, event):
        x1 = min(self.start_x, event.x)
        y1 = min(self.start_y, event.y)
        x2 = max(self.start_x, event.x)
        y2 = max(self.start_y, event.y)

        cuarto = Cuarto(x1, y1, x2, y2)
        cuarto.dibujar(self.canvas)
        self.cuartos.append(cuarto)

def main():
    root = tk.Tk()
    app = PlanosApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
