## Ejercicio 5: Crear un programa que demuestre el uso de diferentes tipos de variables en un contexto real:
## Simular el registro de un estudiante universitario
## Incluir: nombre (str), edad (int), promedio (float), becado (bool)
## Mostrar toda la información de manera organizada
## Realizar cálculos con las variables numérica

# Declaracion de las variables
nombre = "Pepito Fuentes"           # str - Nombre del estudiante
edad = 20                           # int - Edad en años
promedio = 9.50                     # float - Promedio académico (0-10)
becado = True                       # bool - Indica si tiene beca
carrera = "Ingeniería en Software"  # str - Carrera que estudia
semestre = 4                        # int - Semestre actual

# Mostramos la informacion del estudiante
print(f"Nombre completo: {nombre}")
print(f"Edad: {edad} años")
print(f"Carrera: {carrera}")
print(f"Semestre actual: {semestre}° semestre")
print(f"Promedio académico: {promedio:.2f}")
print(f"Estado de beca: {becado}")

# Operacion matematica con las variables numericas

#  Calcular edad al graduarse (asumiendo 2 semestres por año)
semestres_restantes = 10 - semestre  # 10 semestres = 5 años de carrera
años_restantes = semestres_restantes / 2
edad_graduacion = edad + años_restantes
print(f"Edad estimada al graduarse: {edad_graduacion:.0f} años")

