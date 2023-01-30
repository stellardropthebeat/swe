"""Stock services Module."""

from app_init import db
from database.stock import Stock


class StockManager:
    """Stock Manager Class."""

    def __init__(self: "StockManager") -> None:
        """Initialize a stock manager."""
        self.db = db

    def create_product(self: "StockManager", vm_id: int, product: str, quantity: int) -> int:
        """Create a new product in the stock table."""
        new_product: Stock = Stock(vm_id=vm_id, stock=product, quantity=quantity)
        self.db.session.add(new_product)
        self.db.session.commit()
        self.db.session.close()
        return new_product.id

    def read_product(self: "StockManager", product_id: int = None, product: str = None) -> Stock:
        """Read a product from the stock table."""
        if product_id:
            product: Stock = Stock.query.filter_by(id=product_id).first()
        elif product:
            product: Stock = Stock.query.filter_by(product=product).first()
        else:
            product: Stock = Stock.query.all()
        return product

    def update_product(self: "StockManager", product_id: int, product: str = None, quantity: int = None) -> None:
        """Update a product in the stock table."""
        stock: Stock = Stock.query.filter_by(id=product_id).first()
        if product:
            stock.product = product
        if quantity:
            stock.quantity = quantity
        self.db.session.commit()
        self.db.session.close()

    def delete_product(self: "StockManager", product_id: int) -> None:
        """Delete a product from the stock table."""
        stock: Stock = Stock.query.filter_by(id=product_id).first()
        self.db.session.delete(stock)
        self.db.session.commit()
        self.db.session.close()
