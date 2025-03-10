

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
profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Function that checks resources. It inputs order_ingredients which is the based on the ingredients from the chosen drink.
def is_resource_sufficient(order_ingredients):
    is_enough = True
    """This takes the item selected and pulls the ingredients """
    for item in order_ingredients:
        """Then makes sure there is enough resources and if there isnt then it stops the program """
        if order_ingredients[item] >= resources[item]:
            print (f" Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total Calculated from coins inserted."""
    print("Please insert coins")
    total = int (input("Home many quarters?: ")) * .25
    total += int(input("Home many dimes?: ")) * .10
    total += int(input("Home many nickles?: ")) * .05
    total += int(input("Home many pennies?: ")) * .01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepeted or False if money is insufficient ."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        return False
        print("Sorry that's not enough money. Money Refunded")


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")



is_on = True
while True:
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        print("Machine is off!")
        is_on = False
        break
    elif choice == "report":
        print (f"Water: {resources['water']}ml")
        print (f"Milk: {resources['milk']}ml")
        print (f"Coffee: {resources['coffee']}g")
        print (f"Money: ${profit}")
    else:
        drink = MENU[choice]
        is_resource_sufficient(drink['ingredients'])

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])
