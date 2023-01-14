from flask import Flask, request, jsonify
from vending import VendingMachineManager, VendingMachine

app = Flask(__name__)

manager = VendingMachineManager()

@app.route('/add_machine', methods=['POST'])
def add_machine():
    name = request.json['name']
    location = request.json['location']
    manager.add_machine(name, location)
    return jsonify(success=True, message=f"Vending machine {name} with location {location} created successfully")

@app.route('/remove_machine/<name>', methods=['DELETE'])
def remove_machine(name):
    manager.remove_machine(name)
    return jsonify(success=True, message=f"Vending machine {name} removed successfully")

@app.route('/update_machine', methods=['PUT'])
def update_machine():
    name = request.json['name']
    location = request.json['location']
    manager.update_machine(name, location)
    return jsonify(success=True, message=f"Vending machine {name} location updated to {location}")

@app.route('/add_product', methods=['POST'])
def add_product():
    machine_name = request.json['machine_name']
    product = request.json['product']
    quantity = request.json['quantity']
    manager.add_product(machine_name, product, quantity)
    return jsonify(success=True, message=f"Product {product} with quantity {quantity} added to vending machine {machine_name}")

@app.route('/update_product', methods=['PUT'])
def update_product():
    machine_name = request.json['machine_name']
    product = request.json['product']
    quantity = request.json['quantity']
    manager.update_product(machine_name, product, quantity)
    return jsonify(success=True, message=f"Product {product} with quantity {quantity} updated in vending machine {machine_name}")

@app.route('/remove_product', methods=['DELETE'])
def remove_product():
    machine_name = request.json['machine_name']
    product = request.json['product']
    manager.remove_product(machine_name, product)
    return jsonify(success=True, message=f"Product {product} removed from vending machine {machine_name}")

@app.route('/list_products', methods=['GET'])
def list_products():
    products = manager.list_products()
    return jsonify(success=True, products=products)

@app.route('/list_products_by_machine', methods=['GET'])
def list_products_by_machine():
    products_by_machine = manager.list_products_by_machine()
    return jsonify(success=True, products_by_machine=products_by_machine)

if __name__ == '__main__':
    app.run(debug=True)
