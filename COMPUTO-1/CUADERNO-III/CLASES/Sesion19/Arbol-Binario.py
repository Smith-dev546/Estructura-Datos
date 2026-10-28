class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecha = None
        
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)
n6 = Nodo(6)
n7 = Nodo(7)
n8 = Nodo(8)
n9 = Nodo(9)
n10 = Nodo(10)

n1.izquierda = n2
n1.derecha = n3

n2.izquierda = n4
n2.derecha = n5

n5.izquierda = n8

n3.izquierda = n6
n3.derecha = n7

n7.izquierda = n9
n7.izquierda = n10