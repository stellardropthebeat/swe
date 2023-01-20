from database.database import VendingMachine, Stock
from app_init import db

class VendingMachineManager:
    def __init__(self):
        self.db = db
    def create_machine(self, name, location):
        new_machine = VendingMachine(name=name, location=location)
        self.db.session.add(new_machine)
        self.db.session.commit()
        self.db.session.close()
    def read_machine(self, id=None, name=None):
        if id:
            machine = VendingMachine.query.filter_by(id=id).first()
        elif name:
            machine = VendingMachine.query.filter_by(name=name).first()
        else:
            machine = VendingMachine.query.all()
        return machine
    def update_machine(self, id, name=None, location=None):
        machine = VendingMachine.query.filter_by(id=id).first()
        if name:
            machine.name = name
        if location:
            machine.location = location
        self.db.session.commit()
        self.db.session.close()
    def delete_machine(self, id):
        machine = VendingMachine.query.filter_by(id=id).first()
        self.db.session.delete(machine)
        self.db.session.commit()
        self.db.session.close()
    def create_product(self, vm_id, product, quantity):
        new_product = Stock(vm_id=vm_id, product=product, quantity=quantity)
        self.db.session.add(new_product)
        self.db.session.commit()
        self.db.session.close()
    def read_product(self, id=None, product=None):
        if id:
            product = Stock.query.filter_by(id=id).first()
        elif product:
            product = Stock.query.filter_by(product=product).first()
        else:
            product = Stock.query.all()
        return product
    def update_product(self, id, product=None, quantity=None):
        stock = Stock.query.filter_by(id=id).first()
        if product:
            stock.product = product
        if quantity:
            stock.quantity = quantity
        self.db.session.commit()
        self.db.session.close()
    def delete_product(self, id):
        stock = Stock.query.filter_by(id=id).first()
        self.db.session.delete(stock)
        self.db.session.commit()
        self.db.session.close()