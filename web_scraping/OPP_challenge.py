"""
Create a simple inventory management system. This project would cover several key concepts, such as object-oriented programming, file I/O, and data manipulation. Here are the requirements for the project:
Create a class for the inventory item, with the following attributes: name, quantity, and price.
Create a class for the inventory management system, with the following methods:
add_item: allows the user to add a new item to the inventory
remove_item: allows the user to remove an item from the inventory
update_item: allows the user to update the quantity or price of an item
display_inventory: displays the current inventory
Allow the user to load and save the inventory from/to a CSV file
Create a simple UI that allows the user to interact with the inventory management system through a menu.
This project would be a great opportunity for you to practice and solidify your understanding of OOP concepts, data manipulation, and file I/O. Additionally, the project will be a great opportunity for you to learn about the best practices for building a simple user interface, which is an essential part of software development.
"""
import csv
class Item:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class InventoryManagementSystem:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
            self.inventory.append(item)

    def remove_item (self, item):
        self.inventory = [item for item in self.inventory if item.name != item_name]


    def display_inventory(self):
        for item in self.inventory:
            return(
                f"Name: {item.name}, Quantity: {item.quanity}, Price: {item.price}")

   # def remove_item (sef, item):
        #self.invent

inventory = InventoryManagementSystem()
        
item_1 = Item("chairs", 22, 1500)
item_2 = Item("books", 20, 220)
item_3 = Item("pens",30,50)

inventory.add_item(item_1)
inventory.add_item(item_2)
inventory.add_item(item_3)

# for item in self.inventory:
#             if item.name == item_name:
#                 if new_quantity is not None:
#                     item.quantity = new_quantity
#                 if new_price is not None:
#                     item.price = new_price

# def save_to_csv(self, filename):
#          with open(filename, mode='w', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(['Name', 'Quantity', 'Price'])
#             for item in self.inventory:
#                 writer.writerow([item.name, item.quantity, item.price])
  



