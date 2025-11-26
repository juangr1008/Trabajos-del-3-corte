# Dos equipos de 5 jugadores cada uno, 1 arquero, 2 laterales, 1 armador, 1 delantero
# Arquero cuantos goles tapó
# Lateral cuantos jugadores bloqueó
# Armador cuantas jugadas o pases realizó
# Delantero cuantos tiros al arco realizó
# El usuario debe indicar que jugador realiza el gol durante el partido
# En la terminal se debe mostrar el nombre y el dorsal del jugador mas el número de goles que hizo
# El usuario debe tener la opción de ingresar quien hizo el gol mediante el dorsal del jugador

class jugador:
    def __init__(self, nombre, dorsal, goles, posicion):
        self.nombre = nombre
        self.dorsal = dorsal
        self.goles = goles
        self.posicion = posicion
    def descripcion(self):
        print(f"El jugador {self.nombre}, con dorsal {self.dorsal}, ha marcado {self.goles} goles y juega en la posición de {self.posicion}.")

class arquero(jugador):
    def __init__(self, nombre, dorsal, goles, posicion, goles_tapados):
        super().__init__(nombre, dorsal, goles, posicion)
        self.goles_tapados = goles_tapados
    def descripcion(self):
        super().descripcion()
        print(f"Ha tapado {self.goles_tapados} goles.")

class lateral(jugador):
    def __init__(self, nombre, dorsal, goles, posicion, jugadores_bloqueados):
        super().__init__(nombre, dorsal, goles, posicion)
        self.jugadores_bloqueados = jugadores_bloqueados
    def descripcion(self):
        super().descripcion()
        print(f"Ha bloqueado a {self.jugadores_bloqueados} jugadores.")

class armador(jugador):
    def __init__(self, nombre, dorsal, goles, posicion, jugadas_realizadas):
        super().__init__(nombre, dorsal, goles, posicion)
        self.jugadas_realizadas = jugadas_realizadas
    def descripcion(self):
        super().descripcion()
        print(f"Ha realizado {self.jugadas_realizadas} jugadas.")

class delantero(jugador):
    def __init__(self, nombre, dorsal, goles, posicion, tiros_al_arco):
        super().__init__(nombre, dorsal, goles, posicion)
        self.tiros_al_arco = tiros_al_arco
    def descripcion(self):
        super().descripcion()
        print(f"Ha realizado {self.tiros_al_arco} tiros al arco.")

class arquero2(jugador):
    def __init__(self, nombre, dorsal, goles, posicion, goles_tapados):
        super().__init__(nombre, dorsal, goles, posicion)
        self.goles_tapados = goles_tapados
    def descripcion(self):
        super().descripcion()
        print(f"Ha tapado {self.goles_tapados} goles.")

class lateral1(jugador):
    def __init__(self, nombre, dorsal, goles, posicion, jugadores_bloqueados):
        super().__init__(nombre, dorsal, goles, posicion)
        self.jugadores_bloqueados = jugadores_bloqueados
    def descripcion(self):
        super().descripcion()
        print(f"Ha bloqueado a {self.jugadores_bloqueados} jugadores.")

class armador2(jugador):
    def __init__(self, nombre, dorsal, goles, posicion, jugadas_realizadas):
        super().__init__(nombre, dorsal, goles, posicion)
        self.jugadas_realizadas = jugadas_realizadas
    def descripcion(self):
        super().descripcion()
        print(f"Ha realizado {self.jugadas_realizadas} jugadas.")

class delantero2(jugador):
    def __init__(self, nombre, dorsal, goles, posicion, tiros_al_arco):
        super().__init__(nombre, dorsal, goles, posicion)
        self.tiros_al_arco = tiros_al_arco
    def descripcion(self):
        super().descripcion()
        print(f"Ha realizado {self.tiros_al_arco} tiros al arco.")

jugador1 = arquero("Chamorriño", 1, 0, "Arquero", 5)
jugador2 = lateral("Johansiño", 2, 0, "Lateral", 3)
jugador3 = armador("Keinsiño", 3, 0, "Armador", 10)
jugador4 = delantero("Granadiños", 4, 0, "Delantero", 7)
jugador5 = lateral("Jensiño", 5, 0, "Lateral", 4)
jugador6 = arquero2("Gabrieliño", 6, 0, "Arquero rojos", 4)
jugador7 = lateral1("Millersiño", 7, 0, "Lateral rojos", 4)
jugador8 = armador2("Jaja", 8, 0, "Armador rojos", 7)
jugador9 = delantero2("Yarl", 9, 0, "Delantero rojos", 6)
jugador10 = lateral1("Sar", 10, 0, "Lateral rojos", 4)

jugadores = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8, jugador9, jugador10]

locales = jugadores[:5]
visitantes = jugadores[5:]

print("El partido empezó.")
print("Locales del 1 al 5")
print("Visitantes del 6 al 10")

while True:
    accion = input("G para registrar gol, F para finalizar: ").upper()
    if accion == "F":
        print("El partido finalizó.")
        break
    elif accion == "G":
        dorsal_gol = int(input("Ingrese el dorsal del jugador que marcó el gol: "))
        encontrado = False
        for j in jugadores:
            if j.dorsal == dorsal_gol:
                j.goles += 1
                encontrado = True
                print(f"Gol registrado para {j.nombre}.")
                break
        if not encontrado:
            print("Dorsal no válido.")
    else:
        print("Opción no válida.")

max_goles = max(jugadores, key=lambda x: x.goles)
print(f"El jugador con más goles es {max_goles.nombre} con dorsal {max_goles.dorsal} y ha marcado {max_goles.goles} goles.")

print("\nEquipo local")
for jugador in locales:
    jugador.descripcion()

print("\nEquipo visitante")
for jugador in visitantes:
    jugador.descripcion()

input("Presiona Enter para salir.")

