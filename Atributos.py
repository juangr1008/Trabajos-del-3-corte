class Persona:
    def __init__(self, nombre, edad, genero, ocupacion, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion
        self.ciudad = ciudad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.ocupacion} y vivo en {self.ciudad}.")
    
    def estudiar(self):
        print(f"{self.nombre} estudia ingeniería informática.")

juan = Persona("Juan Diego", 19, "Hombre", "Estudiante", "Barranca")

juan.presentarse()
juan.estudiar()