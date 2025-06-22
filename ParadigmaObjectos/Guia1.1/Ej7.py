costoDiaAlquiler = float(input("Introduce el costo por día de alquiler del vehículo: "))
numeroDias = int(input("Introduce el número de días de alquiler: "))
presupuestoCombustible = float(input("Introduce el presupuesto para combustible: "))

costoAlquiler = costoDiaAlquiler * numeroDias
presupuestoTotal = presupuestoCombustible + costoAlquiler

print("Costo total:", presupuestoTotal)