inventory = 0
error = 0

while True:
    stock = input("Enter a stock quantity: ")

    if stock.lower() == "quit": 
        print("Total Units Processed: ", inventory)
        print("Number of Failed Entries: ", error)
        break
    
    elif stock.isdigit() and int(stock) > 0:

        if int(stock) + inventory > 500:
            error += 1
            print("Alert! Stock input exceeds maximum inventory capacity of 500 units.")
            print("Total Units Processed: ", inventory)
            print("Number of Failed Entries: ", error)
            break

        inventory += int(stock)
        
    else:
        error += 1
        print("Error: Please enter a valid number")
        continue



        