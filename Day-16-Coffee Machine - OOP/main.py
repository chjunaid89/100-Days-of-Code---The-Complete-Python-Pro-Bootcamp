from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
my_coffee_maker = CoffeeMaker()
payment = MoneyMachine()

power_on = True
while power_on:
    choice = input(f'What would you like? ({coffee.get_items()}):').lower()
    if choice == 'off':
        power_on = False
    elif choice == 'report':
        my_coffee_maker.report()
        payment.report()
    else:
        drink = coffee.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink):
            drink_cost = drink.cost
            if payment.make_payment(drink_cost):
                my_coffee_maker.make_coffee(drink)

