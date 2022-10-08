MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
}


# TODO: 3. Print report.
def print_report(machines_profit):
    """Prints the report on available resources and profit"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${machines_profit}")


# TODO: 4. Check resources sufficient?
def check_available_resources(order_ingredients):
    """Checks if there are sufficient resources available in the machine"""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins.
def process_coins():
    """Total calculated from the coins inserted"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    rounded_total = round(total, 2)
    return rounded_total


# TODO: 6. Check transaction successful?
def check_transaction(drink_price, user_amount):
    """Return True if payment is accepted else returns False if money is insufficient"""
    if user_amount < drink_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if user_amount > drink_price:
            change = round(user_amount - drink_price, 2)
            print(f"Here is ${change} dollars in change.")
        return True


# TODO: 7. Make Coffee.
def make_coffee(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
def run_coffee_machine():
    is_on = True
    profit = 0
    while is_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            drink = MENU[user_choice]
            if check_available_resources(drink["ingredients"]):
                total_amount = process_coins()
                if check_transaction(drink["cost"], total_amount):
                    profit += drink["cost"]
                    make_coffee(drink["ingredients"])
                    print(f"Here is your {user_choice} ☕️. Enjoy!")
        elif user_choice == "report":
            print_report(profit)
        # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
        elif user_choice == "off":
            is_on = False
        else:
            print("Invalid entry. Please choose again")


run_coffee_machine()
