class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def generar_reporte_desempenio(self):
        # Código para generar el reporte de desempeño
        pass

# Corrección


class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora


class ReporteDesempenio:
    def generar(self, empleado):
        pass
