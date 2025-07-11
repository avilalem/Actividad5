class Estudiante:
    def __init__(self, nombre, carne, carrera, nota_final):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.nota_final = nota_final

class SistemaDeEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def registrar_estudiante(self, nombre, carne, carrera, nota_final):
        estudiante = Estudiante(nombre, carne, carrera, nota_final)
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
         if not self.estudiantes:
            print("No hay estudiantes registrados")
            for est in self.estudiantes:
            print(f"Nombre: {est.nombre} - Carne: {est.carne} - Carrera: {est.carrera} - Nota: {est.nota_final}")

    def buscar_carne(self, carne):
        for est in self.estudiantes:
            if est.carne == carne:
                print(f"Estudiante encontrado")
                print(f"Nombre: {est.nombre} - Carrera: {est.carrera} - Nota: {est.nota_final}")
        print("Estudiante no encontrado")

    def calcular_promedio(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados")

        total = sum(est.nota_final for est in self.estudiantes)
        promedio = total / len(self.estudiantes)
        print(f"Promedio: {promedio:.2f}")
