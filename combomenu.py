def get_yes_no(prompt):
    return input(prompt).strip().upper().startswith('Y')

print("Welcome to Good Burger, home of the Good Burger! Can I take your order?")
print(" Welcome to My Restaurant ")
cost = 0.0

# TODO (3.2.1 - Lists): Use a list to track the user's selections (i.e. the order)
order_list = []

# Sandwich Menu
flag_sandwich = get_yes_no("Do you want a sandwich? Y/N: ")
if flag_sandwich:
    print("* Sandwich Menu *")
    print("chicken $5.25")
    print("beef $6.25")
    print("tofu $5.75")
    print("chorizo $7.50")

    type_sandwich = input("What type of sandwich would you like? chicken, beef, tofu or chorizo: ").strip().lower()
    if type_sandwich in ("chicken", "beef", "tofu", "chorizo"):
        print("You ordered a " + type_sandwich + " sandwich")
        order_list.append(type_sandwich)
        if type_sandwich == "chicken":
            cost += 5.25
        elif type_sandwich == "beef":
            cost += 6.25
        elif type_sandwich == "tofu":
            cost += 5.75
        elif type_sandwich == "chorizo":
            cost += 7.50
    else:
        print("Error for sandwich")
else:
    print("skipping sandwich")
    order_list.append("")


# Beverage Menu
flag_beverage = get_yes_no("Do you want a beverage? Y/N: ")
if flag_beverage:
    print("* Beverage Menu *")
    print("small $1.00")
    print("medium $1.75")
    print("large $2.25")
    print("extra large $2.75")
    size_beverage = input("What size would you like? S/M/L/XL: ").strip().upper()
    if size_beverage in ("S", "M", "L", "XL"):
        print("You ordered a " + size_beverage + " beverage")
        order_list.append(size_beverage)
        if size_beverage == "S":
            cost += 1.00
        elif size_beverage == "M":
            cost += 1.75
        elif size_beverage == "L":
            cost += 2.25
        elif size_beverage == "XL":
            cost += 2.75
    else:
        print("Error for beverage size")
        order_list.append("")

# French Fries Menu
flag_frenchfries = get_yes_no("Do you want french fries? Y/N: ")
if flag_frenchfries:
    print("* French Fries Menu *")
    print("small $1.00")
    print("medium $1.50")
    print("large $2.00")
    size_frenchfries = input("What size would you like? S/M/L: ").strip().upper()
    if size_frenchfries in ("S", "M", "L"):
        order_list.append(size_frenchfries)
        if size_frenchfries == "S":
            mega = get_yes_no("Do you want to mega size your french fries? Y/N: ")
            if mega:
                size_frenchfries = "L"
                cost += 2.00
            else:
                cost += 1.00
        elif size_frenchfries == "M":
            cost += 1.50
        else:
            cost += 2.00

        print("You ordered " + size_frenchfries + " french fries")
    else:
        print("Error for french fries size")
        order_list.append("")

# Ketchup
while True:
    try:
        num_ketchup = int(input("How many ketchup packets would you like? Cost $0.25 each: ").strip())
        if num_ketchup < 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a non-negative whole number.")

print("You ordered " + str(num_ketchup) + " packets of ketchup")
cost += num_ketchup * 0.25
order_list.append(num_ketchup)
# Discount
if flag_sandwich and flag_beverage and flag_frenchfries:
    cost -= 1.00

# tell what they ordered
print(order_list)

# Total Cost
print(f"Total cost of your order is: ${cost:.2f}")
