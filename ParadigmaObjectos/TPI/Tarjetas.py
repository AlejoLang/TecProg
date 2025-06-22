from abc import ABC, abstractmethod


class MetodoPago(ABC):
    def validar_tarjeta(self):
        pass


class TarjetaCredito:
    def __init__(self, numero, dni_titular, nombre, fecha_vencimiento):
        self.numero = numero
        self.dni_titular = dni_titular
        self.nombre = nombre
        self.fecha_vencimiento = fecha_vencimiento


class MercadoPago:
    def __init__(self, celular, email):
        self.celular = celular
        self.email = email


class Uala:
    def __init__(self, email, nombre_titular):
        self.email = email
        self.nombre_titular = nombre_titular
