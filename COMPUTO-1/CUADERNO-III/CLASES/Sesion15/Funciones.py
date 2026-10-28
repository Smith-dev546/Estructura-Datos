## Ejemplo de como se crea las funciones

#def saludar():
 #   print("Hola")
  #  saludar()
  
## Ejemplo de una funcion con suma

#def suma(a,b):
 #   return a+b
#resultado = suma(5,3)

#print("El resultado es: ", resultado)

## Funcion con entrada de datos

def saludar(nombre):
    print("hola",nombre)
nombre1 = input("Ingrese el primer nombre:")
nombre2 = input("Ingrese el segundo nombre:")

saludar(nombre1)
saludar(nombre2)