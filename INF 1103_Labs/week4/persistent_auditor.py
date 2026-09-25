def load_inventory():
    inventory_list = []
    try:
        with open("inventory.txt", "r") as file:
            for every_item in file:
                inventory_list.append(int(every_item.strip()))
            print(inventory)
            return inventory
            
    except FileNotFoundError:
        print("Error: Unable to load inventory data, file not found.")
        return []


def save_inventory(listed_inventory):
    with open("inventory.txt", "w") as file:
        for every_item in listed_inventory:
            file.write(str(every_item) + "\n")


def get_valid_input():
    stock = input("Enter a stock quantity: ")

    if stock.lower() == "quit":
        return "quit"

    if not stock.isdigit() or int(stock) <= 0:
    # For incorrect non-interger, string or '0' input
        print("Error: Please enter a valid number")
        return None

    else:
        return int(stock)
    

def process_delivery(inventory, stock):
    inventory += stock
    return inventory
# Essentially, helps to keep track of the total units processed in the inventory


def calculate_tax(stock):
    tax_rate = 0.10
    return round(float(tax_rate * stock), 2)


def generate_report(inventory, error):
    print("Total Units Processed: ", inventory)
    print("Number of Failed Entries: ", error)


inventory = load_inventory()
error = 0
# stock is the new stock quantity input by the user
# inventory is now a list, NOT an integer

while True:
    stock = get_valid_input()
    if stock == "quit":
        generate_report(inventory, error)
        break

    if stock is None:
    # For incorrect non-interger, string or '0' input
        error += 1
        continue

    else:        
        inventory = process_delivery(inventory, stock)
        print("Amount of Tax for this delivery: $", calculate_tax(stock))
        if inventory > 500:
            print("Alert! Stock input exceeds maximum inventory capacity of 500 units.")
            generate_report(inventory, error)
            break
        else:
            continue

        



        