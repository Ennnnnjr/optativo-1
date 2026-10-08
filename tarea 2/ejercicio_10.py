# ejercicio 10
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio:.2f})"


class Item:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self) -> float:
        """Calcula el costo total para este ítem específico (precio * cantidad)."""
        return self.producto.precio * self.cantidad


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, producto: Producto, cantidad: int = 1):
        """Agrega un ítem al carrito. Si el producto ya existe, incrementa la cantidad."""
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        # Verificar si el producto ya está en el carrito para consolidarlo
        for item in self.items:
            if item.producto.nombre.lower() == producto.nombre.lower():
                item.cantidad += cantidad
                return

        # Si no existe, se crea un nuevo Item
        nuevo_item = Item(producto, cantidad)
        self.items.append(nuevo_item)

    def calcular_total(self) -> float:
        """Calcula el costo total sumando el subtotal de cada ítem."""
        return sum(item.calcular_subtotal() for item in self.items)

    def mostrar_detalle(self):
        """Muestra el desglose de cada producto, subtotal y el total general."""
        if not self.items:
            print("El carrito está vacío.")
            return
        #resulta que puedes multiplicar asi evitas un for n=i
        print("\n" + "=" * 45)
        print("DETALLE DE COMPRA")
        print("=" * 45)
        print(f"{'Producto':<20} | {'Cant.':<6} | {'Subtotal':<10}")
        print("-" * 45)

        for item in self.items:
            nombre = item.producto.nombre
            cant = item.cantidad
            subtotal = item.calcular_subtotal()
            print(f"{nombre:<20} | {cant:<6} | ${subtotal:>8.2f}")

        print("-" * 45)
        print(f"{'TOTAL A PAGAR:':<29} | ${self.calcular_total():>8.2f}")
        print("=" * 45 + "\n")


# ejemplo
if __name__ == "__main__":
    # creamos algunos productos
    p1 = Producto("Teclado Mecánico", 45000.0)
    p2 = Producto("Mouse Inalámbrico", 22000.50)
    p3 = Producto("Monitor 24 inch", 155000.0)

    # el carrito
    mi_carrito = Carrito()

    # agregamos al carrito
    mi_carrito.agregar_item(p1, cantidad=2)
    mi_carrito.agregar_item(p2, cantidad=1)
    mi_carrito.agregar_item(p3, cantidad=1)

    # Agregamos de nuevo 
    mi_carrito.agregar_item(p2, cantidad=2)

    # y el resumen
    mi_carrito.mostrar_detalle()