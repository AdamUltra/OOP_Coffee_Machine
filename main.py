from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_machine = CoffeeMaker()
Menu_items = Menu()
Money = MoneyMachine()
go = True
while go:
    UInp = input(f'What would you like to have? {Menu_items.get_items()}').lower()
    if UInp == 'report':
        coffee_machine.report()
        Money.report()

    elif UInp == 'off':
        quit()

    else:
        if Menu_items.find_drink(UInp) is None:
            continue

        else:
            Item = Menu_items.find_drink(UInp)
            if coffee_machine.is_resource_sufficient(Item):
                pay = True
                print(Item.cost)
                while pay:
                    if Money.make_payment(Item.cost):
                        coffee_machine.make_coffee(Item)
                        pay = False

                    else:
                        pay = True
