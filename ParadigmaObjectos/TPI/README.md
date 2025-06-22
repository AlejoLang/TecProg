# CONSIGNA PARADIGMA ORIENTADO A OBJETOS

Se solicita desarrollar una aplicación orientada a objetos que modele el funcionamiento
del sistema de reservas y ventas de pasajes de la empresa ArgentinaTur. La empresa
opera con itinerarios nacionales predefinidos, compuestos por una ciudad de origen,
una ciudad de destino y una serie de paradas intermedias, cada una representada por
una ciudad con su respectivo código, nombre y provincia. Los servicios son viajes
concretos que se programan sobre estos itinerarios, indicando fechas de partida y
llegada, calidad del servicio (común o ejecutivo), y la unidad (colectivo) asignada.
Las unidades poseen una configuración específica de asientos que pueden estar libres u
ocupados.
El sistema debe permitir crear itinerarios, programar servicios, consultar asientos
disponibles, reservar pasajes y concretar ventas. Las reservas se vinculan a un
pasajero, se registran con fecha y hora, y caducan automáticamente 30 minutos antes de
la salida si no se concretan, liberando el asiento. Las ventas de pasajes se asocian a
un pasajero, e implican la validación de un medio de pago a través de un servicio
externo simulado. Debe quedar registro de la operación, incluyendo los datos del
pasajero, y del asiento. A su vez, se deben incluir medios de pago: Ualá, tarjeta de
crédito, MercadoPago.
Se espera que la solución implemente clases para las principales entidades del dominio
(Ciudad, Itinerario, Servicio, Unidad, Asiento, Pasajero, Pasaje, Tarjeta de Crédito),
y que se definan métodos que representan los comportamientos clave del sistema:

- Consigna 1: diseñar las clases necesarias para representar el dominio del sistema de
  transporte de ArgentinaTur incluyendo atributos, métodos y relaciones adecuadas para
  cumplir los siguientes comportamientos.
- Consigna 2: simular las siguientes gestiones.

> 1.  Consultar servicios disponibles: el sistema debe mostrar todos los
>     servicios disponibles, incluyendo su itinerario (ciudades de origen,
>     destino, las paradas intermedias), calidad del servicio y fechas de
>     partida y llegada disponibles.
> 2.  A partir de la consulta de servicios, simular la reserva de un servicio
>     por parte de un pasajero.
>     > a. Permitir seleccionar un servicio.
>     > b. Mostrar los asientos disponibles para ese servicio. Ejemplo:
>     > “Asientos libres: 1, 2, 4, 6...”
>     > c. Realizar la reserva de un asiento para un pasajero. Verificar que
>     > esté libre. Si no, mostrar un error. Registrar la reserva con fecha
>     > y hora. Mostrar un mensaje del tipo: "Reserva realizada: Pasajero
>     > Juan Pérez, asiento 2, servicio del 12/04/2025".

> > d. Volver a mostrar el estado actualizado de los asientos. Ejemplo:
> > “Asientos libres: 1, 4, 6... / Ocupados: 2 (reservado)”. 3. Generar un informe, que ingresando los datos de fecha desde y hasta,
> > muestre los montos totales facturados, cantidad de viajes a cada
> > localidad destino y cantidades de pagos discriminados por medio de pago,
> > en ese período ingresado.
> > Para la realización de este trabajo, tomar como referencia el siguiente esquema de las
> > clases y relaciones entre las mismas. Esto es solo un punto de partida, deberán
> > considerar los atributos, métodos, relaciones y tipo de relaciones entre clases que
> > necesiten para resolver las consignas.

# Esquema del diagrama a considerar

```

```

@startuml

class Argentur{

- sistemaActivo: boolean
  }

' Entidad Ciudad
class Ciudad {
-codigo: String
-nombre: String
-provincia: String
}

' Itinerario compuesto por ciudades (origen, destino, paradas)
class Itinerario {
}

' Unidad (colectivo)
class Unidad {
-patente: String
}

class Asiento {
-numero: int
-ocupado: boolean
}

' Servicio (viaje programado)
class Servicio {
-unidad: Unidad
-fechaPartida: DateTime
-fechaLlegada: DateTime
-calidad: String
-precio: float
}

' Pasajero

class Pasajero {
-nombre: String
-email: String

- dni: int
  }

' Reserva
class Reserva {
-fechaHora: DateTime
}

' Venta
class Venta {
-fechaHora: DateTime
}

' Medios de pago
abstract class MedioPago {
}

class TarjetaCredito extends MedioPago {
-numero: String
-DNItitular: int
-nombre: String
-fechaVencimiento: Date
}

class MercadoPago extends MedioPago {
-celular: String
-email: String
}

class Uala extends MedioPago {
-email: String
-nombreTitular: String
}

' Relaciones
Pasajero--Asiento
Argentur--Venta
Argentur -- Servicio
Itinerario -- Ciudad
Servicio -- Itinerario
Servicio -- Unidad
Unidad -- Asiento
Reserva-- Pasajero
Venta -- Pasajero
Venta -- Asiento
Venta -- MedioPago
Servicio -- Reserva
Servicio-- Venta

@enduml

```

```
