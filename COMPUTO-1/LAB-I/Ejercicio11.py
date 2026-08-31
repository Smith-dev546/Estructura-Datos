## Ejercicio 11: Una empresa de desarrollo de software necesita llevar un registro de los módulos que forman parte de un sistema.
##Crea una lista llamada módulos con los siguientes elementos:
## Módulos = Autenticación, Usuarios, Productos, Reportes, Notificaciones.

## Desarrolla un programa que realice las siguientes acciones:
## a) Mostrar la lista completa de módulos.
## b) Agregar el módulo "Pagos" utilizando append().
## c) Insertar "Dashboard" en la posición 2 utilizando insert().
## d) Modificar "Productos" por "Inventario" utilizando su índice.
## e) Eliminar "Notificaciones" utilizando remove().
## f) Mostrar cuántos módulos tiene actualmente el sistema utilizando len().
## g) Mostrar la lista final.

# Crear la lista inicial de módulos
modulos = ["Autenticación", "Usuarios", "Productos", "Reportes", "Notificaciones"]

print("GESTION DE MODULOS DEL SISTEMA")

# a) Mostrar la lista completa de módulos
print("a) Lista completa de módulos:")
print(modulos)

# b) Agregar el módulo "Pagos" utilizando append()
modulos.append("Pagos")
print("b) Después de agregar 'Pagos' con append():")
print(modulos)

# c) Insertar "Dashboard" en la posición 2 utilizando insert()
modulos.insert(2, "Dashboard")
print("c) Después de insertar 'Dashboard' en posición 2:")
print(modulos)

# d) Modificar "Productos" por "Inventario" utilizando su índice
indice_productos = modulos.index("Productos")
modulos[indice_productos] = "Inventario"
print("d) Después de modificar 'Productos' por 'Inventario':")
print(modulos)

# e) Eliminar "Notificaciones" utilizando remove()
modulos.remove("Notificaciones")
print("e) Después de eliminar 'Notificaciones' con remove():")
print(modulos)

# f) Mostrar cuántos módulos tiene actualmente el sistema
print("f) Número total de módulos:")
print(len(modulos))

# g) Mostrar la lista final
print("LISTA FINAL DE MODULOS")
print(modulos)