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
