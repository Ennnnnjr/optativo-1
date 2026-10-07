<<<<<<< HEAD
# ejercicio 1
class Cliente:
    def __init__(self, nombre, cedula, telefono):
        # El constructor inicializa los datos personales básicos
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def mostrar_ficha(self):
        # Muestra la ficha completa del cliente en pantalla
        print("=== FICHA DEL CLIENTE ===")
        print(f"Nombre:   {self.nombre}")
        print(f"Cédula:   {self.cedula}")
        print(f"Teléfono: {self.telefono}")
        print("=========================\n")


# ejecucion

# Creamos un par de clientes
cliente1 = Cliente("Ana Campos", "4567890", "0981-123456")
cliente2 = Cliente("Andy Gamarra", "3456789", "0971-000000")

# y mostramos sus fichas
cliente1.mostrar_ficha()
=======
# ejercicio 1
class Cliente:
    def __init__(self, nombre, cedula, telefono):
        # El constructor inicializa los datos personales básicos
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def mostrar_ficha(self):
        # Muestra la ficha completa del cliente en pantalla
        print("=== FICHA DEL CLIENTE ===")
        print(f"Nombre:   {self.nombre}")
        print(f"Cédula:   {self.cedula}")
        print(f"Teléfono: {self.telefono}")
        print("=========================\n")


# ejecucion

# Creamos un par de clientes
cliente1 = Cliente("Ana Campos", "4567890", "0981-123456")
cliente2 = Cliente("Andy Gamarra", "3456789", "0971-000000")

# y mostramos sus fichas
cliente1.mostrar_ficha()
>>>>>>> 00583a4029b3081992e5472579e79a94f7f6a18e
cliente2.mostrar_ficha()