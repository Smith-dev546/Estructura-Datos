##pila = []

## Agregamos 3 elementos A, B C

##pila.append("A")
##pila.append("B")
##pila.append("C")

##print(pila)
##pila.append("D")
##pila.append("E")

def push(pila, elemnto):  #Creamos una funcion llamada push
    pila.append(elemnto)
    
def pop(pila):  ##Creamos pop para retirar elementos
    return pila.pop()

# Creamos una pila vacia
pila = []
push(pila, "A")
push(pila, "B")
push(pila, "C")

print("Los elementos de la pila son: ", pila)

elemento = pop(pila)
print("El ultimo elemento de la pila es: ", elemento)