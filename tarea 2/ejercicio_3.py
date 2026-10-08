# ejercicio 3
class Empleado:
    def __init__(self, nombre: str, cargo: str, salario_mensual: float):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self, incluir_aguinaldo: bool = True) -> float:
        # Calcula el salario anual del empleado.
        meses = 13 if incluir_aguinaldo else 12
        # que seria simplemente el salario por los meses
        return self.salario_mensual * meses

    def __str__(self) -> str:
        
        salario_anual = self.calcular_salario_anual(incluir_aguinaldo=True)
        return (
            f"Ficha de Empleado:\n"
            f"  - Nombre: {self.nombre}\n"
            f"  - Cargo: {self.cargo}\n"
            f"  - Salario Mensual: ₲ {self.salario_mensual:,.0f}\n"
            f"  - Salario Anual (con aguinaldo): ₲ {salario_anual:,.0f}"
        )


# He imprimimos los resultados
if __name__ == "__main__":
    # ponemos unos empleados
    emp1 = Empleado("Maria Gonzalez", "Desarrolladora Senior", 8500000)
    emp2 = Empleado("Andy Gamarra", "Analista de Datos", 5200000)

    # Imprimimos la información legible utilizando el método __str__
    print(emp1)
    print()
    print(emp2)

    # y le agregamos el aguinaldo a uno y al otro no 
    anual_sin_aguinaldo = emp1.calcular_salario_anual(incluir_aguinaldo=False)
    anual_con_aguinaldo = emp1.calcular_salario_anual(incluir_aguinaldo=True)

    print("\n--- Comparativa de sueldo ---")
    print(f"Salario anual base (12 meses): ₲ {anual_sin_aguinaldo:,.0f}")
    print(f"Salario anual real (13 meses): ₲ {anual_con_aguinaldo:,.0f}")