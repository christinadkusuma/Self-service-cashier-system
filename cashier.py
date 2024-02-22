# -*- coding: utf-8 -*-
"""Cashier

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19_2U46kx6YI0U-dIPMgrreYARYRE1bTU
"""

from tabulate import tabulate

class Transaction:
    def __init__(self):
        """
        Initialize an empty list to store transaction items.

        Attributes:
        - items (list): Consist of items which are bought.
        """
        self.items = []

    def display_menu(self):
        """
        Display the menu options for user interaction.
        """
        print("\nMenu:")
        print("1. Add Item")
        print("2. Update Item Name")
        print("3. Update Item Quantity")
        print("4. Update Item Price")
        print("5. Delete Item")
        print("6. Reset Transaction")
        print("7. Check Order")
        print("8. Total Price")
        print("0. Exit")

    def run_menu(self):
        """
        Run the main menu for user interaction.
        """
        while True:
            self.display_menu()
            choice = input("Choose an option (0-8): ")

            if choice == '0':
                break
            elif choice == '1':
                self.add_item()
            elif choice == '2':
                self.update_item_name()
            elif choice == '3':
                self.update_item_qty()
            elif choice == '4':
                self.update_item_price()
            elif choice == '5':
                self.delete_item()
            elif choice == '6':
                self.reset_transaction()
            elif choice == '7':
                self.check_order()
            elif choice == '8':
                self.total_price()
            else:
                print("Invalid option. Please choose a correct option.")

    def add_item(self):
        """
        Add a new item to the transaction.
        """
        name_item = input("Enter item name: ")
        quantity_item = int(input("Enter item quantity: "))
        price_item = int(input("Enter price per item: "))
        self.items.append([name_item, quantity_item, price_item])
        print(f"Item '{name_item}' added.")

    def update_item_name(self):
        """
        Update the name of an existing item in the transaction.
        """
        old_name = input("Enter the name of the item to be updated: ")
        new_name = input("Enter the new name: ")
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name
                print(f"Item name '{old_name}' updated to '{new_name}'.")
                return
        print(f"Item with name '{old_name}' not found.")

    def update_item_qty(self):
        """
        Update the quantity of an existing item in the transaction.
        """
        name = input("Enter the name of the item to update quantity: ")
        new_qty = int(input("Enter the new quantity: "))
        for item in self.items:
            if item[0] == name:
                item[1] = new_qty
                print(f"Item quantity '{name}' updated to {new_qty}.")
                return
        print(f"Item with name '{name}' not found.")

    def update_item_price(self):
        """
        Update the price of an existing item in the transaction.
        """
        name = input("Enter the name of the item to update price: ")
        new_price = int(input("Enter the new price: "))
        for item in self.items:
            if item[0] == name:
                item[2] = new_price
                print(f"Item price '{name}' updated to {new_price}.")
                return
        print(f"Item with name '{name}' not found.")

    def delete_item(self):
        """
        Delete an item from the transaction.
        """
        name = input("Enter the name of the item to delete: ")
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print(f"Item '{name}' deleted.")
                return
        print(f"Item with name '{name}' not found.")

    def reset_transaction(self):
        """
        Reset the transaction by clearing all items.
        """
        if self.items:
            print("All transactions reset.")
            self.items = []
        else:
            print("No transactions to reset.")

    def check_order(self):
        """
        Check the order for any input errors and display the order details.
        """
        try:
            for item in self.items:
                if any(value is None for value in item):
                    raise ValueError("Input data error")
            print("Order is correct")

            headers = ["No", "Item Name", "Quantity", "Price/Item", "Total Price"]
            table_data = [[i + 1, item[0], item[1], item[2], item[1] * item[2]] for i, item in enumerate(self.items)]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        except ValueError as e:
            print(e)

    def total_price(self):
        """
        Calculate and display the total price with applicable discounts.
        """
        total = sum(item[1] * item[2] for item in self.items)
        discount = 0

        if total > 500000:
            discount = 0.1
        elif total > 300000:
            discount = 0.08
        elif total > 200000:
            discount = 0.05

        discounted_total = total - (total * discount)
        print(f"Total Purchase: Rp {total}")
        print(f"Discount: {discount * 100}%")
        print(f"Total Payable: Rp {discounted_total}")