## Elige 5 casos donde un valor suelto no basta: debe cumplir una regla para ser valido

## Implementalos como claves; valida la regla al crear el objeto (Por ejemplo, en _init_)

## Por cada tipo, muestra un caso de uso valido y uno no invalido rechace

## Explica en un comentario que error o daato incorrecto evita cada validación

class Email:
    def __init__(self, direccion):
        if "@" not in direccion or "." not in direccion:
            raise ValueError("Dirección de correo inválida")
        self.direccion = direccion

class Edad:
    def __init__(self, valor):
        if not isinstance(valor, int) or valor < 0 or valor > 120:
            raise ValueError("Edad fuera del rango permitido (0-120)")
        self.valor = valor

class Nota:
    def __init__(self, calificacion):
        if not (0.0 <= calificacion <= 10.0):
            raise ValueError("La nota debe estar entre 0.0 y 10.0")
        self.calificacion = calificacion

# Clases nuevas agregadas

class Precio:
    def __init__(self, valor):
        # Evita registrar productos con precios negativos o gratis por error
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.valor = valor

class CodigoPostal:
    def __init__(self, codigo):
        # Evita códigos postales con un formato incorrecto (ej. texto o longitud errónea)
        if not isinstance(codigo, str) or len(codigo) != 5 or not codigo.isdigit():
            raise ValueError("El código postal debe tener exactamente 5 números")
        self.codigo = codigo


# EJEMPLOS DE USO (Casos válidos e inválidos requeridos)

print("--- Probando Casos Válidos Originales ---")
try:
    e = Email("usuario@dominio.com")
    ed = Edad(20)
    n = Nota(8.5)
    print("Objetos creados exitosamente")
except ValueError as err:
    print("Error:", err)

print("\n--- Probando Casos Inválidos Originales ---")
try:
    e_invalido = Email("correo_sin_arroba.com")
except ValueError as err:
    print("Capturado:", err)

# Ejemplos inválidos adicionales para tus clases originales (Requisito #3)
try:
    edad_invalida = Edad(150)
except ValueError as err:
    print("Capturado (Edad > 120):", err)

try:
    nota_invalida = Nota(-1.5)
except ValueError as err:
    print("Capturado (Nota negativa):", err)


print("\n--- Probando Nuevas Clases (Casos Válidos) ---")
try:
    p = Precio(19.99)
    cp = CodigoPostal("28001")
    print("Nuevos objetos creados exitosamente")
except ValueError as err:
    print("Error:", err)

print("\n--- Probando Nuevas Clases (Casos Inválidos) ---")
try:
    precio_invalido = Precio(-5)
except ValueError as err:
    print("Capturado:", err)

try:
    cp_invalido = CodigoPostal("123")
except ValueError as err:
    print("Capturado:", err)


# COMENTARIOS EXPLICATIVOS (Requisito #4 de la actividad)

# Email: Evita el registro de cadenas de texto arbitrarias que no cumplan la estructura mínima de un correo electrónico.
# Edad: Evita registrar tipos de datos incorrectos (como texto) o edades biológicamente imposibles (negativas o mayores a 120).
# Nota: Evita almacenar calificaciones escolares fuera de la escala estándar permitida (0.0 a 10.0).
# 4. Precio: Evita que el sistema procese transacciones erróneas con valores en cero o saldos negativos.
# 5. CodigoPostal: Evita errores de envío postal causados por códigos mal formateados, incompletos o que contengan letras.