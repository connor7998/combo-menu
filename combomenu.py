def get_yes_no(prompt):
    return input(prompt).strip().upper().startswith('Y')

def order_sandwich():
    flag = get_yes_no("Do you want a sandwich? Y/N: ")
    if not flag:
        print("Skipping sandwich")
        return None, 0.0
    
    print("* Sandwich Menu *")
    print("chicken $5.25")
    print("beef $6.25")
    print("tofu $5.75")
    print("chorizo $7.50")
    
    type_sandwich = input("What type of sandwich would you like? chicken, beef, tofu or chorizo: ").strip().lower()
    if type_sandwich in ("chicken", "beef", "tofu", "chorizo"):
        cost = {"chicken": 5.25, "beef": 6.25, "tofu": 5.75, "chorizo": 7.50}[type_sandwich]
        print(f"You ordered a {type_sandwich} sandwich")
        return type_sandwich, cost
    else:
        print("Error: Invalid sandwich type")
        return None, 0.0

def order_beverage():
    flag = get_yes_no("Do you want a beverage? Y/N: ")
    if not flag:
        print("Skipping beverage")
        return None, 0.0
    
    print("* Beverage Menu *")
    print("small $1.00")
    print("medium $1.75")
    print("large $2.25")
    print("extra large $2.75")
    
    size = input("What size would you like? S/M/L/XL: ").strip().upper()
    if size in ("S", "M", "L", "XL"):
        cost = {"S": 1.00, "M": 1.75, "L": 2.25, "XL": 2.75}[size]
        print(f"You ordered a {size} beverage")
        return size, cost
    else:
        print("Error: Invalid beverage size")
        return None, 0.0

def order_frenchfries():
    flag = get_yes_no("Do you want french fries? Y/N: ")
    if not flag:
        print("Skipping french fries")
        return None, 0.0
    
    print("* French Fries Menu *")
    print("small $1.00")
    print("medium $1.50")
    print("large $2.00")
    
    size = input("What size would you like? S/M/L: ").strip().upper()
    if size in ("S", "M", "L"):
        if size == "S":
            mega = get_yes_no("Do you want to mega size your french fries? Y/N: ")
            if mega:
                size = "L"
                cost = 2.00
            else:
                cost = 1.00
        elif size == "M":
            cost = 1.50
        else:
            cost = 2.00
        print(f"You ordered {size} french fries")
        return size, cost
    else:
        print("Error: Invalid french fries size")
        return None, 0.0

def order_ketchup():
    while True:
        try:
            num = int(input("How many ketchup packets would you like? Cost $0.25 each: ").strip())
            if num < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a non-negative whole number.")
    
    cost = num * 0.25
    print(f"You ordered {num} packets of ketchup")
    return num, cost

print("Welcome to Good Burger, home of the Good Burger! Can I take your order?")
print("Welcome to My Restaurant")

order_list = []
total_cost = 0.0

# Initial order
sandwich_item, sandwich_cost = order_sandwich()
if sandwich_item:
    order_list.append(sandwich_item)
    total_cost += sandwich_cost

beverage_item, beverage_cost = order_beverage()
if beverage_item:
    order_list.append(beverage_item)
    total_cost += beverage_cost

fries_item, fries_cost = order_frenchfries()
if fries_item:
    order_list.append(fries_item)
    total_cost += fries_cost

ketchup_item, ketchup_cost = order_ketchup()
order_list.append(ketchup_item)
total_cost += ketchup_cost

# Discount
if sandwich_item and beverage_item and fries_item:
    total_cost -= 1.00

# Display order and total
print("Your order:", order_list)
print(f"Total cost of your order is: ${total_cost:.2f}")

# Loop for additional orders
while True:
    again = get_yes_no("Would you like to order again? Y/N: ")
    if not again:
        break
    
    # Re-use the ordering functions for additional items
    sandwich_item, sandwich_cost = order_sandwich()
    if sandwich_item:
        order_list.append(sandwich_item)
        total_cost += sandwich_cost
    
    beverage_item, beverage_cost = order_beverage()
    if beverage_item:
        order_list.append(beverage_item)
        total_cost += beverage_cost
    
    fries_item, fries_cost = order_frenchfries()
    if fries_item:
        order_list.append(fries_item)
        total_cost += fries_cost
    
    ketchup_item, ketchup_cost = order_ketchup()
    order_list.append(ketchup_item)
    total_cost += ketchup_cost
    
    # Re-apply discount if all three main items are present
    if sandwich_item and beverage_item and fries_item:
        total_cost -= 1.00
    
    print("Updated order:", order_list)
    print(f"Updated total cost: ${total_cost:.2f}")