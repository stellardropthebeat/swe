"""Stock services Module."""

from src.app_init import db
from src.database.model import Stock


class StockManager:
    """Stock Manager Class."""

    def __init__(self: "StockManager") -> None:
        """Initialize a stock manager."""
        self.db = db

    def create_product(self: "StockManager", vm_id: int, product: str, quantity: int) -> int:
        """Create a new product in the stock table."""
        new_product: Stock = Stock(vm_id=vm_id, stock=product, quantity=quantity)
        # if new_product exists, update the quantity
        if Stock.query.filter_by(product=product).first():
            stock: Stock = Stock.query.filter_by(product=product).first()
            stock.quantity += quantity
            self.db.session.commit()
            return stock.id
        # else create a new product
        else:
            self.db.session.add(new_product)
            self.db.session.commit()
            return new_product.id

    def update_product_quantity(self: "StockManager", product_id: int, quantity: int) -> None:
        """Update a product quantity in the stock table."""
        stock: Stock = Stock.query.filter_by(id=product_id).first()
        stock.quantity += int(quantity)
        self.db.session.commit()
        self.db.session.close()

    def update_product_name(self: "StockManager", product_id: int, product: str) -> None:
        """Update a product name in the stock table."""
        stock: Stock = Stock.query.filter_by(id=product_id).first()
        stock.product = product
        self.db.session.commit()
        self.db.session.close()

    def delete_product(self: "StockManager", product_id: int) -> None:
        """Delete a product from the stock table."""
        stock: Stock = Stock.query.filter_by(id=product_id).first()
        self.db.session.delete(stock)
        self.db.session.commit()
        self.db.session.close()

    def get_random_id(self: "StockManager") -> int:
        """Get a random id from the stock table."""
        return self.db.session.query(Stock.id).order_by(db.func.random()).first()[0]
