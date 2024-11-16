
from tkinter import ttk

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