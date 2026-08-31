## Creamos un diccionario
estudiante = {
    "nombre": "Pepito",
    "Edad": 20,
    "cursos": ["Python", "Estructura de datos"]
}

## Mostramos el diccionario
print(estudiante)

## Accedemos al nombre del estudinte
print("El estudiante es: ", estudiante["nombre"])

## Modificamos la edad
estudiante["Edad"] = 22
print("La edad actual del estudiante es: ", estudiante["Edad"], " anios")

## Agregamos una nueva carrera
estudiante["carrera"] = "Ing. Software"
print(estudiante["nombre"], " estudia la carrera de: ", estudiante["carrera"])

## Eliminamos un metodo del
del estudiante["Edad"]
print(estudiante)

## ELiminamos metodo pop
## estudiante.pop("Edad")

