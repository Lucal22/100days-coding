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


def handle_order(order):
    if order == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        new_order()

    else:
        five_cents = 0.5 * int(input('How many 5 cents coins? '))
        ten_cents = 0.10 * int(input('How many 10 cents coins? '))
        fifty_cents = 0.50 * int(input('How many 50 cents coins? '))
        money = five_cents+ten_cents+fifty_cents

        change = round(-1 * (MENU[order]["cost"] - money), 2)
        if change < 0:
            print('Not enough money')
            new_order()

        else:
            menu_ingredients = MENU[order]["ingredients"]
            for ingredient in menu_ingredients:
                resources[ingredient] = resources[ingredient] - \
                    menu_ingredients[ingredient]
                if resources[ingredient] < 0:
                    print('Not enough ingredients')
                    new_order()
                else:
                    print(f'Here is your order and the change is: ${change}')
                    new_order()


def new_order():
    order = input('Whats your order(espresso/latte/cappuccino)? ')
    handle_order(order)


new_order()
