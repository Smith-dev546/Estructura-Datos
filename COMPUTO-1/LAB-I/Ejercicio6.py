## Ejercicio 6: Crear una lista con los nombres de 5 materias de Ingeniería de Software y realizar las siguientes operaciones:
## a) Mostrar la lista completa 
## b) Agregar 2 materias más usando append() 
## c) Insertar una materia en la posición 2
## d) Eliminar la última materia usando remove() 
## e) Mostrar el número total de materias 

# Creamos una lista con las 5 materias sugeridas
materias = ["Programación Estructurada", "Estructura de Datos", "Base de Datos", "POE", "Redes"]

# a) Mostrar la lista completa
print("LISTA COMPLETA DE MATERIAS")
print(f"Materias: {materias}")
print(f"Cantidad de materias: {len(materias)}\n")

# b) Agregar 2 materias más usando append()
# append() agrega elementos al final de la lista
materias.append("Sistemas Operativos")
materias.append("POO")


print("DESPUÉS DE AGREGAR 2 MATERIAS CON append()")
print(f"Materias: {materias}")
print(f"Cantidad de materias: {len(materias)}\n")

# c) Insertar una materia en la posición 2
# insert(posición, elemento) inserta en el índice indicado
# Índice 2 = tercera posición (0, 1, 2)
materias.insert(2, "Matemáticas I")

print("DESPUÉS DE INSERTAR EN POSICIÓN 2")
print(f"Materias: {materias}")
print(f"Cantidad de materias: {len(materias)}\n")

# d) Eliminar la última materia usando remove()
ultima_materia = materias[-1]  # Accedemos al último elemento
materias.remove(ultima_materia)

print("DESPUÉS DE ELIMINAR LA ÚLTIMA MATERIA")
print(f"Materia eliminada: {ultima_materia}")
print(f"Materias: {materias}")
print(f"Cantidad de materias: {len(materias)}\n")

# e) Mostrar el número total de materias
print("RESUMEN FINAL")
print(f"Número total de materias: {len(materias)}")
print(f"Lista final de materias: {materias}")
