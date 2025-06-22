from typing import List


class Empleado:
    def __init__(self, name, lastName, dni, address, boss):
        self.name = name
        self.lastName = lastName
        self.dni = dni
        self.address = address
        self.boss = boss

    def __str__(self):
        print(self.name, self.lastName, self.dni, self.address)


class EmpleadoMensualizado(Empleado):
    def __init__(self, name, lastName, dni, address, boss, salary, cat):
        super().__init__(name, lastName, dni, address, boss)
        self.salaryMonth = salary
        self.category = cat

    def __str__(self):
        print("Empleado mensualizado cat", self.category)
        super().__str__()


class EmpleadoJornalizado(Empleado):
    def __init__(self, name, lastName, dni, address, boss, salaryBasic, salaryExtra):
        super().__init__(name, lastName, dni, address, boss)
        self.salaryBasicHrs = salaryBasic
        self.salaryExtraHrs = salaryExtra
        self.hours = 0

    def getTotalSalary(self):
        if (self.hours > 40):
            return (self.hours - 40) * self.salaryExtraHrs + 40 * self.salaryBasicHrs
        else:
            return self.hours * self.salaryBasicHrs

    def __str__(self):
        print("Empleado jornalizado")
        super().__str__()


class Jefe(Empleado):
    def __init__(self, name, lastName, dni, address, salary):
        super().__init__(name, lastName, dni, address, None)
        self.salary = salary

    def __str__(self):
        print(self.name, self.lastName)


class Nomina:
    def __init__(self):
        self.empleados: List[Empleado] = []
        self.jefes: List[Jefe] = []

    def listar_empleados_por_jefe(self, jefe: Jefe):
        jefe.__str__
        for empleado in self.empleados:
            if (empleado.boss == jefe):
                empleado.__str__()


if __name__ == "__main__":
    jef = Jefe("fadsf", "asd", 3424324, "skdjfkds", 100000)
    emp = EmpleadoMensualizado(
        "Pepe", "Perez", 1231241, "askdjsd", jef, 1000, 2)
    emp2 = EmpleadoJornalizado(
        "Jaun", "sadas", 2312312, "asdsa", jef, 10000, 100)
    nom = Nomina()
    nom.empleados = [emp, emp2]
    nom.jefes = [jef]
    nom.listar_empleados_por_jefe(jef)
