import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.quantity} {self.name} for {self.price} GEL"
    
def serialization(object):
    if isinstance(object, Product):
        return {
            "Name": object.name,
            "Price": object.price,
            "Quantity": object.quantity
        }
    return object

def deserialization(object):
    return Product(object["Name"], object["Price"], object["Quantity"])

lst = []
pr1 = Product("apple", 2, 10)
pr2 = Product("juice", 20, 3)
pr3 = Product("TV", 1000, 1)

lst.append(pr1)
lst.append(pr2)
lst.append(pr3)


with open("products.json", "w") as json_file:
    json.dump(lst, json_file, default=serialization, indent=2)


with open("products.json", "r") as json_file:
    python_data = json.load(json_file, object_hook=deserialization)


for i in python_data:
    print(i)