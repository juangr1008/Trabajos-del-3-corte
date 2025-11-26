class Personaje:
    def __init__(self, nombre, edad, raza, pueblo, rol, altura, complexion, fortalezas, debilidades, habilidad):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.pueblo = pueblo
        self.rol = rol
        self.altura = altura
        self.complexion = complexion
        self.fortalezas = fortalezas
        self.debilidades = debilidades
        self.habilidad = habilidad
        self.npc = None

    def asignar_npc(self, npc):
        self.npc = npc

    def mostrar_info(self):
        print("PERSONAJE")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Raza: {self.raza}")
        print(f"Pueblo de origen: {self.pueblo}")
        print(f"Rol: {self.rol}")
        print(f"Altura: {self.altura} m")
        print(f"Complexión: {self.complexion}")
        print("\nFortalezas:")
        for f in self.fortalezas:
            print(f"- {f}")
        print("\nDebilidades:")
        for d in self.debilidades:
            print(f"- {d}")
        print(f"\nHabilidad especial: {self.habilidad}")

        if self.npc:
            print("\nAcompañante NPC:")
            self.npc.mostrar_info()

    def usar_habilidad(self):
        print(f"\n{self.nombre} te invita a que sirvas de algo y uses su habilidad {self.habilidad} ")

class NPC:
    def __init__(self, nombre, especie, rol, personalidad):
        self.nombre = nombre
        self.especie = especie
        self.rol = rol
        self.personalidad = personalidad

    def mostrar_info(self):
        print(f"  NPC: {self.nombre} ({self.especie}) - Rol: {self.rol}")
        print(f"  Personalidad: {self.personalidad}")

def crear_personaje_por_rol(rol):
    rol = rol.lower()

    if rol == "guerrero":
        personaje = Personaje(
            "Kraticos Calviño",
            28,
            "Humano",
            "Aldea de bárbaros",
            "Guerrero",
            1.85,
            "Musculoso",
            ["Gran fuerza física", "Resistente al daño"],
            ["Una minita que no lo quiere", "Mala estrategia táctica"],
            "Golpe de Ella: Un ataque poderoso al corazón"
        )
        npc = NPC("Rocky", "Lobo gigante", "Guardián", "Feroz bailarín pero protector")

    elif rol == "mago":
        personaje = Personaje(
            "Masterfire",
            21,
            "Humano",
            "Bosque encantado",
            "Mago",
            1.78,
            "Delgado",
            ["Gran dominio mágico", "Alta inteligencia"],
            ["Baja resistencia física", "Se agota al usar magia avanzada"],
            "Llamarada Armoniosa: Explosión controlada de energía elemental"
        )
        npc = NPC("Kirikú", "Espíritu-cuervo", "Explorador", "Sarcástico, pero leal")

    elif rol == "curandero":
        personaje = Personaje(
            "Sanandiño Curandiño",
            19,
            "Elfa",
            "Santuario de Lunaris",
            "Curandero",
            1.70,
            "Esbelta",
            ["Sanación avanzada", "Empatía sobrenatural"],
            ["Miedo al combate directo", "Dependencia de energía espiritual"],
            "Bendición Lunar: Cura total en área"
        )
        npc = NPC("Tinkerbell", "Ciervo místico", "Guía espiritual", "Calmo y sabio")

    elif rol == "cazador":
        personaje = Personaje(
            "Thor",
            24,
            "Semielfo",
            "Selva oscura",
            "Cazador",
            1.82,
            "Ágil",
            ["Movilidad excelente", "Puntería precisa"],
            ["Débil en combate cuerpo a cuerpo", "No trabaja bien en equipo"],
            "Disparo Fantasma: Flecha que no puede ser esquivada"
        )
        npc = NPC("Alita", "Halcón gigante", "Scout", "Orgullosa y silenciosa")

    else:
        print(" Rol no disponible. Elige: Guerrero, Mago, Curandero o Cazador.")
        return None

    personaje.asignar_npc(npc)
    return personaje

rol_elegido = input("Elige tu rol (Guerrero / Mago / Curandero / Cazador): ")
pj = crear_personaje_por_rol(rol_elegido)

if pj:
    pj.mostrar_info()
    pj.usar_habilidad()

input ("\nPresiona Enter para salir...")