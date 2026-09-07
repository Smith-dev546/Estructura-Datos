## Creamos una PILA
pila = []
print("El tipo de elemento es: ", type(pila))

## Agregamos elementos a la Pila con append()
pila.append("Iniciar Sesion")
pila.append("Consultar el perfil")
pila.append("Ver amigos en comun")
pila.append("Hola que hace?")

print("Los elementos que tiene esta pila son: ", pila)

## Desapilar un elemento
accion = pila.pop()
print("\n El ultimo elemento ingresado es: ", accion)

print("\n Penultima accion retirada", pila)

