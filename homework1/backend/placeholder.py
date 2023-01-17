#import json
#import os
#from flask import Flask, request, jsonify, render_template
#from sqlalchemy_utils import database_exists, create_database
#from flask_sqlalchemy import SQLAlchemy
#
#app = Flask(__name__)
#with app.app_context():
#    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
#    #app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://myuser:mypassword@mariadb:3306/mydb"
#
#    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
#        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
#
#    db = SQLAlchemy(app)
#
#    class VendingMachine(db.Model):
#        id = db.Column(db.Integer, primary_key=True)
#        name = db.Column(db.String(255), nullable=False)
#        location = db.Column(db.String(255), nullable=False)
#
#        def __init__(self, name, location):
#            self.name = name
#            self.location = location
#
#        def __repr__(self):
#            return '<VendingMachine %r>' % self.name
#
#        def to_dict(self):
#            return {
#                'id': self.id,
#                'name': self.name,
#                'location': self.location
#            }
#
#    class Stock(db.Model):
#        id = db.Column(db.Integer, primary_key=True)
#        vm_id = db.Column(db.Integer, db.ForeignKey('vending_machine.id'), nullable=False)
#        product = db.Column(db.String(255), nullable=False)
#        quantity = db.Column(db.Integer, nullable=False)
#
#        def __init__(self, vm_id, product, quantity):
#            self.vm_id = vm_id
#            self.product = product
#            self.quantity = quantity
#
#        def __repr__(self):
#            return '<Stock %r>' % self.product
#        
#        def to_dict(self):
#            return {
#                'id': self.id,
#                'vm_id': self.vm_id,
#                'product': self.product,
#                'quantity': self.quantity
#            }
#
#    class VendingMachineManager:
#        def __init__(self):
#            self.db = db
#        def create_machine(self, name, location):
#            new_machine = VendingMachine(name=name, location=location)
#            self.db.session.add(new_machine)
#            self.db.session.commit()
#            self.db.session.close()
#        def read_machine(self, id=None, name=None):
#            if id:
#                machine = VendingMachine.query.filter_by(id=id).first()
#            elif name:
#                machine = VendingMachine.query.filter_by(name=name).first()
#            else:
#                machine = VendingMachine.query.all()
#            return machine
#        def update_machine(self, id, name=None, location=None):
#            machine = VendingMachine.query.filter_by(id=id).first()
#            if name:
#                machine.name = name
#            if location:
#                machine.location = location
#            self.db.session.commit()
#            self.db.session.close()
#        def delete_machine(self, id):
#            machine = VendingMachine.query.filter_by(id=id).first()
#            self.db.session.delete(machine)
#            self.db.session.commit()
#            self.db.session.close()
#        def create_product(self, vm_id, product, quantity):
#            new_product = Stock(vm_id=vm_id, product=product, quantity=quantity)
#            self.db.session.add(new_product)
#            self.db.session.commit()
#            self.db.session.close()
#        def read_product(self, id=None, product=None):
#            if id:
#                product = Stock.query.filter_by(id=id).first()
#            elif product:
#                product = Stock.query.filter_by(product=product).first()
#            else:
#                product = Stock.query.all()
#            return product
#        def update_product(self, id, product=None, quantity=None):
#            stock = Stock.query.filter_by(id=id).first()
#            if product:
#                stock.product = product
#            if quantity:
#                stock.quantity = quantity
#            self.db.session.commit()
#            self.db.session.close()
#        def delete_product(self, id):
#            stock = Stock.query.filter_by(id=id).first()
#            self.db.session.delete(stock)
#            self.db.session.commit()
#            self.db.session.close()
#
#    db.create_all()
#
#    @app.route('/')
#    def index():
#        return render_template('base.html')
#
#    @app.route('/machines')
#    def machines():
#        return render_template('machines.html')
#
#    @app.route('/stock')
#    def stocks():
#        return render_template('stock.html')
#        
#    @app.route('/add_machine', methods=['POST'])
#    def add_machine():
#        name = request.json['name']
#        location = request.json['location']
#        manager = VendingMachineManager()
#        manager.create_machine(name, location)
#        return jsonify(success=True, message="Vending machine created successfully")
#
#    @app.route('/get_machine/<int:id>', methods=['GET'])
#    def get_machine(id):
#        manager = VendingMachineManager()
#        machine = manager.read_machine(id=id)
#        if machine:
#            return jsonify(success=True, machine=machine.to_dict())
#        else:
#            return jsonify(success=False, message="Vending machine not found"), 404
#
#    @app.route('/update_machine/<int:id>', methods=['PUT'])
#    def update_machine(id):
#        manager = VendingMachineManager()
#        machine = manager.read_machine(id=id)
#        if machine:
#            name = request.json.get('name', machine.name)
#            location = request.json.get('location', machine.location)
#            manager.update_machine(id, name=name, location=location)
#            return jsonify(success=True, message="Vending machine updated successfully")
#        else:
#            return jsonify(success=False, message="Vending machine not found"), 404
#
#    @app.route('/delete_machine/<int:id>', methods=['DELETE'])
#    def delete_machine(id):
#        manager = VendingMachineManager()
#        machine = manager.read_machine(id=id)
#        if machine:
#            manager.delete_machine(id)
#            return jsonify(success=True, message="Vending machine deleted successfully")
#        else:
#            return jsonify(success=False, message="Vending machine not found"), 404
#
#    @app.route('/add_product', methods=['POST'])
#    def add_product():
#        vm_id = request.json['vm_id']
#        product = request.json['product']
#        quantity = request.json['quantity']
#        manager = VendingMachineManager()
#        manager.create_product(vm_id, product, quantity)
#        return jsonify(success=True, message="Product added successfully"), 201
#
#    @app.route('/update_product/<int:id>', methods=['PUT'])
#    def update_product(id):
#        manager = VendingMachineManager()
#        product_to_update = manager.read_product(id=id)
#        if product_to_update:
#            product = request.json.get('product', product_to_update.product)
#            quantity = request.json.get('quantity', product_to_update.quantity)
#            manager.update_product(id, product=product, quantity=quantity)
#            return jsonify(success=True, message="product updated successfully")
#        else:
#            return jsonify(success=False, message="Vending machine not found"), 404
#
#    @app.route('/get_product/<int:id>', methods=['GET'])
#    def get_product(id):
#        manager = VendingMachineManager()
#        product = manager.read_product(id=id)
#        if product:
#            return jsonify(success=True, product=product.to_dict())
#        else:
#            return jsonify(success=False, message="Product not found"), 404
#    
#    @app.route('/delete_product/<int:id>', methods=['DELETE'])
#    def delete_product(id):
#        manager = VendingMachineManager()
#        product_to_delete = manager.read_product(id=id)
#        if product_to_delete:
#            manager.delete_product(id)
#            return jsonify(success=True, message="Produt deleted successfully")
#        else:
#            return jsonify(success=False, message="Product not found"), 404
#
#    @app.route('/all_machines', methods=['GET'])
#    def get_all_machines():
#        machines = VendingMachine.query.all()
#        machines_list = [machine.to_dict() for machine in machines]
#        return jsonify(machines_list)
#
#    @app.route('/all_products', methods=['GET'])
#    def get_all_products():
#        products = Stock.query.all()
#        products_list = [product.to_dict() for product in products]
#        return jsonify(products_list)
#
#if __name__ == '__main__':
#    from waitress import serve
#
#    serve(app, host="0.0.0.0", port=5000)
