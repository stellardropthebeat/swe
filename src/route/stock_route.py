"""Stock API route."""

from flask import Blueprint, Response, jsonify, render_template, request
from sqlalchemy.orm import collections

from src.database.model import Stock
from src.services.stock_services import StockManager

stock_controller: Blueprint = Blueprint("stock_controller", __name__)


@stock_controller.route("/stock")
def stocks() -> str:
    """Stock page."""
    return render_template("stock.html")


@stock_controller.route("/add_product", methods=["POST"])
def add_product() -> tuple[Response, int]:
    """Add product to vending machine."""
    vm_id: int = request.json["vm_id"]
    product: str = request.json["product"]
    quantity: int = request.json["quantity"]
    manager: StockManager = StockManager()
    product_id: int = manager.create_product(vm_id, product, quantity)
    return jsonify(success=True, message="Product added successfully", id=product_id), 201


@stock_controller.route("/update_product_quantity/<int:product_id>", methods=["PUT"])
def update_product_quantity(product_id: int) -> tuple[Response, int]:
    """Update product in vending machine."""
    manager: StockManager = StockManager()
    updated_product: Stock = Stock.query.filter_by(id=product_id).first()
    quantity: int = request.json.get("quantity", updated_product.quantity)
    manager.update_product_quantity(product_id, quantity=quantity)
    return jsonify(success=True, message="product updated successfully"), 200


@stock_controller.route("/update_product_name/<int:product_id>", methods=["PUT"])
def update_product_name(product_id: int) -> tuple[Response, int]:
    """Update product in vending machine."""
    manager: StockManager = StockManager()
    updated_product: Stock = Stock.query.filter_by(id=product_id).first()
    product: str = request.json.get("product", updated_product.product)
    manager.update_product_name(product_id, product=product)
    return jsonify(success=True, message="product updated successfully"), 200


@stock_controller.route("/delete_product/<int:product_id>", methods=["DELETE"])
def delete_product(product_id: int) -> tuple[Response, int]:
    """Delete product from vending machine."""
    manager: StockManager = StockManager()
    manager.delete_product(product_id)
    return jsonify(success=True, message="Product deleted successfully"), 200


@stock_controller.route("/all_products", methods=["GET"])
def get_all_products() -> tuple[Response, int]:
    """Get all products from vending machine."""
    products: collections.Iterable = Stock.query.all()
    products_list: list = [product.to_dict() for product in products]
    return jsonify(products_list), 200
