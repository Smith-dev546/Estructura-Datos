## Haz un sistema de aceleracion usando funciones donde cada vez que
## presiones el aceleraador aumente 10 km
def Acelerar(velocidad_init):
    nueva_Velocidad = velocidad_init + 10
    return nueva_Velocidad

# Pedimos la velocidad inicial 
velocidad_init = int(input("Ingrese su velocidad inicial: "))
velocidad_init = Acelerar(velocidad_init)

print("Despues de acelerar tu velocidad es:", velocidad_init ," Km/h")
