from enum import Enum
import datetime


class EstadoVehiculo(Enum):
    USADO = "Usado"
    NUEVO = "Nuevo"


class Cliente:
    def __init__(self,
                 nombre: str,
                 apellido: str,
                 telefono: str,
                 dni: str):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.dni = dni


class Vehiculo:
    def __init__(self,
                 marca: str,
                 modelo: str,
                 patente: str,
                 precio: float,
                 kilometraje: float,
                 estado: EstadoVehiculo,
                 duenio: Cliente = None):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.precioVenta = precio
        self.kilometraje = kilometraje
        self.estado = estado
        self.duenioAnterior = duenio

    def obtenerEstado(self): return self.estado
    def esImportado(self): return False


class VehiculoNacional(Vehiculo):
    def __init__(self, marca, modelo, patente, precio, kilometraje, estado, duenio=None):
        super().__init__(marca, modelo, patente, precio, kilometraje, estado, duenio)


class VehiculoImportado(Vehiculo):
    def __init__(self,
                 marca: str,
                 modelo: str,
                 patente: str,
                 precio: float,
                 kilometraje: float,
                 pais: str,
                 costoImp: str,
                 estado: EstadoVehiculo,
                 duenio: Cliente = None):
        super().__init__(marca, modelo, patente, precio, kilometraje, estado, duenio)
        self.pais = pais
        self.costoImportacion = costoImp

    def esImportado(self): return True


class Venta:
    def __init__(self,
                 comprador: Cliente,
                 vehiculo: Vehiculo,
                 monto: float,
                 fecha: datetime.date = datetime.date.today()):
        self.fecha = fecha,
        self.vehiculo = vehiculo
        self.comprador = comprador
        self.monto = monto

    def obtenerMonto(self) -> float: return self.monto
    def obtenerVehiculo(self) -> Vehiculo: return self.vehiculo


class Consecionaria:
    def __init__(self):
        self.ventas = []

    def agregarVenta(self, venta: Venta): self.ventas.append(venta)

    def totalNacionalesUsados(self):
        total = 0
        for venta in self.ventas:
            print(venta.obtenerVehiculo().esImportado())
            if (not venta.obtenerVehiculo().esImportado() and venta.obtenerVehiculo().obtenerEstado() == EstadoVehiculo.USADO):
                total += venta.obtenerMonto()
        return total


vehiculos = []
forFocus = VehiculoNacional("Ford Focus", "2011", "asd123", 123123123, 213,
                            EstadoVehiculo.USADO, Cliente("Pepe", "Monzon", "1231231", "54444442"))
cons = Consecionaria()
cons.agregarVenta(
    Venta(Cliente("Juan", "Carlos", "3545", "123333"), forFocus, 123333))
print(cons.totalNacionalesUsados())
