from tkinter import ttk

class PointsCard(ttk.LabelFrame):
    def __init__(self, master):
      super().__init__(master, width=100, height=100, text=" Puntos ", padding=10)
      
      self.columnconfigure(0, weight=1)
      self.columnconfigure(1, weight=1)
      self.columnconfigure(2, weight=1)
      self.columnconfigure(3, weight=1)
      self.columnconfigure(4, weight=1)

      self.create_controls()

    def create_controls(self):
      
      ttk.Label(self, text="A ").grid(column=0, row=0)
      self.axField = ttk.Spinbox(self, width=3)
      self.axField.insert(0,10)
      self.axField.grid(column=1, row=0)
      self.ayField = ttk.Spinbox(self, width=3)
      self.ayField.insert(0,20)
      self.ayField.grid(column=2, row=0)

      ttk.Label(self, text="B ").grid(column=0, row=1)
      self.bxField = ttk.Spinbox(self, width=3)
      self.bxField.insert(0,60)
      self.bxField.grid(column=1, row=1)
      self.byField = ttk.Spinbox(self, width=3)
      self.byField.insert(0,80)
      self.byField.grid(column=2, row=1)

      ttk.Label(self, text="C ").grid(column=0, row=2)
      self.cxField = ttk.Spinbox(self, width=3)
      self.cxField.insert(0,30)
      self.cxField.grid(column=1, row=2)
      self.cyField = ttk.Spinbox(self, width=3)
      self.cyField.insert(0,0)
      self.cyField.grid(column=2, row=2)

      ttk.Frame(self, height=5).grid(row=3, columnspan=5)

      self.sendButton: ttk.Button = ttk.Button(self, text="Crear triangulo", style="Accent.TButton")
      self.sendButton.grid(row=4, columnspan=5, sticky="nsew")
      
      pass