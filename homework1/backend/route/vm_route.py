from flask import Blueprint, request, jsonify, render_template
from app_svc import VendingMachineManager
from database.database import VendingMachine

vm_controller = Blueprint('vm_controller', __name__)

@vm_controller.route('/')
def index():
    return render_template('base.html')

@vm_controller.route('/machines')
def machines():
    return render_template('machines.html')

@vm_controller.route('/add_machine', methods=['POST'])
def add_machine():
    name = request.json['name']
    location = request.json['location']
    manager = VendingMachineManager()
    manager.create_machine(name, location)
    return jsonify(success=True, message="Vending machine created successfully")
@vm_controller.route('/get_machine/<int:id>', methods=['GET'])
def get_machine(id):
    manager = VendingMachineManager()
    machine = manager.read_machine(id=id)
    if machine:
        return jsonify(success=True, machine=machine.to_dict())
    else:
        return jsonify(success=False, message="Vending machine not found"), 404
@vm_controller.route('/update_machine/<int:id>', methods=['PUT'])
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
@vm_controller.route('/delete_machine/<int:id>', methods=['DELETE'])
def delete_machine(id):
    manager = VendingMachineManager()
    machine = manager.read_machine(id=id)
    if machine:
        manager.delete_machine(id)
        return jsonify(success=True, message="Vending machine deleted successfully")
    else:
        return jsonify(success=False, message="Vending machine not found"), 404

@vm_controller.route('/all_machines', methods=['GET'])
def get_all_machines():
    machines = VendingMachine.query.all()
    machines_list = [machine.to_dict() for machine in machines]
    return jsonify(machines_list)