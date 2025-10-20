# Clase base
class Vehiculo:
    def acelerar(self):
        print("El vehículo está acelerando...")

# Subclase 1
class Auto(Vehiculo):
    def acelerar(self):
        print("El auto acelera aumentando la gasolina ")

# Subclase 2
class Bicicleta(Vehiculo):
    def acelerar(self):
        print("La bicicleta acelera pedaleando más rápido ")

# Subclase 3
class Avion(Vehiculo):
    def acelerar(self):
        print("El avión acelera encendiendo los motores a reacción ")

# Subclase 4
class Motosicleta(Vehiculo):
    def acelerar(self):
        print("La motosicleta va acelerando continuamente hasta alcanzar una buena velosidad")

auto1 = Auto()
bici1 = Bicicleta()
avion1 = Avion()
motosicleta1 = Motosicleta()

# Mismo método, diferente comportamiento
auto1.acelerar()
bici1.acelerar()
avion1.acelerar() 
motosicleta1.acelerar()