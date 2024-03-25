#!/usr/bin/env python3

'''EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal'''


class Animal:

    def __init__(self, tipo, nombre, raza, edad, color, sonido):     # Siempre pasar los parámetros como argumentos.
        self.tipo = tipo
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.sonido = sonido
        
    def hacer_sonido(self):
        return print(f"Mi mascota {self.nombre} hace {self.sonido}")
        # Una función dentro de una clase tiene que tener un return sí o sí
        # Si pusiera return print (f"...) saldría un None tras el print si lo estuviera llamando con el print (queda doble)
  
class Gato(Animal):        # clase Gato hereda de clase Animal
    def __init__(self, nombre, raza, edad, color):
        super().__init__("gato", nombre, raza, edad, color, "Miaauuu")  
        # super() hace que herede y ya no hace falta el self
        # Aqui puedo inicializar ya el tipo y el sonido para poder llamarlos luego y no tener que ponerlos en las instancias
    
    def edad_humana(self):    # Método de instancia, debe tener self como 1º parámetro para acceder a los atributos de la instancia
        return self.edad * 5

class Perro(Animal):        # clase Perro hereda de clase Animal
    def __init__(self, nombre, raza, edad, color):
        super().__init__("perro", nombre, raza, edad, color, "Wooff")
        
    def edad_humana(self):    # Método de instancia, debe tener self como 1º parámetro para acceder a los atributos de la instancia
        return self.edad * 7

# Creo instancias para perro y gato
gato1 = Gato("Totoro", "exotico", 8, "blanco")
perro1 = Perro("Luna", "labradora", 13, "crema")

print(gato1.edad_humana())      # 40
print(perro1.edad_humana())     # 91
print(gato1.sonido)             # Miaauuu
gato1.hacer_sonido()            # Mi mascota Totoro hace Miaauuu
perro1.hacer_sonido()           # Mi mascota Luna hace Wooff

'''DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.'''

class Empleado:

    def __init__(self, id, name, empleados_a_cargo=None):
        self.id = id
        self.name = name
        self.empleados_a_cargo = empleados_a_cargo

        # None actúa como un valor predeterminado, útil para evitar errores si un atributo es opcional 
        # y no siempre se necesita al instanciar el objeto.
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.name}")
        print(f"Id de empleado: {self.id}")
        print(f"Cargo: {type(self).__name__}")

    def mostrar_empleados_a_cargo (self):  # No olvidar siempre primero el self
        print(f"Empleados a cargo: {self.empleados_a_cargo}")
        
class Gerente (Empleado):

    def __init__(self, id, name, empleados_a_cargo=None):
        super().__init__(id, name, empleados_a_cargo)
        self.empleados_a_cargo= [Gerente_proyecto.__name__, Programador.__name__]
        # En el 1º __init__ le digo los que quiero que herede y reciba de la clase principal
        # En el __initi__ del super() pongo los que hereda y ya relleno los que son propios de la subclase

class Gerente_proyecto (Empleado):

    def __init__(self, id, name, empleados_a_cargo=None):
        super().__init__(id, name, empleados_a_cargo)
        self.empleados_a_cargo= [Programador.__name__]

class Programador (Empleado):

    def __init__(self, id, name, empleados_a_cargo=None):
        super().__init__(id, name, empleados_a_cargo)
        self.empleados_a_cargo= ["Nadie"]

# Instancias
Jefe = Gerente(1, "Zeus")
G_Proyecto1 = Gerente_proyecto(2, "Moure")
Dev1 = Programador (3, "Troy")

Jefe.mostrar_informacion()
print()
G_Proyecto1.mostrar_informacion()
print()
Dev1.mostrar_informacion()
print()

Jefe.mostrar_empleados_a_cargo()        # Empleados a cargo: ['Gerente_proyecto', 'Programador']
Dev1.mostrar_empleados_a_cargo()