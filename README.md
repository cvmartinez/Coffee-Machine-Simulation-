# Coffee-Machine-Simulation-

This project is a simple coffee machine simulator implemented in Python. It allows users to select from a menu of coffee drinks, processes payments, and checks resource availability to make the selected drink. The program also provides a report of the current resources and profit.

Features
Menu Selection: Choose from espresso, latte, or cappuccino.

Resource Management: The machine checks if there are enough resources (water, milk, coffee) to make the selected drink.

Payment Processing: The machine accepts coins (quarters, dimes, nickels, pennies) and calculates the total amount.

Transaction Handling: The machine checks if the payment is sufficient and provides change if necessary.

Resource Reporting: The machine can generate a report showing the current levels of resources and the total profit.

How to Use
Run the Program: Execute the Main.py script.

Select a Drink: When prompted, type the name of the drink you want (espresso, latte, or cappuccino).

Insert Coins: Follow the prompts to insert coins (quarters, dimes, nickels, pennies).

Receive Your Drink: If the payment is sufficient and there are enough resources, the machine will make your drink and provide any change.

Generate Report: Type "report" to see the current levels of resources and the total profit.

Turn Off the Machine: Type "off" to turn off the machine.

Code Structure
MENU Dictionary: Contains the ingredients and cost for each drink.

Resources Dictionary: Tracks the available resources (water, milk, coffee).

Profit Variable: Keeps track of the total profit.

Functions:

is_resource_sufficient(order_ingredients): Checks if there are enough resources to make the selected drink.

process_coins(): Processes the coins inserted by the user.

is_transaction_successful(money_received, drink_cost): Checks if the payment is sufficient and updates the profit.

make_coffee(drink_name, order_ingredients): Deducts the used resources and makes the coffee.

Example Usage
plaintext
Copy
What would you like? (espresso/latte/cappuccino): latte
Please insert coins
How many quarters?: 2
How many dimes?: 1
How many nickels?: 0
How many pennies?: 0
Here is $0.05
Here is your latte
