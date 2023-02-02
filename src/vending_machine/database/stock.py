"""Stock model."""

from app_init import db


class Stock(db.Model):
    """Stock model."""

    id: int = db.Column(db.Integer, primary_key=True)
    vm_id: int = db.Column(db.Integer, nullable=False)
    product: str = db.Column(db.String(255), unique=True, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)

    def __init__(self: "Stock", vm_id: int, stock: str, quantity: int) -> None:
        """Initialize a stock."""
        self.vm_id: int = vm_id
        self.product: str = stock
        self.quantity: int = quantity

    def __repr__(self: "Stock") -> str:
        """Represent a stock as a unique string."""
        return "<Stock %r>" % self.product

    def to_dict(self: "Stock") -> dict:
        """Return object data in easily serializable format."""
        return {
            "id": self.id,
            "vm_id": self.vm_id,
            "product": self.product,
            "quantity": self.quantity,
        }