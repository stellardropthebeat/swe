"""Database model."""

from src.app_init import db


class VendingMachine(db.Model):
    """Vending Machine Model."""

    __tablename__: str = "vending_machine"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(255), unique=True, nullable=False)
    location: str = db.Column(db.String(255), nullable=False)

    def __init__(self: "VendingMachine", name: str, location: str) -> None:
        """Initialize with name and location."""
        self.name: str = name
        self.location: str = location

    def to_dict(self: "VendingMachine") -> dict:
        """Return object data in easily serializable format."""
        return {"id": self.id, "name": self.name, "location": self.location}


class Stock(db.Model):
    """Stock model."""

    __tablename__: str = "stock"

    id: int = db.Column(db.Integer, primary_key=True)
    vm_id: int = db.Column(db.Integer, nullable=False)
    product: str = db.Column(db.String(255), unique=True, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)

    def __init__(self: "Stock", vm_id: int, stock: str, quantity: int) -> None:
        """Initialize a stock."""
        self.vm_id: int = vm_id
        self.product: str = stock
        self.quantity: int = quantity

    def to_dict(self: "Stock") -> dict:
        """Return object data in easily serializable format."""
        return {
            "id": self.id,
            "vm_id": self.vm_id,
            "product": self.product,
            "quantity": self.quantity,
        }


class VendingMachineTimeLine(db.Model):
    """Vending Machine timeline Model."""

    __tablename__: str = "vending_machine_timeline"

    id: int = db.Column(db.Integer, primary_key=True)
    vm_id: int = db.Column(db.Integer, nullable=False)
    event: str = db.Column(db.String(255), nullable=False)
    timestamp: str = db.Column(db.String(255), nullable=False)

    def __init__(self: "VendingMachineTimeLine", vm_id: int, event: str, timestamp: str) -> None:
        """Initialize with name and location."""
        self.vm_id: int = vm_id
        self.event: str = event
        self.timestamp: str = timestamp

    def to_dict(self: "VendingMachineTimeLine") -> dict:
        """Return object data in easily serializable format."""
        return {
            "id": self.id,
            "vm_id": self.vm_id,
            "event": self.event,
            "timestamp": self.timestamp,
        }
