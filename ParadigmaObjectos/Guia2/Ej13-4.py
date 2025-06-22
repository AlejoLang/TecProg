class Dispositivo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def contar_piezas_dispositivo(self):
        pass


class Celular(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla

    def contar_piezas_dispositivo(self):
        return "Piezas requeridas para reparar el celular"


class Tablet(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, lapiz: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
        self.lapiz = lapiz

    def contar_piezas_dispositivo(self):
        return "Piezas requeridas para reparar la tablet"


class Smartwatch(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, gps: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
        self.gps = gps

    def contar_piezas_dispositivo(self):

        return "Piezas requeridas para reparar el smartwatch"


def contar_piezas_reparacion(dispositivos: list):
    for dispositivo in dispositivos:
        print(dispositivo.contar_piezas_dispositivo())

# Funciones para contar piezas de repuesto específicas para cada tipo de dispositivo


# Ejemplo de uso
dispositivos = [
    Celular("Samsung", "Galaxy S20", True),
    Tablet("Apple", "iPad Pro", True, True),
    Smartwatch("Apple", "Watch Series 6", True, True)
]
contar_piezas_reparacion(dispositivos)
