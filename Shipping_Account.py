print("Welcome to the Shipping Accounts Program\n")
ls = ["john","mike","jasmine","george","kelvin"]
name = input("Hello, what is your username: ").lower()
if name in ls:
    print("Hello {}. Welcome back to your account.".format(name))
    print("Current shipping prices are as follows:")
    print("Shipping orders 0 to 100: $5.10 each")
    print("Shipping orders 100 to 500: $5.00 each")
    print("Shipping orders 500 to 1000: $4.95 each")
    print("Shipping orders over 1000: $4.80 each")
    item_ship = int(input("How many items would you like to ship: "))
    if item_ship < 100:
        a = 5.10
    elif item_ship < 500:
        a = 5.00
    elif item_ship < 1000:
        a = 4.95
    else:
        a = 4.80
    cost_of_shipping = item_ship*a
    cost_of_shipping = round(cost_of_shipping,2)
    print("To ship {} items it will cost you {} at {} per item".format(item_ship, cost_of_shipping,a))
    j = input("Would you like to place this order (y/n): ")
    if j.startswith('y'):
        print("Okay. Shipping your {} items.".format(item_ship))
    else:
        print("No order has been placed")
else:
    print("Sorry, you do not have an account with us. Goodbye.")




