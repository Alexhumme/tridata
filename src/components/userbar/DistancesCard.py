from tkinter import ttk
import math 

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
