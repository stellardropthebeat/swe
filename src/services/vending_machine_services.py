"""Vending Machine Services Module."""

from src.app_init import db
from src.database.model import VendingMachine


class VendingMachineManager:
    """Vending Machine Manager Class."""

    def __init__(self: "VendingMachineManager") -> None:
        """Initialize a vending machine manager."""
        self.db = db

    def create_machine(self: "VendingMachineManager", name: str, location: str) -> int:
        """Create a new vending machine in the vending machine table."""
        new_machine: VendingMachine = VendingMachine(name=name, location=location)
        self.db.session.add(new_machine)
        self.db.session.commit()
        return new_machine.id

    def update_machine(self: "VendingMachineManager", machine_id: int, name: str = None, location: str = None) -> None:
        """Update a vending machine in the vending machine table."""
        machine: VendingMachine = VendingMachine.query.filter_by(id=machine_id).first()
        machine.name = name
        machine.location = location
        self.db.session.commit()
        self.db.session.close()

    def delete_machine(self: "VendingMachineManager", machine_id: int) -> None:
        """Delete a vending machine from the vending machine table."""
        machine: VendingMachine = VendingMachine.query.filter_by(id=machine_id).first()
        self.db.session.delete(machine)
        self.db.session.commit()
        self.db.session.close()
