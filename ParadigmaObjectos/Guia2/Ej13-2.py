from abc import ABC, abstractmethod


class ServicioNotificador(ABC):
    @abstractmethod
    def enviar_notificacion(self, destinatario: str, mansaje: str):
        pass


class CorreoElectronico(ServicioNotificador):
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        # Lógica para enviar notificación por correo electrónico
        print(f"Correo electrónico enviado a {destinatario}: {mensaje}")


class Notificador:
    def __init__(self, servicioNot: ServicioNotificador):
        self.servicioNotificador = servicioNot

    def enviar_notificacion(self, destinatario: str, mensaje: str):
        self.servicioNotificador.enviar_notificacion(destinatario, mensaje)


# Uso del código actual
correo_electronico = CorreoElectronico()
notificador = Notificador(correo_electronico)
notificador.enviar_notificacion(
    "usuario@example.com", "¡Tu tarea está lista!")
