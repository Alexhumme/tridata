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
        self.userbar.pointsCard.sendButton.config(command=lambda : self.update_values(None))


        self.userbar.optsCard.opts[0].config(command=lambda : self.update_values(0))
        self.userbar.optsCard.opts[1].config(command=lambda : self.update_values(1))
        self.userbar.optsCard.opts[2].config(command=lambda : self.update_values(2))
        self.userbar.optsCard.opts[3].config(command=lambda : self.update_values(3))


        self.plot_frame:PlotFrame = PlotFrame(self.app_container)
        self.plot_frame.grid(row=1, sticky="nsew", padx=5, pady=0)
        
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
        self.plot_frame.draw_triangle(points, opt)
        self.userbar.distancesCard.update_distances(points)

def main():
    app:Tridata = Tridata()
    app.mainloop()

if __name__=="__main__": main()