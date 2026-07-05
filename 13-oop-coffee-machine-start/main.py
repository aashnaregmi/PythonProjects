from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()





def welcome_msg():
    print("=" * 45)
    print("      ☕ WELCOME TO COFFEE MACHINE ☕")
    print("=" * 45)

    print("\nHello! What would you like today?\n")

    print("📋 MENU")
    print("-" * 45)
    print("☕ Espresso      - $1.50")
    print("🥛 Latte         - $2.50")
    print("☕🥛 Cappuccino   - $3.00")
    print("-" * 45)

    print("\nCommands:")
    print("• espresso")
    print("• latte")
    print("• cappuccino")
    print("• report  - View machine resources")
    print("• off     - Turn off the coffee machine")
    print("=" * 45)




welcome_msg()

is_on = True

while is_on:
    options=menu.get_items()
    order = input(f"What is your order( {options})? ").lower()

    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(order)
        resource_enough=coffee_maker.is_resource_sufficient(drink)
        if resource_enough:
            money_enough=money_machine.make_payment(drink.cost)
            if money_enough:
               coffee_maker.make_coffee(drink)
              
         

   
