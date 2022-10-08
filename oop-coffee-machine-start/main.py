from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

report_payment = MoneyMachine()
coffee_menu = Menu()
make_coffee = CoffeeMaker()

is_on = True
items = coffee_menu.get_items()

while is_on:
    choice = input(f"What would you like? ({items}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        make_coffee.report()
        report_payment.report()
    else:
        drink = coffee_menu.find_drink(choice)
        if drink is not None:
            if make_coffee.is_resource_sufficient(drink):
                if report_payment.make_payment(drink.cost):
                    make_coffee.make_coffee(drink)
