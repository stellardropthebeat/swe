import json
import sqlite3

class VendingMachine:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.stock = {}
    
    def add_product(self, product, quantity):
        self.stock[product] = quantity
        
    def remove_product(self, product):
        del self.stock[product]
        
    def update_product(self, product, quantity):
        self.stock[product] = quantity
        
    def list_products(self):
        for product, quantity in self.stock.items():
            print(f"Product: {product}, Quantity: {quantity}")
            
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class VendingMachineManager:
    def __init__(self):
        self.conn = sqlite3.connect('vendingmachines.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS VendingMachine
                           (ID INT PRIMARY KEY NOT NULL,
                           NAME TEXT NOT NULL,
                           LOCATION TEXT NOT NULL);''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS Stock
                           (ID INT PRIMARY KEY NOT NULL,
                           VMID INT NOT NULL,
                           PRODUCT TEXT NOT NULL,
                           QUANTITY INT NOT NULL);''')
        self.conn.commit()
        
    def add_machine(self, name, location):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO VendingMachine (NAME, LOCATION) VALUES (?,?)", (name, location))
        self.conn.commit()
        print(f"Vending machine {name} with location {location} created successfully")
        
    def remove_machine(self, name):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM VendingMachine WHERE NAME = ?", (name,))
        self.conn.commit()
        print(f"Vending machine {name} removed successfully")
        
    def update_machine(self, name, location):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE VendingMachine SET LOCATION = ? WHERE NAME = ?", (location, name))
        self.conn.commit()
        print(f"Vending machine {name} location updated to {location}")
    
    def add_product(self, machine_name, product, quantity):
        cursor = self.conn.cursor()
        cursor.execute("SELECT ID from VendingMachine WHERE NAME = ?", (machine_name,))
        vm_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO Stock (VMID, PRODUCT, QUANTITY) VALUES (?,?,?)", (vm_id, product, quantity))
        self.conn.commit()
        print(f"Product {product} with quantity {quantity} added to vending machine {machine_name}")
    
    def list_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Stock")
        products = cursor.fetchall()
        return products

    def list_products_by_machine(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT VendingMachine.NAME, Stock.PRODUCT, Stock.QUANTITY FROM VendingMachine INNER JOIN Stock ON VendingMachine.ID = Stock.VMID")
        products = cursor.fetchall()
        products_by_machine = {}
        for product in products:
            if product[0] in products_by_machine:
                products_by_machine[product[0]].append({'product':product[1], 'quantity':product[2]})
            else:
                products_by_machine[product[0]] = [{'product':product[1], 'quantity':product[2]}]
        return products_by_machine



   
