"""Stock API route."""

from database.stock import Stock
from flask import Blueprint, Response, jsonify, render_template, request
from services.vending_machine_services import VendingMachineManager
from sqlalchemy.orm import collections

stock_controller: Blueprint = Blueprint("stock_controller", __name__)

failed_message: str = "Product not found"


@stock_controller.route("/stock")
def stocks() -> str:
    """Stock page."""
    return render_template("stock.html")


@stock_controller.route("/add_product", methods=["POST"])
def add_product() -> Response | tuple[Response, int]:
    """Add product to vending machine."""
    vm_id: int = request.json["vm_id"]
    product: str = request.json["product"]
    quantity: str = request.json["quantity"]
    manager: VendingMachineManager = VendingMachineManager()
    manager.create_product(vm_id, product, quantity)
    return jsonify(success=True, message="Product added successfully"), 201


@stock_controller.route("/update_product/<int:id>", methods=["PUT"])
def update_product(product_id: int) -> Response | tuple[Response, int]:
    """Update product in vending machine."""
    manager: VendingMachineManager = VendingMachineManager()
    updated_product: Stock = manager.read_product(id=product_id)
    if updated_product:
        product: str = request.json.get("product", updated_product.product)
        quantity: int = request.json.get("quantity", updated_product.quantity)
        manager.update_product(product_id, product=product, quantity=quantity)
        return jsonify(success=True, message="product updated successfully")
    else:
        return jsonify(success=False, message="Vending machine not found"), 404


@stock_controller.route("/get_product/<int:id>", methods=["GET"])
def get_product(product_id: int) -> Response | tuple[Response, int]:
    """Get product from vending machine."""
    manager: VendingMachineManager = VendingMachineManager()
    product: Stock = manager.read_product(id=product_id)
    if product:
        return jsonify(success=True, product=product.to_dict())
    else:
        return jsonify(success=False, message=failed_message), 404


@stock_controller.route("/delete_product/<int:id>", methods=["DELETE"])
def delete_product(product_id: int) -> Response | tuple[Response, int]:
    """Delete product from vending machine."""
    manager: VendingMachineManager = VendingMachineManager()
    product_to_delete: Stock = manager.read_product(id=product_id)
    if product_to_delete:
        manager.delete_product(product_id)
        return jsonify(success=True, message="Product deleted successfully")
    else:
        return jsonify(success=False, message=failed_message), 404


@stock_controller.route("/all_products", methods=["GET"])
def get_all_products() -> Response | tuple[Response, int]:
    """Get all products from vending machine."""
    products: collections.Iterable = Stock.query.all()
    products_list: list = [product.to_dict() for product in products]
    return jsonify(products_list)
