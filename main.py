MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def checker(coffee_type):
    result = {}
    if coffee_type in MENU:
        ingredients = MENU[coffee_type]["ingredients"]
        for key in ingredients:
            if key in resources:
                if resources[key] - ingredients[key] >= 0:
                    result[key] = resources[key] - ingredients[key]
                else:
                    print(f"There is not enough {key} for {coffee_type}")
                    return False
            else:
                print(f"Invalid resource: {key}")
                return False
    else:
        print("Invalid coffee type")
        return False

    return result

def coin_generator(coffee_type):
    print("Please insert your coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    quarter = 0.25
    dime = 0.10
    nickel = 0.05
    penny = 0.01

    total_amount = (quarter * quarters) + (dime * dimes) + (nickel * nickels) + (penny * pennies)

    if total_amount >= MENU[coffee_type]["cost"]:
        left_coins = total_amount - MENU[coffee_type]["cost"]
        resources["money"] += MENU[coffee_type]["cost"]
        print(f"Take your {coffee_type} and your change: {round(left_coins, 2)}")
        return True
    else:
        print("You don't have enough money")
        return False


def make_coffee(coffee_type):
    if checker(coffee_type):
        ingredients = MENU[coffee_type]["ingredients"]
        for key in ingredients:
            resources[key] -= ingredients[key]
        print(f"Here is your {coffee_type}. Enjoy!")

anymore = True
while anymore:
    global_coffee_type = input("What would you like: (espresso/latte/cappuccino/off) ")
    if global_coffee_type == "off":
        print("Bye!")
        break
    else:
        result = checker(global_coffee_type)
        if result:
            if coin_generator(global_coffee_type):
                make_coffee(global_coffee_type)







