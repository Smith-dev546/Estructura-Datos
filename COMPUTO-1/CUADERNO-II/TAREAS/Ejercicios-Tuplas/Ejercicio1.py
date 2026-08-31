## Ejercicio 1  Sistema de configuración de servidor.

## Una aplicación necesita almacenar configuraciones que no deben modificarse 
## accidentalmente durante la ejecución

##Crea una tupla llamada configuración con la siguiente información:

# Creación de la tupla configuración
configuracion = ("Sistema Académico", "1.0.0", "localhost", 8080, "producción")

# Mostrar el contenido de la tupla
print(configuracion)

## Acceso
## Mostrar solamente la version, el servidor y el puerto

print("La version del sistema es: ", configuracion[1])
print("El servidor del sistema es: ", configuracion[2])
print("El puerto del sistema es: ",configuracion[3])

## Longitud
## Utiliza len() para determinar cuántos elementos contiene la tupla

# Contar los elementos de la tupla
total_elementos = len(configuracion)

print("El total de elemento es: ", total_elementos)

