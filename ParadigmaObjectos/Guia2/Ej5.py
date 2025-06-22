import datetime


class Empresa:
    def __init__(self, name):
        self.name = name
        self.facturas = []

    def addFact(self, factura):
        self.facturas.append(factura)

    def totalFacturas(self):
        total = 0
        for factura in self.facturas:
            total += factura.getTotal()
        return total

    def showFacturas(self):
        print("Nombre empresa: ", self.name, " - IVA Monotributo")
        print("")
        for factura in self.facturas:
            print("Factura nro", factura.num)
            print("Cliente: ", factura.client.name,
                  " - CUIT: ", factura.client.cuit)
            print("Fecha: ", factura.date.strftime("%d/%m/%Y"))
            print("Total: $", factura.getTotal())
            i = 1
            for subitem in factura.subitems:
                print(
                    f"Detalle {i}: {subitem.item.name} {subitem.ammount} unid. Total item: {subitem.getSubTotal()}")
            print("")
        print("Total facturas: ", self.totalFacturas())


class Cliente:
    def __init__(self, name, cuit):
        self.name = name
        self.cuit = cuit


class Factura:
    def __init__(self, num, client, date):
        self.num = num
        self.date = date
        self.client = client
        self.subitems = []

    def addSubItem(self, subitem):
        self.subitems.append(subitem)

    def getTotal(self):
        total = 0
        for item in self.subitems:
            total += item.getSubTotal()
        return total


class SubItem:
    def __init__(self, item, ammount):
        self.item = item
        self.ammount = ammount

    def getSubTotal(self):
        return self.item.getPrice() * self.ammount


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getPrice(self):
        return self.price


emp = Empresa("Mayorista S.A.")
cli = Cliente("Gilcomat SRL", "30-12345678-1")

itm1 = Item("Porcelanato 45x45", 6)
itm2 = Item("Grifería FV 6 piezas", 400)

subitm1 = SubItem(itm1, 100)
subitm2 = SubItem(itm2, 1)

fact = Factura("0001 0100", cli, datetime.date.today())
fact.addSubItem(subitm1)
fact.addSubItem(subitm2)

emp.addFact(fact)
emp.showFacturas()
