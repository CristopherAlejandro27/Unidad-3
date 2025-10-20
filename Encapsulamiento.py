class Auto:
    def __init__(self, marca, velocidad_maxima):
        self.__marca = marca           #Asignar una marca al veiculo
        self.__velocidad_maxima = velocidad_maxima #Para guardar el valor de la velocidad 
        self.__velocidad_actual = 0 #Establecer la velocidad

    # obtiene velocidad
    def get_velocidad_actual(self):
        return self.__velocidad_actual

    # método para acelerar
    def acelerar(self, aumento):
        if self.__velocidad_actual + aumento > self.__velocidad_maxima:
            self.__velocidad_actual = self.__velocidad_maxima
        else:
            self.__velocidad_actual += aumento

    # método para frenar
    def frenar(self, reduccion):
        if self.__velocidad_actual - reduccion < 0:
            self.__velocidad_actual = 0
        else:
            self.__velocidad_actual -= reduccion


auto1 = Auto("Toyota", 180)

auto1.acelerar(50)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.acelerar(200)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto1.frenar(100)
print("Velocidad actual:", auto1.get_velocidad_actual(), "km/h")

auto2 = Auto("Lamborghini", 240)

auto2.acelerar(100)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

auto2.acelerar(300)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")

auto2.frenar(150)
print("Velocidad actual:", auto2.get_velocidad_actual(), "km/h")