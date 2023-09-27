def convert_from_euros_to_dollars(euros):
    return euros * 1.08

def convert_from_dollars_to_euros(dollars):
    return dollars * 0.93

def convert_from_gbp_to_euros(gbp):
    return gbp * 1.17

def convert_from_euros_to_gbp(euros):
    return euros / 1.17

def convert_from_jpy_to_euros(jpy):
    return jpy / 130.0

def convert_from_euros_to_jpy(euros):
    return euros * 130.0

def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative. Please enter a valid amount.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

def main():
    print("Welcome to the currency converter program!")
    print("Options:")
    print("1. Convert from euros to dollars")
    print("2. Convert from dollars to euros")
    print("3. Convert from GBP to euros")
    print("4. Convert from euros to GBP")
    print("5. Convert from JPY to euros")
    print("6. Convert from euros to JPY")

    option = input("Enter your choice (1-6): ")

    if option == "1":
        euro_amount = get_valid_amount("Enter amount in euros: ")
        dollars = convert_from_euros_to_dollars(euro_amount)
        print(f"{euro_amount:.2f} euros is equal to {dollars:.2f} dollars.")
    elif option == "2":
        dollar_amount = get_valid_amount("Enter amount in dollars: ")
        euros = convert_from_dollars_to_euros(dollar_amount)
        print(f"{dollar_amount:.2f} dollars is equal to {euros:.2f} euros.")
    elif option == "3":
        gbp_amount = get_valid_amount("Enter amount in GBP: ")
        euros = convert_from_gbp_to_euros(gbp_amount)
        print(f"{gbp_amount:.2f} GBP is equal to {euros:.2f} euros.")
    elif option == "4":
        euro_amount = get_valid_amount("Enter amount in euros: ")
        gbp = convert_from_euros_to_gbp(euro_amount)
        print(f"{euro_amount:.2f} euros is equal to {gbp:.2f} GBP.")
    elif option == "5":
        jpy_amount = get_valid_amount("Enter amount in JPY: ")
        euros = convert_from_jpy_to_euros(jpy_amount)
        print(f"{jpy_amount:.2f} JPY is equal to {euros:.2f} euros.")
    elif option == "6":
        euro_amount = get_valid_amount("Enter amount in euros: ")
        jpy = convert_from_euros_to_jpy(euro_amount)
        print(f"{euro_amount:.2f} euros is equal to {jpy:.2f} JPY.")
    else:
        print("Invalid option. Please choose a number between 1 and 6.")

    print("Program ended successfully.")

if __name__ == "__main__":
    main()
