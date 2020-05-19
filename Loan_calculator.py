from matplotlib import pyplot
def get_loan_info():
    loan = {}
    p = float(input("Enter the loan amount: "))
    r = float(input("Enter the interest rate: "))
    month_pay = float(input("Enter the desired monthly payment amount"))
    loan['Principal'] = p
    loan['Rate'] = r/100
    loan['Monthly_payment'] = month_pay
    loan['money_paid'] = 0
    return  loan

def show_loan_info(loan,month_num):
    print("----Loan information after {} months----".format(month_num))
    for k,v in loan.items():
        print("{}:{}".format(k,v))

def collect_interest(loan):
    loan['Principal'] = loan['Principal'] + loan['Principal']*loan['Rate']/12

def make_monthly_payment(loan):
    loan['Principal'] = loan['Principal'] - loan['Monthly_payment']
    if loan['Principal']>0:
        loan['money_paid'] += loan['Monthly_payment']
    else:
        loan['money_paid'] += loan['Monthly_payment'] + loan['Principal']
        loan['Principal'] = 0

def summarize_loan(loan, month_number,starting_principal):
    print("Congratulations! You paid off your loan in {} months!".format(month_number))
    print("Your initial loan was ${} at a rate of {}%".format(starting_principal,loan['Rate']*100))
    print("Your monthly payment was ${}".format(loan['Monthly_payment']))
    print("You spent ${} total.".format(round(loan['money_paid'],2)))
    print("You spent ${} on interest!".format(round(loan['money_paid']-starting_principal,2)))

def create_graph(data_to_plot,loan):
    x_values = []
    y_values = []
    for i in data_to_plot:
        x_values.append(i[0])
        y_values.append(i[1])
    pyplot.plot(x_values, y_values)
    pyplot.title(str(100 * loan['Rate']) + "% Interest" + " With $" + str(loan['Monthly_payment']) + " Monthly Payment")
    pyplot.xlabel("Month Number")
    pyplot.ylabel("Principal of loan")
    pyplot.show()


print("Welcome to the Loan Calculator App\n")
month_number = 0
loan = get_loan_info()
starting_principal = loan['Principal']
data_to_plot = []
show_loan_info(loan,month_number)
input("Press 'enter' to begin paying off your loan.")
while loan['Principal']>0:
    if loan['Principal']>starting_principal:
        break
    month_number +=1
    collect_interest(loan)
    make_monthly_payment(loan)
    data_to_plot.append((month_number,loan['Principal']))
    show_loan_info(loan,month_number)
if loan['Principal'] <= 0:
        summarize_loan(loan,month_number,starting_principal)
        create_graph(data_to_plot,loan)
else:
        print("\nYou will NEVER pay off your loan!!!")
        print("You cannot get ahead of the interest! :-(")