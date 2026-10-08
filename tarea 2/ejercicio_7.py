# ejercicio 6
class CuentaComercio:
    def __init__(self, cliente: str, saldo_inicial: float = 0.0):
        self.cliente = cliente
        self.saldo = max(0.0, float(saldo_inicial))

    def acreditar(self, monto: float) -> None:

        if monto <= 0:
            print(f"Error: El monto debe ser positivo (${monto:.2f} no es válido).")
            return
        
        self.saldo += monto
        print(f"Acreditacion exitosa: +${monto:.2f}. Saldo actual: ${self.saldo:.2f}")

    def registrar_consumo(self, monto: float) -> bool:

        if monto <= 0:
            print(f"Error: El monto debe ser positivo (${monto:.2f} no es válido).")
            return False

        if monto > self.saldo:
            print(f"Aviso: Saldo insuficiente para realizar el consumo de ${monto:.2f}. Saldo disponible: ${self.saldo:.2f}")
            return False

        self.saldo -= monto
        print(f"Consumo realizado: -${monto:.2f}. Saldo actual: ${self.saldo:.2f}")
        return True

    def __str__(self) -> str:
        return f"Cliente: {self.cliente} | Saldo: ${self.saldo:.2f}"


# ejemplo

if __name__ == "__main__":
    print("=== CUENTA CORRIENTE ===\n")
    
    # Creacion de la cuenta
    cuenta = CuentaComercio("María Pérez")
    print(f"Estado inicial -> {cuenta}\n")

    # Intento de acreditar monto inválido
    cuenta.acreditar(-50.0)
    print(f"Estado -> {cuenta}\n")

    # Carga exitosa de saldo
    print("Acreditación de saldo ($1000.00):")
    cuenta.acreditar(1000.0)
    print(f"Estado -> {cuenta}\n")

    # Consumo válido
    print("Compra ($450.50):")
    cuenta.registrar_consumo(450.50)
    print(f"Estado -> {cuenta}\n")

    # Compra rechazada por falta de fondos
    print(" Intento de compra superior al saldo disponible ($700.00):")
    cuenta.registrar_consumo(700.0)
    print(f"Estado -> {cuenta}\n")

    # Segunda acreditación y consumo posterior
    print(" Nueva acreditación de saldo ($500.00):")
    cuenta.acreditar(500.0)
    print(f"Estado -> {cuenta}\n")

    print(" Reintento de la compra anterior ($700.00):")
    cuenta.registrar_consumo(700.0)
    print(f"Estado final -> {cuenta}\n")

    print("=== BYEBYE ===")