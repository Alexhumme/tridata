from tkinter import ttk
import tkinter as tk
import math

from .PointsCard import PointsCard
from .DistancesCard import DistancesCard


class OptionsCard(ttk.LabelFrame):
  def __init__(self, master = None):
    super().__init__(master, text="Opciones", padding=5)
    
    self.opts = [
        ttk.Button(self, style="", text="Dibujar Baricentro", width=35),
        ttk.Button(self, style="", text="Dibujar Mediatrices", width=35),
        ttk.Button(self, style="", text="Dibujar Circuncentro", width=35),
        ttk.Button(self, style="", text="Dibujar Ortocentro", width=35)
    ]

    for opt in self.opts: opt.pack(expand=True)


class Userbar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_controls()
        
    def create_controls(self) -> None:

      self.pointsCard: PointsCard = PointsCard(self)
      self.pointsCard.grid(column=0, padx=0, pady=0, row=0)
    
      self.distancesCard: DistancesCard = DistancesCard(self)
      self.distancesCard.grid(column=1, padx=5, row=0, sticky="nsew")

      self.optsCard: OptionsCard = OptionsCard(self)
      self.optsCard.grid(column=2, padx=0, row=0, sticky="nsew")

    pass