class NPC:
    def __init__(self, nombre, habilidad, nivel, rol, poder_apoyo):
        self.nombre = nombre
        self.habilidad = habilidad
        self.nivel = nivel
        self.rol = rol
        self.poder_apoyo = poder_apoyo

    def mostrar_info(self):
        print(f"NPC: {self.nombre}")
        print(f" Habilidad: {self.habilidad}")
        print(f" Nivel: {self.nivel}")
        print(f" Rol: {self.rol}")
        print(f" Poder de apoyo: {self.poder_apoyo} pts")

class Personaje:
    def __init__(self, tipo, nombre, equipo_especial, resistencia, habilidades,
                 oficio, poder_equipo, arma, daño, npc):
        
        self.tipo = tipo
        self.nombre = nombre
        self.vidas = 3
        self.equipo_especial = equipo_especial
        self.resistencia = resistencia
        self.habilidades = habilidades
        self.oficio = oficio
        self.poder_equipo = poder_equipo
        self.arma = arma
        self.daño = daño
        self.npc = npc

    def mostrar_personaje(self):
        print("\n-PERSONAJE-")
        print(f"Tipo: {self.tipo}")
        print(f"Nombre: {self.nombre}")
        print(f"Vidas: {self.vidas}")
        print(f"Equipo especial: {self.equipo_especial}")
        print(f"Resistencia: {self.resistencia} pts")
        print(f"Habilidades: {self.habilidades} pts")
        print(f"Oficio: {self.oficio}")
        print(f"Poder del equipo: {self.poder_equipo} pts")
        print(f"Arma especial: {self.arma}")
        print(f"Daño del arma: {self.daño} pts")

        print("\n-Compañero de batalla-")
        self.npc.mostrar_info()

npc1 = NPC(
    nombre="Chamorrin",
    habilidad="protección ligera",
    nivel="Intermedio",
    rol="Escudero",
    poder_apoyo=850
)

personaje1 = Personaje(
    tipo="Guerrero",
    nombre="Thanitos Chupiplú",
    equipo_especial="Espada puñalona",
    resistencia=1800,
    habilidades=1900,
    oficio="Caballero",
    poder_equipo=1200,
    arma="Espada legendaria",
    daño=450500,
    npc=npc1
)

personaje1.mostrar_personaje()

input("\nPresiona Enter para continuar...")