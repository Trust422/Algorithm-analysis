import matplotlib.pyplot as plt

def orientation(p, q, r):
    """
    Esta función nos ayudará a determinar la orientación de tres puntos.
    Devolverá un valor positivo si es en sentido horario,
    negativo si es en sentido antihorario, y cero si son colineales.
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise

def convex_hull(points):
    n = len(points)
    if n < 3:
        return points
    
    hull = []
    
    # Encontrar el punto más a la izquierda (punto inicial)
    leftmost = min(points, key=lambda p: p[0])
    curr_point = leftmost
    while True:
        hull.append(curr_point)
        endpoint = (curr_point[0] + 1, curr_point[1])  # Inicializa el punto final al siguiente punto
        
        for i in range(n):
            if curr_point == points[i]:
                continue
            next_point = points[i]
            turn = orientation(curr_point, next_point, endpoint)
            if turn == 2 or (turn == 0 and distance(curr_point, next_point) > distance(curr_point, endpoint)):
                endpoint = next_point
        
        curr_point = endpoint
        if curr_point == leftmost:
            break
    
    return hull

def distance(p1, p2):
    return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

# Ejemplo de uso (Coordenadas de los puntos)
points = [(0.5, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_points = convex_hull(points)
print("Puntos del convex hull:", convex_points)

# Separar las coordenadas x e y de los puntos del convex hull
convex_x = [point[0] for point in convex_points]
convex_y = [point[1] for point in convex_points]

# Agregar el primer punto al final para cerrar el polígono en la visualización
convex_x.append(convex_x[0])
convex_y.append(convex_y[0])

# Crear el gráfico
plt.plot(convex_x, convex_y, marker='o')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Polígono del Convex Hull')
plt.grid()
plt.show()
