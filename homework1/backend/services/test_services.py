import random
import string

from app_init import db
from database import vending_machine, stock

VendingMachine = vending_machine.VendingMachine
Stock = stock.Stock


def random_string_for_test():
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=10))


def filter_data(data: str, machine_id: int = 0):
    match data.lower():
        case "machine":
            machines = VendingMachine.query.order_by(VendingMachine.id)
            return [m for m in machines]
        case "stock":
            stocks = Stock.query.filter(Stock.machine_id == int(machine_id))
            if stocks is not None:
                return [s for s in stocks]
    return []


class Services:
    def __init__(self):
        self.db = db
