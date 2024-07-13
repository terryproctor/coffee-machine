import resources

menu = resources.MENU
resources = resources.resources

def print_resources():
    print("Resources:")
    for item in resources:
        print(f"{item}: {resources[item]}")
    return

def print_menu():
    menu_items = ""
    for item in menu:
        menu_items += f"{item} cost: {menu[item]['cost']}\n"
    
    return menu_items

def insert_money():
    pennies = int(input("How many pennies? ")) 
    nickels = int(input("How many nickels? ")) * 5
    dimes = int(input("How many dimes? ")) * 10
    quarters = int(input("How many quarters? ")) * 25
    print("\n")
    return (pennies + nickels + dimes + quarters) / 100

def get_selection():
    print_menu()
    on = True
    while on:
        selection = input("What would you like? ")
        if selection in menu:
            return selection
        elif selection == "off":
            on = False
            print("Machine has been turned off")
        else:
            print("Invalid selection")
        return on
    

def check_enough_money(selection, money):
    if money < menu[selection]['cost']:
        print("Not enough money")
        return False
    return True

def check_resources(selection):
    for item in menu[selection]['ingredients']:
        if resources[item] < menu[selection]['ingredients'][item]:
            return False
    return True

def get_change(selection, money):
    change = money - menu[selection]['cost']
    if change < 0:
        return money
    return change

def make_coffee(selection):
    for item in menu[selection]['ingredients']:
        resources[item] -= menu[selection]['ingredients'][item]
    return

def main():
    print_resources()
    print("\n")
    print(print_menu())
    selection = get_selection()
    if selection == False:
        return
    money = insert_money()
    if check_enough_money(selection, money):
        if check_resources(selection):
            change = get_change(selection, money)
            if change >= 0:
                make_coffee(selection)
                print(f"Here is your {selection} and your change is {change}")
        else:
            print("Not enough resources")
    else:
        print("Not enough money")
main()