def load_inventory():
    global inventory_list
    inventory_list = []
    try:
        with open("inventory.txt", "r") as file:
            for every_item in file:
                inventory_list.append(every_item.strip())
                #xxx.strip() removes any whitespace characters from the beginning and end of the string, including newline characters.
            print("Current Inventory:", inventory_list)
            return inventory_list
            
    except FileNotFoundError:
        # intended to handle the case where the inventory file does not exist yet
        return []
    #Eg: int("apple") results in code error.

def save_inventory(listed_inventory):
    with open("inventory.txt", "w") as file:
        for every_item in listed_inventory:
            file.write(str(every_item) + "\n")
        #This adds a new line after each item in the inventory list when saving to the file
        #ensuring that each item is on a separate line in the text file.

def get_valid_input():

    item_name = input("Enter product name: ")
    if item_name.lower() == "quit":
        return "quit"
    
    item_quantity = input("Enter product quantity: ")

    if not item_quantity.isdigit() or int(item_quantity) <= 0:
    # For incorrect non-integer, string or '0' input
        print("Error: Please enter a valid number")
        return None

    else:
        return item_name, int(item_quantity)

def current_order_list(inventory_items):
    print("Current Orders: \n")
    for item in inventory_items:
        #print(inventory_items.index(item) + 1001, ",", item[0], ",", item[1])
        # Output: 1001 (ID) , ProductName , Quantity
        print(item)
    print()

def process_delivery(current_total, new_value): #(a, b)
    inventoryQuantity = current_total + new_value
    return inventoryQuantity
# inventory += new_value
# Essentially, helps to keep track of the total units processed in the inventory

#def calculate_tax(new_value):
    #tax_rate = 0.10
    #return round(float(tax_rate * new_value), 2)


def generate_report(inventoryQuantity, error):
    print("Total Units Processed: ", inventoryQuantity)
    print("Number of Failed Entries: ", error)
    current_order_list(inventory)

inventoryQuantity = 0
inventory = load_inventory()
error = 0
# stock is the new stock quantity input by the user
# inventory is now a list, NOT an integer

while True:
    new_order = get_valid_input()

    if new_order == "quit":
        save_inventory(inventory)
        print("\nOrder successfully saved to order.txt.")
        generate_report(inventoryQuantity, error)
        break

    if new_order is None:
    # For incorrect non-integer, string or '0' input
        error += 1
        continue

    else:
        item_name, item_quantity = new_order
        order_id = 1001 + len(inventory_list)
        formatted_line = f"{order_id}, {item_name}, {item_quantity}"
        inventory_list.append(formatted_line)
        inventoryQuantity = process_delivery(inventoryQuantity, item_quantity)
        print ("\nNew Order Added: \n", new_order[0], ", ", new_order[1])
        if inventoryQuantity > 500:
            print("Alert! Stock input exceeds maximum inventory capacity of 500 units.")
            generate_report(inventoryQuantity, error)
            break
        else:
            continue
