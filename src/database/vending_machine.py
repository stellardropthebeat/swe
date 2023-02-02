"""Vending Machine Model."""

from src.app_init import db


class VendingMachine(db.Model):
    """Vending Machine Model."""

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(255), unique=True, nullable=False)
    location: str = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self: "VendingMachine", name: str, location: str) -> None:
        """Initialize with name and location."""
        self.name: str = name
        self.location: str = location

    def __repr__(self: "VendingMachine") -> str:
        """Represent instance as a unique string."""
        return "<VendingMachine %r>" % self.name

    def to_dict(self: "VendingMachine") -> dict:
        """Return object data in easily serializable format."""
        return {"id": self.id, "name": self.name, "location": self.location}
