"""Database model."""

from datetime import datetime
from typing import List

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
        return {"id": self.id, "vm_id": self.vm_id, "product": self.product, "quantity": self.quantity}


def add_to_timeline(vm_id: int, product_id: int, quantity: int) -> None:
    """Add stock to timeline."""
    db.session.add(StockTimeLine(vm_id, product_id, quantity))
    db.session.commit()


class StockTimeLine(db.Model):
    """Stock Timeline model."""

    __tablename__: str = "stock_timeline"

    id: int = db.Column(db.Integer, primary_key=True)
    vm_id: int = db.Column(db.Integer, nullable=False)
    product_id: int = db.Column(db.Integer, nullable=False)
    quantity: int = db.Column(db.Integer, nullable=False)
    all_product: List[int] = db.Column(db.ARRAY(db.Integer))
    time: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self: "StockTimeLine", vm_id: int, product_id: int, quantity: int) -> None:
        """Initialize a stock."""
        self.vm_id: int = vm_id
        self.product_id: int = product_id
        self.quantity: int = quantity
        all_product = [product.id for product in Stock.query.filter_by(vm_id=vm_id).all()]
        all_product.append(product_id)
        self.all_product = all_product

    def get_all_product_stock(self) -> dict:
        """Get all product stock."""
        ret: dict = {}
        for product_id in self.all_product:
            if product_id == self.product_id:
                ret[self.product_id] = {
                    "product_name": Stock.query.filter_by(id=self.product_id).first().product,
                    "quantity": self.quantity,
                }
                continue
            timeline: List = (
                StockTimeLine.query.filter(StockTimeLine.time < self.time).filter_by(product_id=product_id).all()
            )
            if len(timeline) > 0:
                product: StockTimeLine = timeline[-1]
                ret[product.product_id] = {
                    "product_name": Stock.query.filter_by(id=product.product_id).first().product,
                    "quantity": product.quantity,
                }
        return ret

    def to_dict(self: "StockTimeLine") -> dict:
        """Return object data in easily serializable format."""
        return {
            "vm_name": VendingMachine.query.filter_by(id=self.vm_id).first().name,
            "product_name": Stock.query.filter_by(id=self.product_id).first().product,
            "all_products_detail": self.get_all_product_stock(),
            "quantity": self.quantity,
            "time": self.time,
        }
