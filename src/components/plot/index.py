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
        self.ax.set_xlim(-10, 100)
        self.ax.set_ylim(-10, 100)
        self.ax.grid()

        self.ax.set_aspect('equal', 'box')

    def draw_sides(self, points):
         # Dibujar el triángulo sin relleno 
        x, y = zip(*points.values())
        self.ax.plot(x + (x[0],), y + (y[0],), marker='o', color='b')
        
        # Añadir etiquetas a cada punto
        for label, (x, y) in points.items():
            self.ax.text(x, y, label, fontsize=12, ha='right', color='red')
        
    def draw_midpoints(self, points):
        # Calcular y dibujar puntos medios
        midpoints = {
            'M_AB': ((points['A'][0] + points['B'][0]) / 2, (points['A'][1] + points['B'][1]) / 2),
            'M_BC': ((points['B'][0] + points['C'][0]) / 2, (points['B'][1] + points['C'][1]) / 2),
            'M_CA': ((points['C'][0] + points['A'][0]) / 2, (points['C'][1] + points['A'][1]) / 2)
        }
        
        for label, (x, y) in midpoints.items():
            self.ax.plot(x, y, marker='o', color='green')  # Dibuja el punto medio
            self.ax.text(x, y, label, fontsize=10, ha='left', color='green')  # Añade la etiqueta

    def carculate_baricenter(self, points):
        return (
            (points['A'][0] + points['B'][0] + points['C'][0]) / 3,
            (points['A'][1] + points['B'][1] + points['C'][1]) / 3
        )
    def draw_baricenter(self, points):

        lineas_baricentro = [
            (
                ((points['A'][0] + points['B'][0]) / 2,points['C'][0]),
                ((points['A'][1] + points['B'][1]) / 2, points['C'][1])
            ),(
                ((points['B'][0] + points['C'][0]) / 2,points['A'][0]),
                ((points['B'][1] + points['C'][1]) / 2, points['A'][1])
            ),(
                ((points['C'][0] + points['A'][0]) / 2,points['B'][0]),
                ((points['C'][1] + points['A'][1]) / 2, points['B'][1])
            ),
        ]

        # Calcular y dibujar el baricentro
        baricentro = self.carculate_baricenter(points)

        for line in lineas_baricentro:
            self.ax.plot(line[0], line[1],'--', linewidth=1,color='purple', )

        self.ax.plot(baricentro[0], baricentro[1], marker='o', color='purple')  # Dibujar el baricentro
        self.ax.text(baricentro[0], baricentro[1], 'G', fontsize=12, ha='left', color='purple')  # Etiqueta del baricentro

    def calculate_circumcenter(self, A, B, C):
        # Extraer coordenadas
        x1, y1 = A
        x2, y2 = B
        x3, y3 = C

        # Calcular el denominador
        D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        if D == 0:  # Evitar división por cero
            return (0, 0)

        # Calcular el numerador de x y y
        Ux = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2))
        Uy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1))

        # Circuncentro
        cx = Ux / D
        cy = Uy / D
        return (cx, cy)

    def draw_cincurcenter(self, points):
        circuncentro = self.calculate_circumcenter(points['A'], points['B'], points['C'])
        self.ax.plot(circuncentro[0], circuncentro[1], marker='o', color='orange')
        self.ax.text(circuncentro[0], circuncentro[1], 'Circuncentro', fontsize=12, ha='left', color='orange')

        pass

    def calculate_orthocenter(self, A, B, C):
        def perpendicular_line_through_point(p1, p2, p3):
            """Calcula la altura desde un punto p3 hacia la línea formada por p1 y p2."""
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            if x1 == x2:  # Línea vertical
                return (x1, y3), (x1, y1)
            elif y1 == y2:  # Línea horizontal
                return (x3, y1), (x1, y1)
            else:
                # Pendiente de la línea
                m = (y2 - y1) / (x2 - x1)
                m_perp = -1 / m  # Pendiente de la altura
                b_perp = y3 - m_perp * x3
                return (x3, y3), ((y1 - b_perp) / m_perp, y1)

        # Calcular las alturas desde cada vértice al lado opuesto
        altura_A = perpendicular_line_through_point(B, C, A)
        altura_B = perpendicular_line_through_point(A, C, B)
        altura_C = perpendicular_line_through_point(A, B, C)

        # Resolver intersección de dos de las alturas para encontrar el ortocentro
        def line_intersection(p1, p2, q1, q2):
            """Encuentra la intersección de dos líneas dadas por puntos (p1, p2) y (q1, q2)."""
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = q1
            x4, y4 = q2

            # Determinante
            det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if det == 0:
                return None  # Las líneas son paralelas
            # Punto de intersección
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
            py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det
            return px, py

        ortocentro = line_intersection(*altura_A, *altura_B)
        return ortocentro
    
    def draw_altitudes(self, A, B, C, orthocenter):
        def extend_line(p1, p2):
            """Extiende una línea entre dos puntos para cubrir el plano."""
            x1, y1 = p1
            x2, y2 = p2
            dx, dy = x2 - x1, y2 - y1
            return ((x1 - 10 * dx, y1 - 10 * dy), (x2 + 10 * dx, y2 + 10 * dy))

        # Alturas desde cada vértice al lado opuesto
        for vertex, side in [(A, (B, C)), (B, (A, C)), (C, (A, B))]:
            altura = self.calculate_orthocenter(*side, vertex)
            extended = extend_line(vertex, altura)
            self.ax.plot(*zip(*extended), linestyle='--', color='green')

    def draw_orthocenter(self, points):
        circuncentro = self.calculate_circumcenter(points['A'], points['B'], points['C'])
        baricentro = self.carculate_baricenter(points)

        # (mX1 - nX2)/(m - n), (mY1 - nY2)/(m - n)
        h =  [(3 * baricentro[0] - 2 * circuncentro[0]), 
            (3 * baricentro[1] - 2 * circuncentro[1])]
        
        # Print the x and y-coordinate
        h[0] = h[0] - 0.400

        # Calcular y dibujar el ortocentro
        ortocentro = self.calculate_orthocenter(points['A'], points['B'], points['C'])
        self.ax.plot(ortocentro[0], ortocentro[1], marker='o', color='red')
        self.ax.text(ortocentro[0], ortocentro[1], 'Ortocentro', fontsize=12, ha='left', color='red')
        # Dibujar las alturas
        self.draw_altitudes(points['A'], points['B'], points['C'], ortocentro)

    def draw_triangle(self, points, opt):
        # Limpiar el gráfico anterior
        self.ax.clear()

        cpoints = {
            'A': (points[0][0], points[0][1]),
            'B': (points[1][0], points[1][1]),
            'C': (points[2][0], points[2][1])
        }

        self.draw_sides(cpoints)
        if opt != None:
            if opt == 0: self.draw_baricenter(cpoints)
            if opt == 1: self.draw_midpoints(cpoints)
            if opt == 2: self.draw_cincurcenter(cpoints)
            if opt == 3: self.draw_orthocenter(cpoints)

        # Configurar los límites de los ejes para mejor visualización
        self.ax.set_xlim(-10, 100)
        self.ax.set_ylim(-10, 100)
        self.ax.grid()

        self.ax.set_aspect('equal', 'box')

        # Actualizar el canvas
        self.canvas.draw()

    pass
