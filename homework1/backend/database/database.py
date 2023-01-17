from app_init import db

class Stock(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    vm_id = db.Column(db.Integer, db.ForeignKey('vending_machine.id'), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, vm_id, product, quantity):
        self.vm_id = vm_id
        self.product = product
        self.quantity = quantity
        
    def __repr__(self):
        return '<Stock %r>' % self.product
    
    def to_dict(self):
        return {
            'id': self.id,
            'vm_id': self.vm_id,
            'product': self.product,
            'quantity': self.quantity
        }

class VendingMachine(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)

    def __init__(self, name, location):
        self.name = name
        self.location = location
    def __repr__(self):
        return '<VendingMachine %r>' % self.name
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }