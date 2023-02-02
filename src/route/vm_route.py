"""Vending Machine API Route."""

from flask import Blueprint, Response, jsonify, render_template, request
from sqlalchemy.orm import collections

from src.database.vending_machine import VendingMachine
from src.services.vending_machine_services import VendingMachineManager

vm_controller: Blueprint = Blueprint("vm_controller", __name__)

failed_message: str = "Vending machine not found"
create_success: str = "Vending machine created successfully"
update_success: str = "Vending machine updated successfully"
delete_success: str = "Vending machine deleted successfully"


@vm_controller.route("/")
def index() -> str:
    """Index page."""
    return render_template("base.html")


@vm_controller.route("/machines")
def machines() -> str:
    """Vending machines page."""
    return render_template("machines.html")


@vm_controller.route("/add_machine", methods=["POST"])
def add_machine() -> tuple[Response, int]:
    """Add vending machine."""
    name: str = request.json["name"]
    location: str = request.json["location"]
    manager: VendingMachineManager = VendingMachineManager()
    machine_id: int = manager.create_machine(name, location)
    if machine_id:
        return jsonify(success=True, message=create_success, id=machine_id), 201
    else:
        return jsonify(success=False, message=failed_message), 500


@vm_controller.route("/update_machine/<int:machine_id>", methods=["PUT"])
def update_machine(machine_id: int) -> tuple[Response, int]:
    """Update vending machine."""
    manager: VendingMachineManager = VendingMachineManager()
    machine: VendingMachine = manager.read_machine(machine_id=machine_id)
    if machine:
        name: str = request.json.get("name", machine.name)
        location: str = request.json.get("location", machine.location)
        manager.update_machine(machine_id, name=name, location=location)
        return jsonify(success=True, message=update_success), 200
    else:
        return jsonify(success=False, message=failed_message), 404


@vm_controller.route("/delete_machine/<int:machine_id>", methods=["DELETE"])
def delete_machine(machine_id: int) -> tuple[Response, int]:
    """Delete vending machine."""
    manager: VendingMachineManager = VendingMachineManager()
    machine: VendingMachine = manager.read_machine(machine_id=machine_id)
    if machine:
        manager.delete_machine(machine_id)
        return jsonify(success=True, message=delete_success), 200
    else:
        return jsonify(success=False, message=failed_message), 404


@vm_controller.route("/all_machines", methods=["GET"])
def get_all_machines() -> tuple[Response, int]:
    """Get all vending machines."""
    all_machines: collections.Iterable = VendingMachine.query.all()
    machines_list: list = [machine.to_dict() for machine in all_machines]
    return jsonify(machines_list), 200
