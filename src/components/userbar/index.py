from tkinter import ttk
import tkinter as tk
import math

from .PointsCard import PointsCard
from .DistancesCard import DistancesCard
from .OptionsCard import OptionsCard


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