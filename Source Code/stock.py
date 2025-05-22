class Item:
    def __init__(self,name,price,stock):
        self.name = name
        self.price= price
        self.stock = stock
    def add_stock(self, stock):
        if stock >0:
            self.stock += stock
            return True
        return False
    def remove_stock(self, stock):
        if 0<stock<=self.stock:
            self.stock -= stock
            return True
        return False

class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self, product):
        self.products[product.name] = product
    def remove_product(self, product):
        self.products.pop(product.name, None)
    def get_product(self, name):
        return self.products.get(name)
    def update_stock(self, product, amount, action):
        self.products[product.name] = product
        if not product:
            return False, "Product not found"
        if action == "add":
            success = Item.add_stock(amount)
        elif action == "remove":
            success = Item.remove_stock(amount)
        else:
            return False, "Invalid action"
        if success:
            return True, "Stock has been updated"
        else:
            return False, "Invalid amount or Insufficient stock"

    def list_products(self):
        return list(self.products.values())
