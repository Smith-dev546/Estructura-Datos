## Supongamos que estamos desarrolando un sistema para una empresa.
##TEnemos un producto

producto = {
    "codigo": "P001",
    "nombre": "Teclado mecanico",
    "precio": 45.99,
    "stock": 20,
    "disponible": True
}

## Podemos consultar el nombre del producto
print("El nombre del producto buscado es: ", producto["nombre"])

## Cambiar la disponibilidad del productony el stock a 0

producto["stock"] = 0
producto["disponible"] = None

print("El stock del producto es: ", producto["stock"])
print("Esta disponible el producto?: ", producto["disponible"])