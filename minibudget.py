def main():
    print("Hello! Please input your current income")
    user_income = float(input('>'))
    print("Please enter your rent, food, and transport expenses!")
    user_rent = float(input('Rent: '))
    user_food = float(input('Food: '))
    user_transport = float(input('Transport: '))

    user_balance = user_income - (user_rent + user_food + user_transport) 

    print(f"User balance after expenses: ${user_balance:.2f}")

    if user_balance < 0:
        print("You are in the red!")
    else:
        print("You are in the green!")

main()