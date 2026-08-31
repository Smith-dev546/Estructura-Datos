## Ejercicio 7: Dada la siguiente lista de días de la semana, realizar operaciones de slicing:
## dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
## a) Mostrar los primeros 3 días 
## b) Mostrar los últimos 2 días 
## c) Mostrar los días laborales (Lunes a Viernes) 
## d) Mostrar el fin de semana 
## e) Mostrar todos los días en orden inverso 
## f) Mostrar un día sí y otro no (días pares)

# Lista inicial de días
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# a) Mostrar los primeros 3 dias
primeros_3 = dias[0:3]
print("a) Primeros 3 dias:")
print(primeros_3)

# b) Mostrar los ultimos 2 dias
ultimos_2 = dias[-2:]
print("b) Ultimos 2 dias:")
print(ultimos_2)

# c) Mostrar los dias laborales (Lunes a Viernes)
laborales = dias[0:5]
print("c) Dias laborales (Lunes a Viernes):")
print(laborales)

# d) Mostrar el fin de semana
fin_semana = dias[5:7]
print("d) Fin de semana:")
print(fin_semana)

# e) Mostrar todos los dias en orden inverso
orden_inverso = dias[::-1]
print("e) Dias en orden inverso:")
print(orden_inverso)

# f) Mostrar un dia si y otro no (dias pares)
dias_pares = dias[::2]
print("f) Un dia si y otro no:")
print(dias_pares)
