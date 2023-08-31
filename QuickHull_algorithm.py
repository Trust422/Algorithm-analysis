import matplotlib.pyplot as plt
import random
import time

def orientation(p, q, r):
    """
    Esta función nos ayudará a determinar la orientación de tres puntos.
    Devuelve un valor positivo si es en sentido horario,
    negativo si es en sentido antihorario, y cero si son colineales.
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def distance(p, q, r):
    """
    Función para calcular la distancia entre el punto r y la línea que pasa por p y q.
    """
    return abs((q[1] - p[1]) * r[0] - (q[0] - p[0]) * r[1] + q[0] * p[1] - q[1] * p[0]) / ((q[1] - p[1])**2 + (q[0] - p[0])**2)**0.5

def quickhull(points):
    n = len(points)
    if n < 3:
        return []

    # Encontrar los puntos extremos izquierdo y derecho
    leftmost = min(points, key=lambda x: x[0])
    rightmost = max(points, key=lambda x: x[0])

    hull = []
    hull.append(leftmost)
    hull.append(rightmost)

    def build_hull(p, q, points):
        if not points:
            return
        farthest = max(points, key=lambda x: distance(p, q, x))
        hull.insert(hull.index(q), farthest)
        points.remove(farthest)
        s1, s2 = [], []
        for point in points:
            if orientation(p, farthest, point) == 1:
                s1.append(point)
            elif orientation(farthest, q, point) == 1:
                s2.append(point)
        build_hull(p, farthest, s1)
        build_hull(farthest, q, s2)

    s1, s2 = [], []
    for point in points:
        if orientation(leftmost, rightmost, point) == 1:
            s1.append(point)
        elif orientation(rightmost, leftmost, point) == 1:
            s2.append(point)

    build_hull(leftmost, rightmost, s1)
    build_hull(rightmost, leftmost, s2)

    return hull

# Generar puntos aleatorios
num_points = 20  # Número de puntos aleatorios a generar
seed = int(time.time())  # Generar una semilla basada en el tiempo actual
random.seed(seed)  # Fijar la semilla para generar puntos aleatorios únicos en cada ejecución
points = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(num_points)]

# Encontrar la envoltura convexa usando QuickHull
hull = quickhull(points)

# Separar coordenadas x e y de todos los puntos para graficar
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Graficar todos los puntos
plt.scatter(x_coords, y_coords, color='blue', label='Puntos')

# Separar coordenadas x e y de la envoltura convexa para graficar
hull_x_coords = [point[0] for point in hull]
hull_y_coords = [point[1] for point in hull]

# Cerrar el polígono trazando una línea desde el último punto al primero
hull_x_coords.append(hull_x_coords[0])
hull_y_coords.append(hull_y_coords[0])

# Graficar el polígono
plt.plot(hull_x_coords, hull_y_coords, marker='o', color='red', label='Envoltura Convexa')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Envoltura Convexa usando QuickHull')
plt.grid()
plt.legend()
plt.show()