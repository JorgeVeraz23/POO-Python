"""class Cuadrado:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcularArea(self):
        area = self.ancho * self.alto
        return area

figura = Cuadrado(10, 12)

print(figura.calcularArea())

print(figura.ancho)"""

from Empleado import Empleado
from Cliente import Cliente


"""emp = Empleado('Lucas', 'Moy', '123123', '23456789',1000)
cli = Cliente('jorge','vera', '12543','58223', 'vip')"""



def cargar():
    respuesta = input("¿Va a agregar a un empleado?")
    nombre = input("ingrese el nombre")
    apellido = input("ingrese el apellido")
    dni = input("ingrese el dni")
    telefono = input("telefono")

    if (respuesta == "si"):
        salario = input("ingrese el salario")
        emp = Empleado(nombre, apellido, dni, telefono, int(salario))
        personas.append(emp)
    else:
        tipo = input("ingrese el tipo de clientes")
        cli = Empleado(nombre, apellido, dni, telefono, tipo)
        personas.append(cli)

personas = []

cargar()
cargar()

for persona in personas:
    print(persona)