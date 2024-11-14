from tkinter import ttk
import math

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
      self.axField.insert(0,0)
      self.axField.grid(column=1, row=0)
      self.ayField = ttk.Spinbox(self, width=3)
      self.ayField.insert(0,0)
      self.ayField.grid(column=2, row=0)

      ttk.Label(self, text="B ").grid(column=0, row=1)
      self.bxField = ttk.Spinbox(self, width=3)
      self.bxField.insert(0,0)
      self.bxField.grid(column=1, row=1)
      self.byField = ttk.Spinbox(self, width=3)
      self.byField.insert(0,0)
      self.byField.grid(column=2, row=1)

      ttk.Label(self, text="C ").grid(column=0, row=2)
      self.cxField = ttk.Spinbox(self, width=3)
      self.cxField.insert(0,0)
      self.cxField.grid(column=1, row=2)
      self.cyField = ttk.Spinbox(self, width=3)
      self.cyField.insert(0,0)
      self.cyField.grid(column=2, row=2)

      ttk.Frame(self, height=5).grid(row=3, columnspan=5)

      self.sendButton: ttk.Button = ttk.Button(self, text="Crear triangulo", style="Accent.TButton")
      self.sendButton.grid(row=4, columnspan=5, sticky="nsew")
      
      pass

class DistancesCard(ttk.LabelFrame):
    def __init__(self, master):
      super().__init__(master, text="Distancias", padding=10)

      self.columnconfigure(0, weight=1)
      self.columnconfigure(1, weight=1)

      ttk.Label(self, text="AB").grid(row=0, column=0)
      self.abText = ttk.Entry(self, width=5)
      self.abText.insert(0,"0")
      self.abText.configure(state="disabled")
      self.abText.grid(row=0, column=1, padx=5,pady=5)

      ttk.Label(self, text="BC").grid(row=1, column=0)
      self.bcText = ttk.Entry(self, width=5)
      self.bcText.insert(0,"0")
      self.bcText.configure(state="disabled")
      self.bcText.grid(row=1, column=1, padx=5, pady=5)

      ttk.Label(self, text="CA").grid(row=2, column=0)
      self.caText = ttk.Entry(self, width=5)
      self.caText.insert(0,"0")
      self.caText.configure(state="disabled")
      self.caText.grid(row=2, column=1, padx=5, pady=5)

    def update_distances(self, points):
        self.abText.configure(state="normal")
        self.abText.delete(0, "end")
        self.abText.insert(0, str(self.calculate_distance(points[0], points[1])))
        self.abText.configure(state="disabled")

        self.bcText.configure(state="normal")
        self.bcText.delete(0, "end")
        self.bcText.insert(0, str(self.calculate_distance(points[1], points[2])))
        self.bcText.configure(state="disabled")

        self.caText.configure(state="normal")
        self.caText.delete(0, "end")
        self.caText.insert(0, str(self.calculate_distance(points[2], points[0])))
        self.caText.configure(state="disabled")

    def calculate_distance(self, point1, point2):
      
      x1, y1 = point1
      x2, y2 = point2
      distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

      return distance

    


class Userbar(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_controls()
        
    def create_controls(self) -> None:

      self.pointsCard: PointsCard = PointsCard(self)
      self.pointsCard.grid(column=0, padx=0, pady=0, row=0)
    
      self.distancesCard: DistancesCard = DistancesCard(self)
      self.distancesCard.grid(column=1, padx=5, row=0, sticky="nsew")

    pass