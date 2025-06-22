from datetime import datetime
from typing import List


class Reserva:
    def __init__(self, Fecha_Hora: datetime):
        self.Fecha_Hora = Fecha_Hora

    def obtener_FechaHora_reserva(self):
        return self.Fecha_Hora


class Asiento:
    def __init__(self, numero):
        self.numero = numero
        self.ocupado = False

    def obtener_numero(self):
        return self.numero

    def establecer_estado(self, estado: bool):
        self.ocupado = estado

    def esta_ocupado(self):
        return self.ocupado


class Unidad:
    def __init__(self, patente, num_asientos):
        self.patente = patente
        self.asientos: List[Asiento] = []
        for i in range(num_asientos):
            self.asientos.append(Asiento(i + 1))

    def obtener_asientos(self):
        return self.asientos

    def obtener_disponibilidad_asiento(self, num_asiento):
        return not self.asientos[num_asiento - 1].esta_ocupado()

    def reservar(self, num_asiento):
        if not self.asientos[num_asiento - 1].esta_ocupado():
            self.asientos[num_asiento - 1].establecer_estado(True)
            return True
        return False


class Pasajero:
    def __init__(self, Nombre, Email, Dni):
        self.Nombre = Nombre
        self.Email = Email
        self.Dni = Dni

    def obtener_nombre(self):
        return self.Nombre

    def obtener_email(self):
        return self.Email

    def obtener_dni(self):
        return self.Dni
