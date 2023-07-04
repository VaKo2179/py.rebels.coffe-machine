import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffemaker=CoffeeMaker()
moneymachine=MoneyMachine()
menu = Menu()




is_on =True

while is_on:
    items = menu.get_items()
    choise = input(f"Enter the name of the drink:{items} ")
    if choise=="off":
        is_on=False
    elif choise=="report":
        report = coffemaker.report()
        report1 = moneymachine.report()
    else:
        drink=menu.find_drink(choise)
        if coffemaker.is_resource_sufficient(drink):
             if(moneymachine.make_payment(drink.cost)):
                  coffemaker.make_coffee(drink)














"""drink = menu.find_drink(order_name)

if drink:
    print(f"The {order_name} costs {drink.cost} and requires:")
    for ingredient, amount in drink.ingredients.items():
        print(f"- {amount} ml of {ingredient}")

coin = MoneyMachine()
cost = 2.6
make_payment = coin.make_payment(cost)

coffeemaker = CoffeeMaker()
drink = menu.find_drink(order_name)
is_sufficient = coffeemaker.is_resource_sufficient(drink)

if is_sufficient and make_payment:
    coffeemaker.make_coffee(drink)
"""
