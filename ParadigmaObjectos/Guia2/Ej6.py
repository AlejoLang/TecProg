class Empleado:
    def __init__(self, name, lastName, dni, address, boss):
        self.name = name
        self.lastName = lastName
        self.dni = dni
        self.address = address
        self.boss = boss


class EmpleadoMensualizado(Empleado):
    def __init__(self, name, lastName, dni, address, boss, salary):
        super().__init__(name, lastName, dni, address, boss)
        self.salaryMonth = salary


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


class Jefe(Empleado):
    def __init__(self, name, lastName, dni, address, salary):
        super().__init__(name, lastName, dni, address, jefe=None)
        self.salary = salary
