from flask import Blueprint, request, jsonify, render_template
from app_svc import VendingMachineManager
from database.database import VendingMachine, Stock

app_controller = Blueprint('app_controller', __name__)

@app_controller.route('/')
def index():
    return render_template('base.html')
@app_controller.route('/machines')
def machines():
    return render_template('machines.html')
@app_controller.route('/stock')
def stocks():
    return render_template('stock.html')
    
@app_controller.route('/add_machine', methods=['POST'])
def add_machine():
    name = request.json['name']
    location = request.json['location']
    manager = VendingMachineManager()
    manager.create_machine(name, location)
    return jsonify(success=True, message="Vending machine created successfully")
@app_controller.route('/get_machine/<int:id>', methods=['GET'])
def get_machine(id):
    manager = VendingMachineManager()
    machine = manager.read_machine(id=id)
    if machine:
        return jsonify(success=True, machine=machine.to_dict())
    else:
        return jsonify(success=False, message="Vending machine not found"), 404
@app_controller.route('/update_machine/<int:id>', methods=['PUT'])
def update_machine(id):
    manager = VendingMachineManager()
    machine = manager.read_machine(id=id)
    if machine:
        name = request.json.get('name', machine.name)
        location = request.json.get('location', machine.location)
        manager.update_machine(id, name=name, location=location)
        return jsonify(success=True, message="Vending machine updated successfully")
    else:
        return jsonify(success=False, message="Vending machine not found"), 404
@app_controller.route('/delete_machine/<int:id>', methods=['DELETE'])
def delete_machine(id):
    manager = VendingMachineManager()
    machine = manager.read_machine(id=id)
    if machine:
        manager.delete_machine(id)
        return jsonify(success=True, message="Vending machine deleted successfully")
    else:
        return jsonify(success=False, message="Vending machine not found"), 404
@app_controller.route('/add_product', methods=['POST'])
def add_product():
    vm_id = request.json['vm_id']
    product = request.json['product']
    quantity = request.json['quantity']
    manager = VendingMachineManager()
    manager.create_product(vm_id, product, quantity)
    return jsonify(success=True, message="Product added successfully"), 201
@app_controller.route('/update_product/<int:id>', methods=['PUT'])
def update_product(id):
    manager = VendingMachineManager()
    product_to_update = manager.read_product(id=id)
    if product_to_update:
        product = request.json.get('product', product_to_update.product)
        quantity = request.json.get('quantity', product_to_update.quantity)
        manager.update_product(id, product=product, quantity=quantity)
        return jsonify(success=True, message="product updated successfully")
    else:
        return jsonify(success=False, message="Vending machine not found"), 404
@app_controller.route('/get_product/<int:id>', methods=['GET'])
def get_product(id):
    manager = VendingMachineManager()
    product = manager.read_product(id=id)
    if product:
        return jsonify(success=True, product=product.to_dict())
    else:
        return jsonify(success=False, message="Product not found"), 404

@app_controller.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product(id):
    manager = VendingMachineManager()
    product_to_delete = manager.read_product(id=id)
    if product_to_delete:
        manager.delete_product(id)
        return jsonify(success=True, message="Produt deleted successfully")
    else:
        return jsonify(success=False, message="Product not found"), 404

@app_controller.route('/all_machines', methods=['GET'])
def get_all_machines():
    machines = VendingMachine.query.all()
    machines_list = [machine.to_dict() for machine in machines]
    return jsonify(machines_list)

@app_controller.route('/all_products', methods=['GET'])
def get_all_products():
    products = Stock.query.all()
    products_list = [product.to_dict() for product in products]
    return jsonify(products_list)