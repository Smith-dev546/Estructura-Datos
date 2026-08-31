## Ejercicio 4: Crear un programa que declare variables de diferentes tipos de datos básicos y muestre su información:

## Crear al menos una variable de cada tipo: int, float, str, bool
## Usar la función type() para mostrar el tipo de cada variable
## Mostrar el valor y tipo de cada variable en formato legible
## Realizar al menos una operación compatible entre las variables, por ejemplo, concatenar cadenas o realizar una operación matemática.

# Declaración de variables de diferentes tipos
edad = 20                                               # Tipo int (entero)
promedio = 8.5                                          # Tipo float (decimal)
nombre = "Pepito Fuentes"                               # Tipo str (cadena de texto)
activo = True                                           # Tipo bool (booleano)

# Mostrar el valor y tipo de cada variable
print(f"Variable: edad = {edad}, Tipo: {type(edad)}")
print(f"Variable: promedio = {promedio}, Tipo: {type(promedio)}")
print(f"Variable: nombre = \"{nombre}\", Tipo: {type(nombre)}")
print(f"Variable: activo = {activo}, Tipo: {type(activo)}")

# Operaciones compatibles entre variables

# 1. Operación matemática (int + float)
suma_edad_promedio = edad + promedio
print(f"\nOperación matemática: edad + promedio = {edad} + {promedio} = {suma_edad_promedio}")
print(f"Tipo del resultado: {type(suma_edad_promedio)}")

# 2. Concatenación de cadenas (str + str)
nombre_completo = nombre + " Pérez"  # Agregamos un apellido
print(f"\nConcatenación de cadenas: nombre + \" Pérez\" = \"{nombre_completo}\"")
print(f"Tipo del resultado: {type(nombre_completo)}")