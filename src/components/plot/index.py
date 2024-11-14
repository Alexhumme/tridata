import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class PlotFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, style="Card.TFrame", padding=15, width=680, height=500)

        # Crear el marco para la gráfica
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=6)

        # Dibuja el triángulo inicial
        #self.draw_triangle()

    def draw_triangle(self, points):
        # Limpiar el gráfico anterior
        self.ax.clear()


        cpoints = {
            'A': (points[0][0], points[0][1]),
            'B': (points[1][0], points[1][1]),
            'C': (points[2][0], points[2][1])
        }

        # Dibujar el triángulo sin relleno 
        x, y = zip(*cpoints.values())
        self.ax.plot(x + (x[0],), y + (y[0],), marker='o', color='b')
        
        # Añadir etiquetas a cada punto
        for label, (x, y) in cpoints.items():
            self.ax.text(x, y, label, fontsize=12, ha='right', color='red')
        
        # Configurar los límites de los ejes para mejor visualización
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_aspect('equal', 'box')
        
        # Calcular y dibujar puntos medios
        midpoints = {
            'M_AB': ((cpoints['A'][0] + cpoints['B'][0]) / 2, (cpoints['A'][1] + cpoints['B'][1]) / 2),
            'M_BC': ((cpoints['B'][0] + cpoints['C'][0]) / 2, (cpoints['B'][1] + cpoints['C'][1]) / 2),
            'M_CA': ((cpoints['C'][0] + cpoints['A'][0]) / 2, (cpoints['C'][1] + cpoints['A'][1]) / 2)
        }
        
        for label, (x, y) in midpoints.items():
            self.ax.plot(x, y, marker='o', color='green')  # Dibuja el punto medio
            self.ax.text(x, y, label, fontsize=10, ha='left', color='green')  # Añade la etiqueta


        # Actualizar el canvas
        self.canvas.draw()

    pass
