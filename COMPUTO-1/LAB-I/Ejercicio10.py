## Ejercicio 10: Trabajar con conjuntos de materias de diferentes carreras:
## Crear 3 conjuntos: 
## Ingeniería de Software
## Ingeniería en Sistemas
## Ingeniería en Ciencia de Datos
## Cada conjunto debe tener al menos 6 materias
## Encontrar materias comunes entre todas las carreras
## Encontrar materias exclusivas de cada carrera
## Crear la unión de todas las materias
## Mostrar cuántas materias únicas hay en total

# Ejercicio 10: Conjuntos de materias de diferentes carreras

# Crear 3 conjuntos con materias de cada carrera
ingenieria_software = {"Programacion", "Estructura de Datos", "Base de Datos", 
                       "POO", "Redes", "Sistemas Operativos"}

ingenieria_sistemas = {"Programacion", "Estructura de Datos", "Base de Datos", 
                       "Redes", "Sistemas Operativos", "Arquitectura de Computadoras"}

ciencia_datos = {"Programacion", "Base de Datos", "Estadistica", 
                 "Machine Learning", "Visualizacion de Datos", "Big Data"}
print("MATERIAS POR CARRERA")

print("Ingenieria de Software:", ingenieria_software)
print("Ingenieria en Sistemas:", ingenieria_sistemas)
print("Ingenieria en Ciencia de Datos:", ciencia_datos)

# Encontrar materias comunes entre todas las carreras
# Usamos la interseccion de los 3 conjuntos
comunes = ingenieria_software & ingenieria_sistemas & ciencia_datos

print("MATERIAS COMUNES ENTRE TODAS LAS CARRERAS")
print(comunes)

# Encontrar materias exclusivas de cada carrera
# Usamos la diferencia de conjuntos
exclusivas_software = ingenieria_software - ingenieria_sistemas - ciencia_datos
exclusivas_sistemas = ingenieria_sistemas - ingenieria_software - ciencia_datos
exclusivas_datos = ciencia_datos - ingenieria_software - ingenieria_sistemas

print("MATERIAS EXCLUSIVAS DE CADA CARRERA")
print("Exclusivas de Ingenieria de Software:", exclusivas_software)
print("Exclusivas de Ingenieria en Sistemas:", exclusivas_sistemas)
print("Exclusivas de Ingenieria en Ciencia de Datos:", exclusivas_datos)

# Crear la union de todas las materias
union = ingenieria_software | ingenieria_sistemas | ciencia_datos
print("UNION DE TODAS LAS MATERIAS")
print(union)

# Mostrar cuantas materias unicas hay en total
print("TOTAL DE MATERIAS UNICAS")
print("Cantidad de materias unicas:", len(union))
