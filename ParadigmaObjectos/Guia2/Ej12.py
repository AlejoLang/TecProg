from typing import List
import datetime
from enum import Enum

MIN_DATE = datetime.date(datetime.MINYEAR)
MAX_DATE = datetime.date.today()


class Moneda(Enum):
    PESO = "Pesos"
    DOLAR = "Dolares"
    REAL = "Reales"


class Monto:
    def __init__(self, moneda: Moneda, cantidad):
        self.__moneda: Moneda = moneda
        self.__cantidad = cantidad


class Titular:
    def __init__(self, nombre, apellido, cuil):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cuil = cuil


class Transaccion:
    def __init__(self, fecha):
        self.__fecha = fecha

    def obtener_fecha(self):
        return self.__fecha


class TransaccionDeposito(Transaccion):
    def __init__(self, fecha, monto: Monto):
        super().__init__(fecha)
        self.__monto: Monto = monto


class TransaccionExtraccion(Transaccion):
    def __init__(self, fecha, monto: Monto):
        super().__init__(fecha)
        self.__monto: Monto = monto


class TransaccionConsulta(Transaccion):
    def __init__(self, fecha):
        super().__init__(fecha)


class Cuenta:
    def __init__(self, titular: Titular):
        self.__titular: Titular = titular
        self.__transacciones: List[Transaccion] = []

    def obenerCantidadTransacciones(self, periodoInicio: datetime.date = MIN_DATE, periodoFin: datetime.date = MAX_DATE):
        count = 0
        for transaccion in self.__transacciones:
            if transaccion.obtener_fecha() <= periodoFin and transaccion.obtener_fecha() >= periodoInicio:
                count += 1
        return count

    def obtenerTransacciones(self, periodoInicio: datetime.date = MIN_DATE, periodoFin: datetime.date = MAX_DATE):
        transacciones = []
        for transaccion in self.__transacciones:
            if transaccion.obtener_fecha() <= periodoFin and transaccion.obtener_fecha() >= periodoInicio:
                transacciones.append(transaccion)
        return transacciones

    def calcularComision(self, periodoInicio, periodoFin):
        numTra = self.obenerCantidadTransacciones(periodoInicio, periodoFin)
        transacciones = self.obtenerTransacciones(periodoInicio, periodoFin)
        sumTra = 0
        for transaccion in transacciones:
            sumTra = transaccion.convertir_a_pesos()
        return 30 - ((sumTra / numTra) * 0.5)
