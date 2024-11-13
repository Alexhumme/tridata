import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
 
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sv_ttk

from components.userbar.index import *
from components.plot.index import *


class Tridata(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title = "Tridata"
        self.geometry("700x700")
        
        # layout principal
        self.app_container: tk.Frame = tk.Frame(self,height=620)
        self.app_container.pack(expand=True)

        self.app_container.rowconfigure(0)
        self.app_container.rowconfigure(1)
        
        self.create_controls()

        # Tema de estilo
        sv_ttk.set_theme("light")
    
    def create_controls(self):
        
        self.userbar:Userbar = Userbar(self.app_container)
        self.userbar.grid(row=0, sticky="nsew", padx=5, pady=5)
        self.userbar.pointsCard.sendButton.config(command=self.draw_triangle)

        self.plot_frame:ttk.Frame = PlotFrame(self.app_container)
        self.plot_frame.grid(row=1, sticky="nsew", padx=5, pady=0)
        
    pass
    
    def get_points(self) -> tuple:
        x = [
            self.userbar.pointsCard.axField.get(),
            self.userbar.pointsCard.bxField.get(),
            self.userbar.pointsCard.cxField.get(),
        ]
        y = [
            self.userbar.pointsCard.ayField.get(),
            self.userbar.pointsCard.byField.get(),
            self.userbar.pointsCard.cyField.get(),
        ]
        return (x,y)

    def draw_triangle(self):
        
        x,y = self.get_points()

        x = np.array(x)  # Coordenadas en el eje X
        y = np.array(y)  # Coordenadas en el eje Y
        
        # Crear una figura y un eje
        fig, ax = plt.subplots()

        # Dibujar el triángulo
        ax.fill(x, y, 'b')  # 'b' es el color azul, puedes cambiarlo
        ax.set_aspect('equal', 'box')  # Asegura que el triángulo no se deforme
        ax.set_xlim(-100, 300)  # Ajusta los límites en el eje X
        ax.set_ylim(-100, 300)  # Ajusta los límites en el eje Y

        # Incrustar la figura en Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)  # Crear el lienzo con la figura
        canvas.draw()  # Dibujar la figura en el lienzo
        canvas.get_tk_widget().pack()  # Empaquetar el lienzo en la ventana Tkinter```

def main():
    app:Tridata = Tridata()
    app.mainloop()

if __name__=="__main__": main()