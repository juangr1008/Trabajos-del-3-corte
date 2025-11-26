class Militar:
    def __init__(self, nombre, identificacion, rango, peloton):
        self.nombre = nombre
        self.identificacion = identificacion
        self.rango = rango
        self.peloton = peloton

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"ID: {self.identificacion}")
        print(f"Rango: {self.rango}")
        print(f"Pelotón: {self.peloton}")

class SoldadoRaso(Militar):
    def __init__(self, nombre, identificacion, peloton, alias, tiempo_servicio):
        super().__init__(nombre, identificacion, "Soldado Raso", peloton)
        self.alias = alias
        self.tiempo_servicio = tiempo_servicio

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Alias: {self.alias}")
        print(f"Tiempo de Servicio: {self.tiempo_servicio} años")

class Cabo(Militar):
    def __init__(self, nombre, identificacion, peloton, tiempo_servicio):
        super().__init__(nombre, identificacion, "Cabo", peloton)
        self.tiempo_servicio = tiempo_servicio

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tiempo de Servicio: {self.tiempo_servicio} años")

class Sargento(Militar):
    def __init__(self, nombre, identificacion, peloton):
        super().__init__(nombre, identificacion, "Sargento", peloton)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Responsabilidad: Está a cargo de un pelotón")

class Teniente(Militar):
    def __init__(self, nombre, identificacion, peloton, oficiales_a_cargo):
        super().__init__(nombre, identificacion, "Teniente", peloton)
        self.oficiales_a_cargo = oficiales_a_cargo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Oficiales a cargo: {self.oficiales_a_cargo}")

class General(Militar):
    def __init__(self, nombre, identificacion, peloton, batallon):
        super().__init__(nombre, identificacion, "General", peloton)
        self.batallon = batallon

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Batallón a cargo: {self.batallon}")

soldado = SoldadoRaso("Lucho Díaz", 1000, "Pelotón Alfanumérico", "El Halcón", 2)
cabo = Cabo("Luisito Comunica", 1001, "Pelotón Bravo pero feliz", 4)
sargento = Sargento("Marcos Reus", 1002, "Pelotón Delta")
teniente = Teniente("Torres Gemelas", 1003, "Pelotón Épico", 10)
general = General("Roberto Carlos saveiro du brasil", 1004, "Pelotón apocaliptico", "Batallón Fénix")

soldado.mostrar_info()

cabo.mostrar_info()

sargento.mostrar_info()

teniente.mostrar_info()

general.mostrar_info()

input("Presione Enter para salir...")