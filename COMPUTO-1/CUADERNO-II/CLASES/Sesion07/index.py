##nombre = "Pepito"
##print(nombre)
##print(nombre[3])
##print(nombre[-1])

##Usuario = "pepito";
##nuevo_usuario = "P" + Usuario[1:]
##print(nuevo_usuario)


producto = "Cuadernos"
print(producto[6:9])
print(producto[2:6])
print(producto[0:3])


##Listas 

Estudiantes = ["Ana", "Luis", "Carlos", "Maria"]
print(Estudiantes)
print(Estudiantes[0])

##Agregamos un nuevo elemesto a la lista

Estudiantes.append("Pedro")
print(Estudiantes)

##Eliminar un elemnto
Estudiantes.remove("Luis")
print(Estudiantes)

##Ejercicio de Listas 

## Crear una lista que contenga dos manzanas, banana, uva, manzana

Lista_Mercado = ["Manzana","Manzana", "banana", "uva", "Manzana"]
print(Lista_Mercado)

##Acceder por medio de indice a banana
print(Lista_Mercado[2])

## Agrege una fruta llamada pera y que solo muestre una manzana
Lista_Mercado_Limpia = list(set(Lista_Mercado))
Lista_Mercado_Limpia.append("Pera")
print(Lista_Mercado_Limpia)
