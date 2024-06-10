import tkinter as tk

class PlanosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Diseñador de Planos Arquitectónicos")

        self.canvas = tk.Canvas(master, width=800, height=600, bg="white")
        self.canvas.pack()

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

def main():
    root = tk.Tk()
    app = PlanosApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
