import tkinter as tk
from tkinter import ttk


class DialogBox(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, style="Card.TFrame", height=100, padding=10)
        
        self.textLabel = ttk.Label(self, text="Digite las coordenadas de los puntos", anchor="center", justify="center")
        self.textLabel.pack(expand=True)