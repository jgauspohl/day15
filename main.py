
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
    "water": 320,
    "milk": 200,
    "coffee": 100,
}


def payment(price):
    """Processes payment, giving back extra change or displaying not enough provided."""
    print("Please input moneys")
    quarters = int(input("Quarters: "))
    nickels = int(input("Nickels: "))
    dimes = int(input("Dimes: "))
    pennies = int(input("Pennies: "))

    quarters = quarters * 0.25
    nickels = nickels * 0.05
    dimes = dimes * 0.10
    pennies = pennies * 0.01

    total = quarters + nickels + dimes + pennies
    total2 = str(round(total, 2))

    if total >= price:
        refund = total - price
        refund2 = str(round(refund, 2))
        print(f"Total accepted. Refunded amount: ${refund2}")
    else:
        print(f"Sorry that's not enough money. ${total2} refunded.")


def check(x, y, z):
    """Checks available resources to make the selected drink with, as well as subtracts from total if enough is there"""
    if x > resources['water']:
        print("not enough water")
        exit()
    if y == 0:
        pass
    else:
        if y > resources['milk']:
            print("not enough milk")
            exit()

    if z > resources['coffee']:
        print("Not enough coffee")
        exit()
    resources['water'] = resources['water'] - x
    resources['milk'] = resources['milk'] - y
    resources['coffee'] = resources['coffee'] - z

# TODO 1. Print report of coffe machine resources
def report():
    """Displays current levels of resources"""
    x = resources['water']
    y = resources['milk']
    z = resources['coffee']
    print(f" Water: {x}ml \n Milk: {y}ml \n Coffee: {z}ml\n")


def choice(x):
    """User chooses which drink to create"""
    if x == "off":
        exit()
    elif x == "report":
        report()
    elif x == "espresso":
        check(x=MENU['espresso']['ingredients']['water'], z=MENU['espresso']['ingredients']['coffee'], y=0)
        payment(MENU['espresso']['cost'])
        print("Here is your espresso!")
    elif x == "latte":
        check(x=MENU['latte']['ingredients']['water'], y=MENU['latte']['ingredients']['milk'],
              z=MENU['latte']['ingredients']['coffee'])
        payment(MENU['latte']['cost'])
        print("Here is your latte!")
    elif x == "cappuccino":
        check(x=MENU['cappuccino']['ingredients']['water'],
              y=MENU['cappuccino']['ingredients']['milk'],
              z=MENU['cappuccino']['ingredients']['coffee'])
        payment(MENU['cappuccino']['cost'])
        print("Here is your cappuccino!")


print(report())
prompt = input("what would you like? (espresso/latte/cappuccino): ")
choice(prompt)
