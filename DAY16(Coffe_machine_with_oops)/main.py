from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

a = MoneyMachine()
b = CoffeeMaker()
c = Menu()

while 1:
    choice = input(f"What do you want {c.get_items()}")
    if choice == "report":
        a.report()
        b.report()
    elif choice == "off":
        break
    else:
        d = c.find_drink(choice)
        if b.is_resource_sufficient(d) and a.make_payment(d.cost):
            b.make_coffee(d)

