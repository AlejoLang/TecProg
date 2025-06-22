from typing import List
import datetime
from Tarjetas import TarjetaCredito, Uala, MercadoPago
from Reservas import Unidad, Asiento, Pasajero


class Reserva:
    def __init__(self, num_servicio: int, cliente: Pasajero, fecha_reserva: datetime.datetime, num_asiento: int):
        self.num_servicio = num_servicio
        self.cliente = cliente
        self.fecha_reserva = fecha_reserva
        self.num_asiento = num_asiento

    def obtener_num_servicio(self):
        return self.num_servicio

    def obtener_cliente(self):
        return self.cliente

    def obtener_fecha_reserva(self):
        return self.fecha_reserva

    def obtener_num_asiento(self):
        return self.num_asiento


class Ciudad:

    def __init__(self, nombre: str, codigo: str, provincia: str):
        self.nombre = nombre
        self.codigo = codigo
        self.provincia = provincia

    def obtener_nombre(self):
        return self.nombre

    def obtener_codigo(self):
        return self.codigo

    def obtener_provincia(self):
        return self.provincia


class Itinerario:
    def __init__(self, origen: Ciudad, destino: Ciudad, paradas_intermedias: List[Ciudad] = None):
        self.origen = origen
        self.destino = destino
        self.paradas_intermedias = paradas_intermedias if paradas_intermedias else []

    def obtener_origen(self):
        return self.origen

    def obtener_destino(self):
        return self.destino

    def obtener_paradas_intermedias(self):
        return self.paradas_intermedias


class Servicio:
    def __init__(self, unidad: Unidad, precio: float, calidad: str, fecha_partida: datetime.datetime, fecha_llegada: datetime.datetime, itinerario: Itinerario):
        self.unidad = unidad
        self.precio = precio
        self.calidad = calidad
        self.fecha_partida = fecha_partida
        self.fecha_llegada = fecha_llegada
        self.itinerario = itinerario
        self.reservas: List[Reserva] = []

    def obtener_asientos(self):
        return self.unidad.obtener_asientos()

    def obtener_origen(self):
        return self.itinerario.obtener_origen()

    def obtener_destino(self):
        return self.itinerario.obtener_destino()

    def obtener_fecha_partida(self):
        return self.fecha_partida

    def obtener_paradas_intermedias(self):
        return self.itinerario.obtener_paradas_intermedias()

    def consultar_disponibilidad(self, num_asiento: int) -> bool:
        return self.unidad.obtener_disponibilidad_asiento(num_asiento)

    def reservar_asiento(self, num_asiento: int):
        return self.unidad.reservar(num_asiento)

    def agregar_reserva(self, reserva: Reserva):
        self.reservas.append(reserva)


class ArgenTour:
    def __init__(self):
        self.sistema_activo: bool = True
        self.itinerarios: List[Itinerario] = []
        self.servicios: List[Servicio] = []
        self.ciudades: List[Ciudad] = []
        self.unidades: List[Unidad] = []

    def crear_itinerario(self, origen: Ciudad, destino: Ciudad, paradas_intermedias: List[Ciudad] = None):
        nuevo_itinerario = Itinerario(origen, destino, paradas_intermedias)
        self.itinerarios.append(nuevo_itinerario)

    def crear_servicio(self, unidad: Unidad, precio: float, calidad: str, fecha_partida: datetime.datetime, fecha_llegada: datetime.datetime, itinerario: Itinerario):
        nuevo_servicio = Servicio(unidad, precio, calidad,
                                  fecha_partida, fecha_llegada, itinerario)
        self.servicios.append(nuevo_servicio)

    def generar_reporte(self, fecha_incio: datetime.datetime, fecha_fin: datetime.datetime):
        totalFacturado = 0
        cantidad_por_destino = {}
        cantidad_medio_pago = {}

        ventasEnRango = [
            venta for venta in self.ventas if fecha_incio <= venta.fecha <= fecha_fin]

        for venta in ventasEnRango:
            totalFacturado += venta.obtener_precio()
            destino = venta.obner_destino()
            medio_pago = venta.obtener_medio_pago()
            cantidad_por_destino[destino] = cantidad_por_destino.get(
                destino, 0) + 1
            cantidad_medio_pago[medio_pago] = cantidad_medio_pago.get(
                medio_pago, 0) + 1

        print(f"Total facturado: {totalFacturado}")
        print("Cantidad de ventas por destino:")
        for destino, cantidad in cantidad_por_destino.items():
            print(f"{destino}: {cantidad}")
        print("Cantidad de ventas por medio de pago:")
        for medio_pago, cantidad in cantidad_medio_pago.items():
            print(f"{medio_pago}: {cantidad}")

    def crear_reserva(self, num_servicio: int, cliente: Pasajero, fecha_reserva: datetime.datetime, num_asiento: int) -> bool:
        if not self.servicios[num_servicio].consultar_disponibilidad(num_asiento):
            return False
        nueva_reserva = Reserva(num_servicio, cliente,
                                fecha_reserva, num_asiento)
        self.servicios[num_servicio].reservar_asiento(num_asiento)
        self.servicios[num_servicio].agregar_reserva(nueva_reserva)
        return True

    def obtener_itinerarios(self):
        return self.itinerarios

    def obtener_servicio(self, num_servicio: int):
        return self.servicios[num_servicio]


sistema = ArgenTour()
u1 = Unidad("ABC123", 50)
u2 = Unidad("DEF456", 50)
c1 = Ciudad("Buenos Aires", "BA", "Buenos Aires")
c2 = Ciudad("Córdoba", "CD", "Córdoba")
c3 = Ciudad("Mendoza", "MZ", "Mendoza")
c4 = Ciudad("Salta", "SLT", "Salta")
c5 = Ciudad("San Luis", "SL", "San Luis")
c6 = Ciudad("Rosario", "RS", "Santa Fe")
sistema.crear_itinerario(c1, c2, [c6])
sistema.crear_itinerario(c2, c3, [c5])
sistema.crear_itinerario(c3, c4)
its = sistema.obtener_itinerarios()
sistema.crear_servicio(
    u1, 1000, "Económico", datetime.datetime(2023, 10, 1, 10, 0),
    datetime.datetime(2023, 10, 1, 12, 0), its[0])
sistema.crear_servicio(
    u2, 1500, "Premium", datetime.datetime(2023, 10, 2, 10, 0),
    datetime.datetime(2023, 10, 2, 12, 0), its[1])


def menu():
    print("Menu principal")
    print("1. Listar servicios")
    print("2. Crear reserva")
    print("Seleccionar una opcion: ")
    opcion = input()
    if opcion == "1":
        listar_servicios()
    elif opcion == "2":
        crear_reserva()
    else:
        print("Opcion no valida")
        menu()
    menu()


def listar_servicios():
    print("Servicios disponibles:")
    it = 0
    for servicio in sistema.servicios:
        print(f"Servicio: {it+1}")
        print("Itinerario:")
        print(f"\tOrigen: {servicio.obtener_origen().obtener_nombre()}")
        print("\tParadas intermedias:")
        for parada in servicio.obtener_paradas_intermedias():
            print(f"\t\t- {parada.obtener_nombre()}")
        print(f"\tDestino: {servicio.obtener_destino().obtener_nombre()}")
        print(f"Calidad: {servicio.calidad}")
        print(f"Precio: {servicio.precio}")
        print(f"Fecha de partida: {servicio.fecha_partida}")
        print(f"Fecha de llegada: {servicio.fecha_llegada}")
        it += 1
        print("-" * 20)
    menu()


def crear_reserva():
    print("Crear reserva")
    num_servicio = int(
        input("Ingrese el numero de servicio (0 para menu): ")) - 1
    if num_servicio == -1:
        return
    servicio = sistema.obtener_servicio(num_servicio)

    print("Asientos libres: ", end="")
    for asiento in servicio.obtener_asientos():
        if (not asiento.esta_ocupado()):
            print(asiento.numero, end=", ")
    print(" / Ocupados: ", end="")
    for asiento in servicio.obtener_asientos():
        if asiento.esta_ocupado():
            print(asiento.numero, end=", ")
    print()

    num_asiento = int(input("Ingrese el numero de asiento: "))
    if not servicio.consultar_disponibilidad(num_asiento):
        print("El asiento no esta disponible")
        return

    nombre_pasajero = input("Ingrese el nombre del pasajero: ")
    email_pasajero = input("Ingrese el email del pasajero: ")
    dni_pasajero = input("Ingrese el dni del pasajero: ")

    print("Ingrese la fecha de reserva (YYYY-MM-DD): ")
    fecha_reserva = datetime.datetime.today()
    cliente = Pasajero(nombre_pasajero, email_pasajero, dni_pasajero)
    if sistema.crear_reserva(num_servicio, cliente, fecha_reserva, num_asiento):
        print(
            f"Reserva realizada: Pasajero {nombre_pasajero}, Asiento {num_asiento}, Fecha de reserva {fecha_reserva}")
    else:
        print("No se pudo crear la reserva")
    crear_reserva()


def main():
    print("Sistema de reservas ArgenTour")
    menu()


if __name__ == "__main__":
    main()
