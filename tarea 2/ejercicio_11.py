# ejercicio 11
class Estudiante:
    def __init__(self, nombre: str, nota_minima_aprobacion: float = 6.0):
        self.nombre = nombre
        self.nota_minima_aprobacion = nota_minima_aprobacion
        # Diccionario para almacenar 'Materia': Nota
        self.notas = {}

    def registrar_nota(self, materia: str, nota: float):
        """Registra o actualiza la nota de una materia (validando que esté entre 0 y 10)."""
        if 0 <= nota <= 10:
            self.notas[materia] = nota
        else:
            print(f"Error: La nota {nota} para '{materia}' no es válida (debe estar entre 0 y 10).")

    def calcular_promedio(self) -> float:
        """Calcula el promedio general de las notas cargadas."""
        if not self.notas:
            return 0.0
        return sum(self.notas.values()) / len(self.notas)

    def esta_aprobado(self) -> bool:
        """Determina si el estudiante aprobó considerando el promedio general."""
        if not self.notas:
            return False
        return self.calcular_promedio() >= self.nota_minima_aprobacion

    def obtener_condicion_final(self) -> str:
        """Devuelve el estado académico final."""
        if not self.notas:
            return "Sin Evaluaciones"
        return "APROBADO" if self.esta_aprobado() else "REPROBADO"

    def mostrar_boletin(self):
        """Imprime el boletín oficial con el desglose de materias, promedio y estado."""
        print("\n" + "=" * 45)
        print(f"         boletin academico: {self.nombre.upper()}")
        print("=" * 45)
        print(f"{'Materia':<30} | {'Nota':<8}")


        if not self.notas:
            print(" No hay notas registradas para este estudiante.")
        else:
            for materia, nota in self.notas.items():
                print(f"{materia:<30} | {nota:>6.2f}")

        promedio = self.calcular_promedio()
        condicion = self.obtener_condicion_final()

        print("-" * 45)
        print(f"{'PROMEDIO GENERAL:':<30} | {promedio:>6.2f}")
        print(f"{'CONDICIÓN FINAL:':<30} | {condicion:>8}")



# ejemplo
if __name__ == "__main__":
    # Crear un estudiante
    estudiante1 = Estudiante("Sofía Benítez", nota_minima_aprobacion=6.0)

    # notas
    estudiante1.registrar_nota("Matemáticas", 8.5)
    estudiante1.registrar_nota("Historia", 5.0)
    estudiante1.registrar_nota("Programación", 9.0)
    estudiante1.registrar_nota("Física", 7.0)

    # boletin
    estudiante1.mostrar_boletin()

    # ejemplo de aprobado
    estudiante2 = Estudiante("Lucas Gómez", nota_minima_aprobacion=6.0)
    estudiante2.registrar_nota("Matemáticas", 4.0)
    estudiante2.registrar_nota("Historia", 5.5)
    estudiante2.registrar_nota("Programación", 5.0)

    estudiante2.mostrar_boletin()