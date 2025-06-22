class Categoria:
    def __init__(self, nombre, descuento):
        self.nombre = nombre
        self.descuento = descuento

    def obtenerDescuento(self):
        return self.descuento


class Producto:
    def __init__(self, nombre: str, categoria: Categoria):
        self.nombre = nombre
        self.categoria = categoria

    def calcular_descuento(self):
        print(
            f"Descuento del {self.categoria.obtenerDescuento() * 100}% en {self.nombre}")


class Carrito:
    def __init__(self, productos: list):
        self.productos = productos

    def calcular_descuentos(self):
        for producto in self.productos:
            producto.calcular_descuento()


# Añadir más condiciones para nuevos tipos de productos y descuentos
alimentos = Categoria("alimentos", 0.1)
limpieza = Categoria("limpieza", 0.05)
productos = [
    Producto('manzanas', alimentos),
    Producto('jabón', limpieza)
]
carrito = Carrito(productos)
carrito.calcular_descuentos()
