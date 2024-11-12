class Alumno:
    def __init__(self, nombre, apellido, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.notas = []  
        self.faltas = 0  
        self.amonestaciones = 0  

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def asignar_falta(self):
        self.faltas += 1

    def asignar_amonestacion(self):
        self.amonestaciones += 1

    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def obtener_promedio(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        return 0

    def __str__(self):
        return (f"Nombre: {self.nombre} {self.apellido}\n"
                f"Dirección: {self.direccion}\n"
                f"Notas: {self.notas}\n"
                f"Promedio: {self.obtener_promedio():.2f}\n"
                f"Faltas: {self.faltas}\n"
                f"Amonestaciones: {self.amonestaciones}\n")


class RegistroAlumnos:
    def __init__(self):
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            for alumno in self.alumnos:
                archivo.write(str(alumno) + "\n")
                archivo.write("=" * 40 + "\n")

    def mostrar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno)


if __name__ == "__main__":
    alumno1 = Alumno("Sebastian", "zapata","Calle Lavalle 123")
    alumno1.agregar_nota(8)
    alumno1.agregar_nota(9)
    alumno1.asignar_falta()
    alumno1.asignar_amonestacion()

    alumno2 = Alumno("Marcelo","Britos", "Barcala 456")
    alumno2.agregar_nota(6)
    alumno2.agregar_nota(7)
    alumno2.asignar_falta()

    registro = RegistroAlumnos()
    registro.agregar_alumno(alumno1)
    registro.agregar_alumno(alumno2)

    registro.mostrar_alumnos()

    registro.guardar_en_archivo("registro_alumnos.txt")
    print("Los datos han sido guardados en 'registro_alumnos.txt'.")