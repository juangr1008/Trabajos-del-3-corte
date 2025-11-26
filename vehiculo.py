class Vehiculo:
    def __init__(self, marca, modelo, color, tipo_terreno, capacidad_personas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipo_terreno = tipo_terreno
        self.capacidad_personas = capacidad_personas

    def moverse(self):
        print(f"El {self.marca} {self.modelo} de color {self.color} y es {self.tipo_terreno}.")

    def transportar(self):
        print(f"Este vehículo puede transportar hasta {self.capacidad_personas} personas cómodamente.")

auto = Vehiculo("Toyota", "Hilux", "blanco", "todo terreno", 5)

auto.moverse()
auto.transportar()