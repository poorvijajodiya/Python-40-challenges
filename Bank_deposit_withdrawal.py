def get_info():
    print("Welcome to the Python First National Bank.")
    name = input("Hello, what is your name: ").title()
    savings = int(input("How much money would you like to set up your savings account with: "))
    checking = int(input("How much money would you like to set up your checking account with: "))
    dict = {
        "Name":name,
        "savings":savings,
        "checking":checking,
    }
    return dict
def make_deposit(dict1,Type_of_acc,money_to_deposit):
        dict1[Type_of_acc] += money_to_deposit
        print("Deposited ${} into {}'s {} account.".format(money_to_deposit,dict1['Name'],Type_of_acc))


def make_withdrawal(dict,acc,money):
        if dict[acc]>=money:
            dict[acc] -=money
            print("Withdrew ${} from {}'s {} account".format(money,dict['Name'],acc))
        else:
            print("Sorry, by withdrawing ${} you will have a negative balance".format(money))

def display_info(dict):
    for k,v in dict.items():
        print("{} : {}".format(k,v))

def perform_transaction_again():
    res = input("Would you like to roll again(y/n)")
    if res.startswith('n'):
        flag = False
        print("Thank you for using the Python Dice App.")
    else:
        flag = True
    return flag

dict = get_info()
flag = True
while flag:
    display_info(dict)
    acc = input("What account would you like to access (Savings or Checking): ").lower()
    transaction = input("What type of transaction would you like to make (Deposit or Withdrawal): ").lower()
    money = int(input("How much money: "))
    if acc == 'savings'or acc == 'checking':
        if transaction == 'deposit':
            make_deposit(dict,acc,money)
        elif transaction == 'withdrawal':
            make_withdrawal(dict,acc,money)
        else:
            print("I'm sorry, we cannot do that for you today")
    else:
        print("I'm sorry, we cannot do that for you today")
    flag = perform_transaction_again()
