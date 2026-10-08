# ejercicio 8
class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"'{self.titulo}' - {self.artista} ({minutos}:{segundos:02d})"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []  # Colección interna de objetos Cancion

    def agregar_cancion(self, cancion):
        """Añade un objeto Cancion a la lista."""
        self.canciones.append(cancion)

    def obtener_duracion_total(self):
        """Recorre la colección y suma la duración total en segundos."""
        total_segundos = 0
        for cancion in self.canciones:
            total_segundos += cancion.duracion_segundos
        return total_segundos

    def mostrar_lista(self):
        """Muestra cada canción y la duración total al final."""
        print(f"--- Lista de Reproducción: {self.nombre} ---")
        if not self.canciones:
            print("La lista está vacía.")
            return

        for i, cancion in enumerate(self.canciones, start=1):
            print(f"{i}. {cancion}")

        total_seg = self.obtener_duracion_total()
        minutos = total_seg // 60
        segundos = total_seg % 60
        print("-" * 40)
        print(f"Duracion total: {minutos} min {segundos:02d} seg ({total_seg} segundos)")


# Ejemplo 
cancion1 = Cancion("Bohemian Rhapsody", "Queen", 354)
cancion2 = Cancion("Hotel California", "Eagles", 391)
cancion3 = Cancion("Billie Jean", "Michael Jackson", 294)

mi_playlist = ListaReproduccion("Mis Favoritas")
mi_playlist.agregar_cancion(cancion1)
mi_playlist.agregar_cancion(cancion2)
mi_playlist.agregar_cancion(cancion3)

mi_playlist.mostrar_lista()