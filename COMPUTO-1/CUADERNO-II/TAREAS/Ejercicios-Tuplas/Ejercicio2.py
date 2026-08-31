## Ejercicio 2: Ubicación de dispositivos
## Una empresa de tecnología registra la ubicación de
## sus dispositivos mediante coordenadas

## Cada dispositivo debe almacenar:
## Código del dispositivo
## Nombre
## Ubicación (X, Y)
## Estado

# 1. Creación de las tres tuplas con los datos de los dispositivos
dispositivo1 = ("PC001", "Servidor principal", (150, 300), "Activo")
dispositivo2 = ("LAP02", "Laptop Desarrollo", (450, 600), "Inactivo")
dispositivo3 = ("TEL03", "Teléfono Soporte", (100, 200), "Activo")

# 2. Mostrar la información del dispositivo 1 como lo pide el ejemplo
print(f"Código: {dispositivo1[0]}")
print(f"Nombre: {dispositivo1[1]}")
print(f"Coordenada X: {dispositivo1[2][0]}")  # Accede al primer elemento de la coordenada
print(f"Coordenada Y: {dispositivo1[2][1]}")  # Accede al segundo elemento de la coordenada
print(f"Estado: {dispositivo1[3]}")

# Creación de la tupla contenedora
dispositivos = (dispositivo1, dispositivo2, dispositivo3)

# Mostrar el contenido completo de la tupla contenedora
print(dispositivos)

# Mostrar únicamente la coordenada Y del segundo dispositivo
coordenada_y_segundo = dispositivos[1][2][1]
print("La coordenada Y del segundo dispositivo es: ", coordenada_y_segundo)
