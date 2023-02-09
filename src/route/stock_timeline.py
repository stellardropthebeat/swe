"""Stock timeline route."""

from flask import Blueprint, Response, jsonify
from sqlalchemy.orm import collections

from src.database.model import StockTimeLine

stock_timeline_controller: Blueprint = Blueprint("stock_timeline_controller", __name__)


@stock_timeline_controller.route("/stock_timeline/product/<int:product_id>", methods=["GET"])
def get_stock_timeline(product_id: int) -> tuple[Response, int]:
    """Get stock timeline."""
    stock_timeline: collections.Iterable = StockTimeLine.query.filter_by(product_id=product_id).all()
    stock_timeline_list: list = [stock_timeline.to_dict() for stock_timeline in stock_timeline]
    return jsonify(stock_timeline_list), 200


@stock_timeline_controller.route("/stock_timeline/vm/<int:vm_id>", methods=["GET"])
def get_stock_timeline_by_vm(vm_id: int) -> tuple[Response, int]:
    """Get stock timeline."""
    stock_timeline: collections.Iterable = StockTimeLine.query.filter_by(vm_id=vm_id).all()
    stock_timeline_list: list = [stock_timeline.to_dict() for stock_timeline in stock_timeline]
    return jsonify(stock_timeline_list), 200
