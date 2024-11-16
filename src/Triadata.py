import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
 
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import sv_ttk

from .components.userbar.index import *
from .components.plot.index import *
from .components.DialogBox import DialogBox


class Tridata(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title = "Tridata"
        self.geometry("700x800")
        
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
        self.userbar.pointsCard.sendButton.config(command=lambda : self.update_values(None))


        self.userbar.optsCard.opts[0].config(command=lambda : self.update_values(0))
        self.userbar.optsCard.opts[1].config(command=lambda : self.update_values(1))
        self.userbar.optsCard.opts[2].config(command=lambda : self.update_values(2))
        self.userbar.optsCard.opts[3].config(command=lambda : self.update_values(3))

        self.plot_frame:PlotFrame = PlotFrame(self.app_container)
        self.plot_frame.grid(row=1, sticky="nsew", padx=5, pady=0)

        self.dialogBox:DialogBox = DialogBox(self.app_container)
        self.dialogBox.grid(column=0, row=2, sticky="nsew", pady=5, padx=5)
        
    pass
    
    def get_points(self) -> list:
        points = [
            (
                float(self.userbar.pointsCard.axField.get()),
                float(self.userbar.pointsCard.ayField.get())
            ),
            (
                float(self.userbar.pointsCard.bxField.get()),
                float(self.userbar.pointsCard.byField.get())
            ),
            (
                float(self.userbar.pointsCard.cxField.get()),
                float(self.userbar.pointsCard.cyField.get())
            ),
            (
                float(self.userbar.pointsCard.axField.get()),
                float(self.userbar.pointsCard.ayField.get())
            )
        ]
        return points
    
    def update_values(self, opt):
        points = self.get_points()
        result = self.plot_frame.draw_triangle(points, opt)
        self.userbar.distancesCard.update_distances(points)

        if opt == None:
            text = f"Este es un triangulo con puntos A({points[0][0]:.2f},{points[0][1]:.2f}), B({points[1][0]:.2f},{points[1][1]:.2f}), C({points[2][0]:.2f},{points[2][1]:.2f})."
        if opt == 0:
            text = f"El baricentro de este triangulo esta en las coordenadas ({result[0]:.2f},{result[1]:.2f})."
        if opt == 1:
            text = f"Las mediatrices de este triangulo son : "
            for m,v in result.items():
                text += f"{m} ({v[0]:.2f}, {v[1]:.2f}) "
        if opt == 2:
            text = f"El circumcentro de este triangulo esta en las coordenadas ({result[0]:.2f},{result[1]:.2f})."
        if opt == 3:
            text = f"El ortocentro de este triangulo esta en las coordenadas ({result[0]:.2f},{result[1]:.2f})."

        self.dialogBox.textLabel.config(text=text)

