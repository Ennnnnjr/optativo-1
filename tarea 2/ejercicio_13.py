# ejercicio 13
class Habitacion:
    def __init__(self, numero: int, tipo: str, tarifa_por_noche: float):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = float(tarifa_por_noche)
        self.ocupada = False

    def ocupar(self) -> bool:
        #Intenta ocupar la habitacion
        if self.ocupada:
            print(f"La habitación {self.numero} ({self.tipo}) ya se encuentra ocupada.")
            return False
        
        self.ocupada = True
        print(f"La habitación {self.numero} ({self.tipo}) ha sido ocupada.")
        return True

    def liberar(self) -> bool:
        #Intenta liberar la habitacion
        if not self.ocupada:
            print(f"La habitación {self.numero} ({self.tipo}) ya está libre.")
            return False
        
        self.ocupada = False
        print(f"La habitación {self.numero} ({self.tipo}) ha sido liberada.")
        return True

    def calcular_costo_estadia(self, noches: int) -> float:
        #Calcula el costo total
        if noches <= 0:
            print("La cantidad de noches debe ser mayor a 0.")
            return 0.0
        
        return self.tarifa_por_noche * noches

    def mostrar_estado(self):
        estado_str = "OCUPADA" if self.ocupada else "LIBRE"
        print(f"Habitación {self.numero:<4} | Tipo: {self.tipo:<12} | Tarifa/noche: ${self.tarifa_por_noche:>8.2f} | Estado: {estado_str}")


# ejemplo
if __name__ == "__main__":
    print("        SISTEMA DE GESTION")
    print("=" * 65 + "\n")

    # Creamos una habitacion
    hab_201 = Habitacion(numero=201, tipo="Suite", tarifa_por_noche=85.0)

    # Estado inicial
    print("--- estado ---")
    hab_201.mostrar_estado()
    print()

    # Ocupar la habitacion
    print("--- Registro  ---")
    hab_201.ocupar()
    hab_201.mostrar_estado()
    print()

    # Intento de re-ocupar 
    print("--- validacion ---")
    hab_201.ocupar()
    print()

    # Calcular el costo de estadia 
    noches_estadia = 4
    costo_total = hab_201.calcular_costo_estadia(noches_estadia)
    
    print("---  costo de estadia ---")
    print(f"Noches de hospedaje : {noches_estadia}")
    print(f"Tarifa por noche    : ${hab_201.tarifa_por_noche:.2f}")
    print(f"Total a pagar      : ${costo_total:.2f}")
    print()

    # Liberar la habitacion
    print("--- Registro de check-out ---")
    hab_201.liberar()
    hab_201.mostrar_estado()
    print()

    # Validación de estado
    print("--- (Validacion) ---")
    hab_201.liberar()