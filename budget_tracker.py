def main():
    print("Welcome to the Budget Tracker!")
    income = get_input("Please enter your total income: ")
    rent = get_input("Please enter your monthly rent: ")
    food = get_input("Please enter your monthly food expenses: ")
    transport = get_input("Please enter your monthly transport fees: ")

    budget = calculate_budget(income, rent, food, transport)
    display_results(budget)



def get_input(user_input):
    while True:
        try:
            value = float(input(user_input))
            if value > 0:
                return value        
            elif value <= 0:
                print ('Value must be greater than 0, please try again')
        except ValueError:
            print ('Please input a valid integer.')        

def calculate_budget(income, rent, food, transport):

    total_expenses = rent + food + transport

    remaining_balance = income - total_expenses

    rent_percentage = (rent/income) * 100
    food_percentage = (food/ income) * 100
    transport_percentage = (transport/income) * 100

    if remaining_balance < 0:
        savings_rate = 0
    else:
        savings_rate = (remaining_balance/income) * 100 

    budget = {
        "income" : income,
        "total expenses" : total_expenses,
        "remaining balance" : remaining_balance,
        "rent percent" : rent_percentage,
        "food percent" : food_percentage,
        "transport percent" : transport_percentage,
        "savings rate" : savings_rate
    }

    return budget

def display_results(budget):
    print("============= BUDGET SUMMARY =============")
    print()
    print("--------Monthly Income--------")
    print(f"Income: ${budget['income']:.2f}")
    print()
    print("--------Monthly Expenses--------")
    print(f"Rent: ${(budget['rent percent'] * budget['income']) / 100 :.2f}")
    print(f"Rent - Percent of Income: {budget['rent percent'] :.2f}%")
    print(f"Food: ${(budget['food percent'] * budget['income']) / 100:.2f}")
    print(f"Food - Percent of Income: {budget['food percent']:.2f}%")
    print(f"Transport: ${(budget['transport percent']* budget['income']) / 100 :.2f}")
    print(f"Transport - Percent of Income: {budget['transport percent']:.2f}%")
    print("--------------------------------")
    print(f"Total Monthly Expenses: ${budget['total expenses']:.2f}")
    print("--------------------------------")
    print(f"Remaining Balance: ${budget['remaining balance']:.2f}")
    print(f"Savings Rate: {budget['savings rate']:.2f}%")

    print("------------WARNINGS------------")

    if budget['rent percent'] > 30:
        print('WARNING: Ideally rent should not cost more than 30% of your income') #This is an outdated rule that hardly applies in this day and age
    
    if budget['savings rate'] < 10:
        print('WARNING: Your savings are less than 10% of your total income, with proper budgeting this can be improved!')
    elif budget['savings rate'] <= 20:
        print('Your savings are in a decent position, however, there is still a bit more room for improvement')
    else:
        print('Your savings are in an good position, keep up the good work!')
    
    if budget['remaining balance'] < 0:
        print("WARNING: Your monthly expenses exceeds your monthly income and has entered the red zone! Please decrease your spending!")
    else:
        print("Your monthly expenses are in the green zone!")


    

main()