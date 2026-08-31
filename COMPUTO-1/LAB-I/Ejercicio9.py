## Ejercicio 9: Crear un sistema de coordenadas usando tuplas:
## Crear 5 tuplas que representen coordenadas (x, y) de diferentes puntos
## Almacenar las tuplas en una lista llamada puntos
## Calcular la distancia de cada punto al origen (0,0)
## Mostrar cuál punto está más cerca del origen

# Crear 5 tuplas que representen coordenadas (x, y)
punto1 = (1, 2)
punto2 = (3, 4)
punto3 = (5, 6)
punto4 = (7, 8)
punto5 = (9, 2)

# Almacenar las tuplas en una lista llamada puntos
puntos = [punto1, punto2, punto3, punto4, punto5]

# Mostrar todos los puntos
print("Puntos creados:")
print(punto1)
print(punto2)
print(punto3)
print(punto4)
print(punto5)
print()

# Calcular distancias al origen y mostrarlas
print("Distancias al origen (0,0):")

# Punto 1
distancia1 = ((punto1[0]**2) + (punto1[1]**2)) ** 0.5
print("Punto 1", punto1, "distancia:", round(distancia1, 2))

# Punto 2
distancia2 = ((punto2[0]**2) + (punto2[1]**2)) ** 0.5
print("Punto 2", punto2, "distancia:", round(distancia2, 2))

# Punto 3
distancia3 = ((punto3[0]**2) + (punto3[1]**2)) ** 0.5
print("Punto 3", punto3, "distancia:", round(distancia3, 2))

# Punto 4
distancia4 = ((punto4[0]**2) + (punto4[1]**2)) ** 0.5
print("Punto 4", punto4, "distancia:", round(distancia4, 2))

# Punto 5
distancia5 = ((punto5[0]**2) + (punto5[1]**2)) ** 0.5
print("Punto 5", punto5, "distancia:", round(distancia5, 2))
print()

# Guardar distancias en una lista
distancias = [distancia1, distancia2, distancia3, distancia4, distancia5]

# Encontrar la distancia minima
distancia_minima = min(distancias)

# Encontrar el indice de la distancia minima
indice = distancias.index(distancia_minima)

# Mostrar el punto mas cercano
print("El punto mas cercano al origen es:", puntos[indice])
print("Distancia:", round(distancia_minima, 2))