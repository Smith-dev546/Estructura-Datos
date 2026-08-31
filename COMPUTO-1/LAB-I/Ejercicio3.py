## Ejercicio 3: Sin crear variables adicionales, solicitar que el estudiante de la Universidad de Oriente ingrese la siguiente información:
## (Nombres), (Apellidos), (Materia) y (Carnet) y que se imprima de la siguiente manera:


# Solicitar todos los datos directamente dentro del print usando f-string
# input() anidado dentro del print() para no crear variables intermedias
print(
    f"Hola, Bienvenido {input('Ingrese sus Nombres: ')} {input('Ingrese sus Apellidos: ')} "
    f"gracias por registrarte a la materia de: {input('Ingrese la Materia: ')}, "
    f"tu usuario para ingresar es: {input('Ingrese su Carnet: ')}@univo.edu.sv"
)