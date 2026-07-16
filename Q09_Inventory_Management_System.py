def search_product(inventory, s_id):
    if s_id in inventory:
        info = inventory[s_id]
        print("========== PRODUCT ==========")
        print(f"ID       : {s_id}")
        print(f"Name     : {info['name']}")
        print(f"Price    : {info['price']}")
        print(f"Quantity : {info['quantity']}")
    else:
        print("Product Not Found")


def update_quantity(inventory, s_id, quantity):
    if s_id in inventory:
        inventory[s_id]["quantity"] += quantity
        print("Quantity Updated Successfully")
    else:
        print("Product Not Found")


def sell(inventory, s_id, quantity):
    if s_id in inventory:
        info = inventory[s_id]

        if info["quantity"] >= quantity:
            info["quantity"] -= quantity
            print("Sale Successful")
            print(f"Remaining Quantity : {info['quantity']}")
        else:
            print("Insufficient Stock")
    else:
        print("Product Not Found")


def display(inventory):
    print("=============== INVENTORY ===============")

    for pid, info in inventory.items():
        print("========== PRODUCT ==========")
        print(f"ID       : {pid}")
        print(f"Name     : {info['name']}")
        print(f"Price    : {info['price']}")
        print(f"Quantity : {info['quantity']}")
        print()


n = int(input("Enter the number of total products: "))

inventory = {}

for i in range(n):
    pid, name, price, quantity = input(
        f"Enter the information of {i+1}th product: "
    ).split()

    inventory[int(pid)] = {
        "name": name,
        "price": int(price),
        "quantity": int(quantity)
    }


while True:
    print("\n===== MENU =====")
    print("1. Search Product")
    print("2. Update Quantity")
    print("3. Sell Product")
    print("4. Display Inventory")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pid = int(input("Enter Product ID: "))
        search_product(inventory, pid)

    elif choice == 2:
        pid = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity to Add: "))
        update_quantity(inventory, pid, quantity)

    elif choice == 3:
        pid = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity to Sell: "))
        sell(inventory, pid, quantity)

    elif choice == 4:
        display(inventory)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")