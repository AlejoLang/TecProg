from abc import ABC, abstractmethod
from typing import List
import datetime
from datetime import timedelta
import threading


class Argentur:
    pass


class Servicio:
    pass


class Itinerario:
    pass


class Ciudad:
    pass


class Reserva:
    pass


class Unidad:
    pass


class Asiento:
    pass


class Pasajero:
    pass


class Venta:
    pass


class MedioPago(ABC):
    pass


class TarjetaCredito(MedioPago):
    pass


class MercadoPago(MedioPago):
    pass


class Uala(MedioPago):
    pass


class Argentur:
    def __init__(self):
        self.sistema_activo: bool = True
        self.itinerarios: List[Itinerario] = []
        self.servicios: List[Servicio] = []
        self.ciudades: List[Ciudad] = []
        self.unidades: List[Unidad] = []
        self.ventas: List[Venta] = []

    def crear_itinerario(self, origen: Ciudad, destino: Ciudad, paradas_intermedias: List[Ciudad] = None):
        nuevo_itinerario = Itinerario(origen, destino, paradas_intermedias)
        self.itinerarios.append(nuevo_itinerario)

    def crear_servicio(self, num_servicio: int, unidad: Unidad, precio: float, calidad: str, fecha_partida: datetime.datetime, fecha_llegada: datetime.datetime, itinerario: Itinerario):
        nuevo_servicio = Servicio(
            num_servicio, unidad, precio, calidad, fecha_partida, fecha_llegada, itinerario)
        self.servicios.append(nuevo_servicio)

    def crear_reserva(self, num_servicio: int, cliente: Pasajero, fecha_reserva: datetime.datetime, num_asiento: int) -> bool:
        # Retorna la reserva creada o None si no se pudo crear
        servicio = self.obtener_servicio(num_servicio)
        if servicio is None:
            return None
        return servicio.crear_reserva(cliente, fecha_reserva, num_asiento)

    def crear_venta(self, servicio: Servicio, pasajero: Pasajero, num_asiento: int, medio_pago: MedioPago):
        # Verifica si ya existe una venta para el servicio y el asiento
        for venta in self.ventas:
            if venta.obtener_num_servicio() == servicio and venta.obtener_asiento() == num_asiento:
                return None
        fecha_venta = datetime.datetime.today()
        print(medio_pago.validar_tarjeta())
        # Cancela la reserva del asiento
        servicio.cancelar_reserva(num_asiento)
        # Crea la venta y reserva el asiento
        venta = Venta(servicio, pasajero, num_asiento, medio_pago, fecha_venta)
        self.ventas.append(venta)
        servicio.reservar_asiento(num_asiento)
        return Venta

    def generar_reporte(self, fecha_incio: datetime.datetime, fecha_fin: datetime.datetime):
        totalFacturado = 0
        cantidad_por_destino = {}
        cantidad_medio_pago = {}
        # Filtra las ventas por fecha
        ventasEnRango = [
            venta for venta in self.ventas if fecha_incio <= venta.obtener_fecha() <= fecha_fin]
        # Cuenta las ventas por destino y medio de pago mediante un diccionario
        for venta in ventasEnRango:
            totalFacturado += venta.obtener_precio()
            destino = venta.obtener_destino()
            medio_pago = venta.obtener_medio_pago()
            cantidad_por_destino[destino.obtener_nombre()] = cantidad_por_destino.get(
                destino.obtener_nombre(), 0) + 1
            cantidad_medio_pago[medio_pago.obtener_nombre_medio()] = cantidad_medio_pago.get(
                medio_pago.obtener_nombre_medio(), 0) + 1
        resp = {
            "total": totalFacturado,
            "ventas_destino": cantidad_por_destino,
            "ventas_medio_pago": cantidad_medio_pago
        }
        return resp

    def obtener_itinerarios(self):
        return self.itinerarios

    def obtener_servicios(self):
        return self.servicios

    def obtener_servicio(self, num_servicio: int):
        for servicio in self.servicios:
            if servicio.obtener_num_servicio() == num_servicio:
                return servicio
        return None


class Servicio:
    def __init__(self, num_servicio: int, unidad: Unidad, precio: float, calidad: str, fecha_partida: datetime.datetime, fecha_llegada: datetime.datetime, itinerario: Itinerario):
        self.num_servicio: int = num_servicio
        self.unidad: Unidad = unidad
        self.precio: float = precio
        self.calidad: str = calidad
        self.fecha_partida: datetime.datetime = fecha_partida
        self.fecha_llegada: datetime.datetime = fecha_llegada
        self.itinerario: Itinerario = itinerario
        self.reservas: List[Reserva] = []

        # Se programa la cancelacion de reservas 30 minutos antes de la partida
        self.schedule_cancelar_reservas()

    def crear_reserva(self,  pasajero: Pasajero, fecha_reserva: datetime.datetime, num_asiento: int):
        # Si el asiento esta disponible, lo reserva y crea la reserva retornando el objeto Reserva
        # Si no, retorna None
        if not self.unidad.obtener_disponibilidad_asiento(num_asiento):
            return None
        self.unidad.reservar_asiento(num_asiento)
        nueva_reserva = Reserva(
            self.num_servicio, pasajero, fecha_reserva, num_asiento)
        # reserva necesita pasaje y numAs
        self.reservas.append(nueva_reserva)
        return nueva_reserva

    def reservar_asiento(self, num_asiento: int):
        self.unidad.reservar_asiento(num_asiento)

    def cancelar_reserva(self, num_asiento: int):
        # Cancela la reserva eliminando el objeto Reserva de la lista de reservas y liberando el asiento
        # Si no se encuentra la reserva, retorna False
        # Si se encuentra, retorna True
        for reserva in self.reservas:
            if reserva.obtener_num_asiento() == num_asiento:
                self.unidad.cancelar_reserva(num_asiento)
                self.reservas.remove(reserva)
                return True
        return False

    def schedule_cancelar_reservas(self):
        # Cancela las reservas cuando faltan 30 minutos para la partida
        ahora = datetime.datetime.now()
        delay = (self.fecha_partida - ahora +
                 timedelta(minutes=30)).total_seconds()
        delay = max(0, delay)
        timer = threading.Timer(
            delay, self.cancelar_reservas_pasadas_de_tiempo)
        timer.start()

    def cancelar_reservas_pasadas_de_tiempo(self):
        ahora = datetime.datetime.now()
        if self.fecha_partida - ahora <= timedelta(minutes=30):
            reservas_a_cancelar = self.reservas.copy()
            for reserva in reservas_a_cancelar:
                print(
                    f"Reserva cancelada: {reserva.obtener_pasajero()} - Asiento: {reserva.obtener_num_asiento()}")
                self.cancelar_reserva(reserva.obtener_num_asiento())

    def obtener_num_servicio(self):
        return self.num_servicio

    def obtener_asientos_libres(self):
        return self.unidad.obtener_asientos_libres()

    def obtener_asientos_ocupados(self):
        return self.unidad.obtener_asientos_ocupados()

    def obtener_origen(self):
        return self.itinerario.obtener_origen()

    def obtener_destino(self):
        return self.itinerario.obtener_destino()

    def obtener_fecha_partida(self):
        return self.fecha_partida

    def obtener_fecha_llegada(self):
        return self.fecha_llegada

    def obtener_paradas_intermedias(self):
        return self.itinerario.obtener_paradas_intermedias()

    def consultar_disponibilidad(self, num_asiento: int) -> bool:
        # Retorna True si el asiento esta disponible, False si no
        return self.unidad.obtener_disponibilidad_asiento(num_asiento)

    def obtener_precio(self):
        return self.precio

    def obtener_destino(self):
        return self.itinerario.obtener_destino()

    def obtener_reservas(self):
        return self.reservas


class Itinerario:
    def __init__(self, origen: Ciudad, destino: Ciudad, paradas_intermedias: List[Ciudad] = None):
        self.origen = origen
        self.destino = destino
        self.paradas_intermedias = paradas_intermedias

    def aniadir_ciudad(self, ciudad: Ciudad):
        self.paradas_intermedias.append(ciudad)

    def quitar_ciudad(self, ciudad: Ciudad):
        self.paradas_intermedias.remove(ciudad)

    def obtener_origen(self):
        return self.origen

    def obtener_destino(self):
        return self.destino

    def obtener_paradas_intermedias(self):
        return self.paradas_intermedias


class Ciudad:
    def __init__(self, nombre: str, codigo: str, provincia: str):
        self.codigo = codigo
        self.nombre = nombre
        self.provincia = provincia

    def obtener_nombre(self):
        return self.nombre


class Reserva:
    def __init__(self, num_servicio: int, cliente: Pasajero, fecha_reserva: datetime.datetime, num_asiento: int):
        self.num_servicio = num_servicio
        self.cliente = cliente
        self.fecha_reserva = fecha_reserva
        self.num_asiento = num_asiento

    def obtener_num_asiento(self):
        return self.num_asiento

    def obtener_pasajero(self):
        return self.cliente.obtener_nombre()


class Venta:
    def __init__(self, servicio: Servicio, pasajero: Pasajero, num_asiento: int, medio_pago: MedioPago, fecha_venta: datetime.datetime):
        self.servicio = servicio
        self.pasajero = pasajero
        self.num_asiento = num_asiento
        self.medio_pago = medio_pago
        self.fecha_venta = fecha_venta

    def obtener_fecha(self):
        return self.fecha_venta

    def obtener_medio_pago(self):
        return self.medio_pago

    def obtener_precio(self):
        return self.servicio.obtener_precio()

    def obtener_destino(self):
        return self.servicio.obtener_destino()

    def obtener_num_servicio(self):
        return self.servicio.obtener_num_servicio()

    def obtener_num_asiento(self):
        return self.num_asiento


class Unidad:
    def __init__(self, patente: str, num_asientos: int):
        self.patente = patente
        self.asientos: List[Asiento] = []
        for i in range(num_asientos):
            self.asientos.append(Asiento(i + 1))

    def obtener_asientos_libres(self):
        return [asiento for asiento in self.asientos if not asiento.esta_ocupado()]

    def obtener_asientos_ocupados(self):
        return [asiento for asiento in self.asientos if asiento.esta_ocupado()]

    def obtener_disponibilidad_asiento(self, num_asiento: int):
        # Retorna True si el asiento esta disponible, False si no
        if num_asiento < 1 or num_asiento > len(self.asientos):
            return False
        return not self.asientos[num_asiento - 1].esta_ocupado()

    def reservar_asiento(self, num_asiento: int):
        return self.asientos[num_asiento - 1].establecer_estado(True)

    def cancelar_reserva(self, num_asiento: int):
        return self.asientos[num_asiento - 1].establecer_estado(False)


class Asiento:
    def __init__(self, numero: int):
        self.numero = numero
        self.ocupado = False

    def obtener_numero(self):
        return self.numero

    def establecer_estado(self, estado: bool):
        aux = self.ocupado
        self.ocupado = estado
        return aux != estado

    def esta_ocupado(self):
        return self.ocupado


class Pasajero:
    def __init__(self, nombre: str, email: str, dni: str):
        self.nombre = nombre
        self.email = email
        self.dni = dni

    def obtener_nombre(self):
        return self.nombre


class MedioPago(ABC):
    def __init__(self, nombre):
        self.nombre_medio = nombre

    def obtener_nombre_medio(self):
        return self.nombre_medio

    @abstractmethod
    def validar_tarjeta(self):
        pass


class TarjetaCredito(MedioPago):
    def __init__(self, numero: str, dni_titular: str, nombre: str, fecha_vencimiento: datetime.datetime):
        super().__init__("Tarjeta de credito")
        self.numero = numero
        self.dni_titular = dni_titular
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento

    def validar_tarjeta(self):
        return "Tarjeta de credito validada correctamente"


class MercadoPago(MedioPago):
    def __init__(self, celular: str, email: str):
        super().__init__("Mercado Pago")
        self.celular = celular
        self.email = email

    def validar_tarjeta(self):
        return "Tarjeta de mercado pago validada correctamente"


class Uala(MedioPago):
    def __init__(self, email: str, nombre_titular: str):
        super().__init__("Uala")
        self.email = email
        self.nombre_titular = nombre_titular

    def validar_tarjeta(self):
        return "Tarjeta Uala validada correctamente"

# ------------------------------------------------------------------------------------------------------------------------


sistema: Argentur = Argentur()
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
itinerarios = sistema.obtener_itinerarios()
sistema.crear_servicio(124334, u1, 1000, "Económico", datetime.datetime(
    2023, 10, 1, 10, 0), datetime.datetime(2023, 10, 1, 12, 0), itinerarios[0])
sistema.crear_servicio(2, u2, 1500, "Premium", datetime.datetime(
    2023, 10, 2, 10, 0), datetime.datetime(2023, 10, 2, 12, 0), itinerarios[1])
sistema.crear_servicio(1, u2, 1500, "Premium", datetime.datetime.now(
) - timedelta(minutes=28), datetime.datetime(2023, 10, 2, 12, 0), itinerarios[1])


def menu():
    print("Menu principal")
    print("1. Listar servicios")
    print("2. Crear reserva")
    print("3. Crear venta")
    print("4. Generar informe")
    print("-1. Finalizar programa")
    opcion = int(input("Seleccionar una opcion: "))
    print("-" * 20)
    if opcion == 1:
        listar_servicios()
    elif opcion == 2:
        crear_reserva()
    elif opcion == 3:
        crear_venta()
    elif opcion == 4:
        generar_informe()
    elif opcion == -1:
        return
    else:
        print("Opcion no valida")
        menu()
    menu()


def listar_servicios():
    print("Servicios disponibles:")
    it = 0
    for servicio in sistema.obtener_servicios():
        print(f"Servicio: {servicio.obtener_num_servicio()}")
        print("Itinerario:")
        print(f"\tOrigen: {servicio.obtener_origen().obtener_nombre()}")
        print("\tParadas intermedias:")
        for parada in servicio.obtener_paradas_intermedias():
            print(f"\t\t- {parada.obtener_nombre()}")
        print(f"\tDestino: {servicio.obtener_destino().obtener_nombre()}")
        print(f"Calidad: {servicio.calidad}")
        print(f"Precio: {servicio.precio}")
        print(f"Fecha de partida: {servicio.obtener_fecha_partida()}")
        print(f"Fecha de llegada: {servicio.obtener_fecha_llegada()}")
        it += 1
        print("-" * 20)
    menu()


def crear_reserva():
    print("Crear reserva")
    num_servicio = int(input("Ingrese el numero de servicio (0 para menu): "))
    while sistema.obtener_servicio(num_servicio) is None and num_servicio != 0:
        print("Numero de servicio no valido")
        num_servicio = int(
            input("Ingrese el numero de servicio (0 para menu): "))
    if num_servicio == 0:
        print("-" * 20)
        return
    servicio = sistema.obtener_servicio(num_servicio)
    num_asiento = menu_seleccion_asiento(servicio)
    print(f"Num asiento: {num_asiento}")
    if num_asiento == 0:
        return
    cliente = menu_datos_cliente()
    fecha_reserva = datetime.datetime.today()
    reserva = sistema.crear_reserva(
        servicio.obtener_num_servicio(), cliente, fecha_reserva, num_asiento)
    if reserva != None:
        print(
            f"Reserva realizada: Pasajero {cliente.obtener_nombre()}, Asiento {num_asiento}, Fecha de reserva {fecha_reserva}")
    else:
        print("No se pudo crear la reserva")
    print("-" * 20)
    crear_reserva()


def crear_venta():
    print("Crear venta")
    num_servicio = int(input("Ingrese el numero de servicio (0 para menu): "))
    while sistema.obtener_servicio(num_servicio) is None and num_servicio != 0:
        print("Numero de servicio no valido")
        num_servicio = int(
            input("Ingrese el numero de servicio (0 para menu): "))
    if num_servicio == 0:
        print("-" * 20)
        return
    servicio = sistema.obtener_servicio(num_servicio)
    print("1. Vender asiento reservado")
    print("2. Vender asiento no reservado")
    opc = int(input("Seleccione una opcion: "))
    if opc == 1:
        for reserva in servicio.obtener_reservas():
            print(
                f"Reserva: {reserva.obtener_pasajero()} - Asiento: {reserva.obtener_num_asiento()}")
        num_asiento = int(
            input("Ingrese el numero de asiento (0 para menu): "))
        while num_asiento == 0 or servicio.consultar_disponibilidad(num_asiento):
            if num_asiento == 0:
                print("-" * 20)
                return
            print("El asiento no esta reservado")
            num_asiento = int(
                input("Ingrese el numero de asiento (0 para menu): "))

        cliente = None
        for reserva in servicio.obtener_reservas():
            if reserva.obtener_num_asiento() == num_asiento:
                cliente = reserva.obtener_pasajero()
                break
        if cliente is None:
            print("No se encontro la reserva")
            return
        medio_pago = menu_medio_pago()
        if medio_pago is None:
            print("No se selecciono medio de pago")
            return

        if sistema.crear_venta(servicio, cliente, num_asiento, medio_pago):
            print(
                f"Venta realizada: Pasajero: {reserva.cliente.obtener_nombre()}, Asiento: {num_asiento}, Medio de pago: {medio_pago.obtener_nombre_medio()}")
        else:
            print("No se pudo crear la venta")

    elif opc == 2:
        num_asiento = menu_seleccion_asiento(servicio)
        if num_asiento == 0:
            return
        cliente = menu_datos_cliente()
        if cliente is None:
            return
        medio_pago = menu_medio_pago()
        if medio_pago is None:
            return
        venta = sistema.crear_venta(
            servicio, cliente, num_asiento, medio_pago)
        if venta:
            print(
                f"Venta realizada: Pasajero: {cliente.obtener_nombre()}, Asiento: {num_asiento}, Medio de pago: {medio_pago.obtener_nombre_medio()}")
        else:
            print("No se pudo crear la venta")
    print("-" * 20)
    crear_venta()


def generar_informe():
    print("Generar informe")
    print("Ingrese fecha desde (YYYY-MM-DD): ")
    fecha_desde_str = input()
    fecha_desde = datetime.datetime.strptime(fecha_desde_str, "%Y-%m-%d")
    print("Ingrese fecha hasta (YYYY-MM-DD): ")
    fecha_hasta_str = input()
    fecha_hasta = datetime.datetime.strptime(fecha_hasta_str, "%Y-%m-%d")

    print("-" * 20)
    resp = sistema.generar_reporte(fecha_desde, fecha_hasta)

    print(f"Total facturado: {resp.get('total')}")
    print("Cantidad de ventas por destino:")
    for destino, cantidad in resp.get("ventas_destino").items():
        print(f"{destino}: {cantidad}")
    print("Cantidad de ventas por medio de pago:")
    for medio_pago, cantidad in resp.get("ventas_medio_pago").items():
        print(f"{medio_pago}: {cantidad}")

    print("-" * 20)


def menu_seleccion_asiento(servicio: Servicio) -> int:
    print("Asientos libres: ", end="")
    for asiento in servicio.obtener_asientos_libres():
        print(asiento.numero, end=", ")
    print("\nOcupados: ", end="")
    for asiento in servicio.obtener_asientos_ocupados():
        print(asiento.numero, end=", ")
    print()
    num_asiento = int(
        input("Ingrese el numero de asiento (0 para volver): "))
    if num_asiento == 0:
        return 0
    while not servicio.consultar_disponibilidad(num_asiento):
        if num_asiento == 0:
            return 0

        print("El asiento no esta disponible")
        num_asiento = int(
            input("Ingrese el numero de asiento (0 para volver): "))

    return num_asiento


def menu_datos_cliente() -> Pasajero:
    nombre_pasajero = input("Ingrese el nombre del pasajero: ")
    email_pasajero = input("Ingrese el email del pasajero: ")
    dni_pasajero = input("Ingrese el dni del pasajero: ")

    return Pasajero(nombre_pasajero, email_pasajero, dni_pasajero)


def menu_medio_pago():
    medio_pago_opc = int(
        input("Seleccione medio de pago (1. Tarjeta, 2. MercadoPago, 3. Uala): "))
    if medio_pago_opc == 1:
        numero_tarjeta = input("Ingrese el numero de tarjeta: ")
        dni_titular = input("Ingrese el dni del titular: ")
        nombre_titular = input("Ingrese el nombre del titular: ")
        fecha_vencimiento_str = input(
            "Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
        medio_pago = TarjetaCredito(
            numero_tarjeta, dni_titular, nombre_titular, datetime.datetime.strptime(fecha_vencimiento_str, "%Y-%m-%d"))
    elif medio_pago_opc == 2:
        celular = input("Ingrese el numero de celular: ")
        email = input("Ingrese el email: ")
        medio_pago = MercadoPago(celular, email)
    elif medio_pago_opc == 3:
        email = input("Ingrese el email: ")
        nombre_titular = input("Ingrese el nombre del titular: ")
        medio_pago = Uala(email, nombre_titular)
    else:
        print("Opcion no valida")
        return None
    return medio_pago


def main():
    print("Sistema de reservas ArgenTour")
    menu()


main()
