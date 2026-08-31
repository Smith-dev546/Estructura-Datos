## Ejercicio 8: Crear un programa que trabaje con una cadena de texto usando slicing:

## Usar la frase: "Universidad de Oriente - El Salvador"
## Extraer solo "Universidad"
## Extraer solo "El Salvador"
## Mostrar la frase completa al revés
## Mostrar cada tercera letra de la frase

# Frase inicial
frase = "Universidad de Oriente - El Salvador"

# Mostrar la frase original
print("Frase original:")
print(frase)

# a) Extraer solo "Universidad"
universidad = frase[0:11]
print("a) Extraer solo 'Universidad':")
print(universidad)

# b) Extraer solo "El Salvador"
el_salvador = frase[21:]
print("b) Extraer solo 'El Salvador':")
print(el_salvador)

# c) Mostrar la frase completa al reves
frase_reves = frase[::-1]
print("c) Frase completa al reves:")
print(frase_reves)

# d) Mostrar cada tercera letra de la frase
cada_tercera = frase[::3]
print("d) Cada tercera letra de la frase:")
print(cada_tercera)
