from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

money = 0
is_on = True


while is_on: 
    options = menu.get_items()
    order = input(f'What do you like ? {options} ? ')
    
    if order == 'off':
        break
    
    if order == 'report':
        coffe_maker.report()
        money_machine.report()
    
    else:
        drink = menu.find_drink(order_name=order)
        if coffe_maker.is_resource_sufficient(drink=drink) and (money_machine.make_payment(drink.cost)): 
            coffe_maker.make_coffee(drink)
                