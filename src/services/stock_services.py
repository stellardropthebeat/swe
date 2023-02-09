"""Stock services Module."""

from src.app_init import db
from src.database.model import Stock, add_to_timeline


class StockManager:
    """Stock Manager Class."""

    def __init__(self: "StockManager") -> None:
        """Initialize a stock manager."""
        self.db = db

    def create_product(self: "StockManager", vm_id: int, product: str, quantity: int) -> int:
        """Create a new product in the stock table."""
        stock: Stock = Stock.query.filter_by(product=product).first()
        if stock:
            new_quantity: int = stock.quantity + int(quantity)
            stock.quantity = new_quantity
            add_to_timeline(vm_id, stock.id, new_quantity)
            self.db.session.commit()
            return stock.id
        else:
            new_product: Stock = Stock(vm_id=vm_id, stock=product, quantity=quantity)
            self.db.session.add(new_product)
            self.db.session.commit()
            add_to_timeline(vm_id, new_product.id, quantity)
            return new_product.id

    def update_product_quantity(self: "StockManager", product_id: int, quantity: int) -> None:
        """Update a product quantity in the stock table."""
        stock: Stock = Stock.query.filter_by(id=product_id).first()
        new_quantity: int = stock.quantity + int(quantity)
        stock.quantity = new_quantity
        add_to_timeline(stock.vm_id, product_id, new_quantity)
        self.db.session.commit()
        self.db.session.close()

    def update_product_name(self: "StockManager", product_id: int, product: str) -> None:
        """Update a product name in the stock table."""
        stock: Stock = Stock.query.filter_by(id=product_id).first()
        new_product_name: str = product
        stock.product = new_product_name
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
