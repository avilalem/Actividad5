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
                return
        print("Estudiante no encontrado")

    def calcular_promedio(self):
        if not self.estudiantes:
            print("No hay estudiantes registrados")
            return
        total = sum(est.nota_final for est in self.estudiantes)
        promedio = total / len(self.estudiantes)
        print(f"Promedio: {promedio:.2f}")
def menu():
   sistema=SistemaDeEstudiantes()
   while True:
       print("\n ___ M E N U ___")
       print("1. Registrar estudiante")
       print("2. Mostrar estudiantes ")
       print("3. Buscar estudiantes por carne")
       print("4. Calcular promedio")
       print("5. Salir")


       opcion=input("Elige una opcion: ")
       if opcion=="1":
           nombre=input("Nombre: ")
           carne=input("Carne: ")
           carrera=input("Carrera: ")
           try:
            nota_final=float (input("Nota final: "))
            sistema.registrar_estudiante(nombre, carne, carrera, nota_final)
           except ValueError:
            print("Ingrese un numero valido")
       elif opcion=="2":
           sistema.mostrar_estudiantes()
       elif opcion=="3":
           carne=input("Carne: ")
           sistema.buscar_carne(carne)
       elif opcion=="4":
           sistema.calcular_promedio()
       elif opcion=="5":
           print("Gracias por usar el programa!")
           break
       else:
           print("opcion invalida. Intente nuevamente")
menu()
#:)
