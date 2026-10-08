# ejercicio 4
class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: '{self.titulo}' | Autor: {self.autor} | Estado: {estado}"


# Ejemplo 
libro_1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", disponible=True)
libro_2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", disponible=False)

print(libro_1)
print(libro_2)
