# ejercicio 12
class LineaTelefonica:
    def __init__(self, cliente: str, gb_plan: float):
        self.cliente = cliente
        self.gb_plan = float(gb_plan)
        self.gb_consumidos = 0.0

    def registrar_consumo(self, gb: float):
        """Registra el consumo de gigabytes verificando la disponibilidad del plan."""
        if gb <= 0:
            print("El consumo registrado debe ser mayor a 0 GB")
            return

        if self.gb_consumidos >= self.gb_plan:
            print(f"aviso: {self.cliente}: El paquete de datos ya se encuentra agotado")
            return

        gb_disponibles = self.obtener_gb_disponibles()

        if gb > gb_disponibles:
            # Se consume solo lo que resta del paquete
            self.gb_consumidos = self.gb_plan
            excedente = gb - gb_disponibles
            print(
                f"Aviso: {self.cliente}: Se consumieron los últimos {gb_disponibles:.2f} GB. "
                f"El paquete se ha agotado (intento de exceso: {excedente:.2f} GB)."
            )
        else:
            self.gb_consumidos += gb
            print(
                f" consumo {self.cliente}: Consumidos {gb:.2f} GB. "
                f"Quedan disponibles {self.obtener_gb_disponibles():.2f} GB."
            )

    def obtener_gb_disponibles(self) -> float:
        """Calcula los gigabytes restantes del plan."""
        disponible = self.gb_plan - self.gb_consumidos
        return max(0.0, disponible)

    def mostrar_estado(self):
        """Muestra el estado detallado de la línea telefónica."""
        porcentaje_usado = (self.gb_consumidos / self.gb_plan) * 100 if self.gb_plan > 0 else 100
        

        print(f"       ESTADO DE LA LÍNEA - {self.cliente.upper()}")
        print("=" * 50)
        print(f"{'GB Contratados:':<30} | {self.gb_plan:>8.2f} GB")
        print(f"{'GB Consumidos:':<30} | {self.gb_consumidos:>8.2f} GB")
        print(f"{'GB Disponibles:':<30} | {self.obtener_gb_disponibles():>8.2f} GB")
        print(f"{'Uso del paquete:':<30} | {porcentaje_usado:>7.1f} %")

        
        if self.obtener_gb_disponibles() == 0:
            print("paquete agotado")
        else:
            print("estado: activo")



# ejemplo
if __name__ == "__main__":
    # linea de 10gb
    linea_juan = LineaTelefonica(cliente="Juan Pérez", gb_plan=10.0)

    # consulta el estado
    linea_juan.mostrar_estado()

    # registro de consumo
    linea_juan.registrar_consumo(3.5)
    linea_juan.registrar_consumo(4.0)

    # Intentar consumir más de lo que queda disponible
    linea_juan.registrar_consumo(5.0)

    # Intentar consumir teniendo el paquete ya agotado
    linea_juan.registrar_consumo(1.0)

    # Ver el reporte final 
    linea_juan.mostrar_estado()