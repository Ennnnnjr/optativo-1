# ejercicio 5
class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def descripcion_comercial(self):
        return f"{self.marca} {self.modelo} {self.anio} — {self.precio:,.0f} Gs.".replace(",", ".")


# dos vehiculos
vehiculo_1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
vehiculo_2 = Vehiculo("Hyundai", "HB20", 2022, 82000000)

# y los resultados en pantalla
print(vehiculo_1.descripcion_comercial())
print(vehiculo_2.descripcion_comercial())