#Sistema de gestión de vehiculos en una ciudad inteligente
class vehiculo: 
    def __init__(self, marca, modelo, año, velocidad_actual):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_actual = int(velocidad_actual)
    def acelerar(self, incrementa_la_velocidad):
        self.velocidad_actual += incrementa_la_velocidad
        print(f"El Vehículo aceleró y ahora va a {self.velocidad_actual} Km/h")
    def frenar(self, reduce_la_velocidad):
        self.velocidad_actual -= reduce_la_velocidad
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
        print(f"El vehiculo frenó y va a: {self.velocidad_actual} km/h")
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Velocidad Actual: {self.velocidad_actual} km/h")
        
class Carro(vehiculo):
    def __init__(self, marca, modelo, año, velocidad_actual, num_puertas):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.num_puertas = num_puertas
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Puertas: {self.num_puertas}")

class Moto(vehiculo):
    def __init__(self, marca, modelo, año, velocidad_actual, cilindraje):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.cilindraje = cilindraje
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindraje: {self.cilindraje} cc")

class Bicicleta(vehiculo):
    def __init__(self, marca, modelo, año, velocidad_actual, tipo):
        super().__init__(marca, modelo, año, velocidad_actual)
        self.tipo = tipo
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo: {self.tipo}")

Chevy = Carro("Mazda", "MX-5", "1989", 80, "2 puertas")


Mustang = Carro("Ford", "Mustang", "2020", 100, "2 puertas")


XR150 = Moto("Honda", "XR150", "2026", 60, "150 cc")


Dr150 = Moto("Suzuki", "Dr150", "2024", 70, "150 cc")


Giant = Bicicleta("TCR", "Advanced", "2021", 30, "Carretera")


Specialized = Bicicleta("Rockhopper", "Expert 29", "2022", 25, "Montaña")


#Crear una lista de vehículos de diferentes tipos
#Recorrer la lista y mostrar la información de cada vehículo
#Demostrar como cada objeto responde a los métodos acelerar y frenar

vehiculos = [
    Carro("Mazda", "MX-5", "1989", 80, "2 puertas"),
    Carro("Ford", "Mustang", "2020", 100, "2 puertas"),

    Moto("Honda", "XR150", "2026", 60, "150 cc"),
    Moto("Suzuki", "Dr150", "2024", 70, "150 cc"),

    Bicicleta("TCR", "Advanced", "2021", 30, "Carretera"),
    Bicicleta("Rockhopper", "Expert 29", "2022", 25, "Montaña"),
]
for v in vehiculos:
    v.mostrar_info()
    v.acelerar(20)
    v.frenar(5)
    print("-" * 40)

input("Presiona Enter para salir...")