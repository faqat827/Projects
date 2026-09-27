import datetime



class fundsError(Exception):
    pass


class AddZeroError(Exception):
    pass



    
def load_balance():
    try:
        with open("balance.txt", "r") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return 1000


def save_balance(balance):
    with open("balance.txt", "w") as file:
        file.write(str(balance))


def bank():
    balance = load_balance()

    while True:
        print("\nOur Menu")
        print(f"Current balance: {balance}")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        print("4. View Transaction History")

        try:
            choice = int(input("Select 1-4: "))
        except ValueError:
            print("Please choose a valid number")
            continue

        if choice == 1:
            try:
                amount = int(input("Enter your amount: "))

                if amount <= 0:
                    raise AddZeroError(
                        "You cannot add zero or negative amount"
                    )

                balance += amount
                save_balance(balance)  # File mein naya balance update kar diya
                transaction_type = "Deposit"

                print(
                    f"Your amount added successfully. "
                    f"Now your balance is: {balance}"
                )

                # History save karein (file.write mein single string use karein)
                with open("transaction.txt", "a") as file:
                    file.write(
                        f"Transaction: {transaction_type}, "
                        f"Amount: {amount}, "
                        f"Date: {datetime.date.today()}, "
                        f"Balance: {balance}\n"
                    )

            except ValueError:
                print("Please write a valid amount")
            except AddZeroError as e:
                print(f"Error: {e}")

        elif choice == 2:
            try:
                amount = int(input("Enter your amount: "))

                if amount <= 0:
                    raise AddZeroError(
                        "You cannot withdraw zero or negative amount"
                    )

                if amount > balance:
                    raise fundsError(
                        f"You cannot withdraw this amount. "
                        f"Your balance is {balance}"
                    )

                balance -= amount
                save_balance(balance)  # File mein naya balance update kar diya
                transaction_type = "Withdraw"

                print(
                    f"You withdrew successfully. "
                    f"Now your balance is: {balance}"
                )

                # History save karein
                with open("transaction.txt", "a") as file:
                    file.write(
                        f"Transaction: {transaction_type}, "
                        f"Amount: {amount}, "
                        f"Date: {datetime.date.today()}, "
                        f"Balance: {balance}\n"
                    )

            except ValueError:
                print("Please put a valid amount")
            except AddZeroError as e:
                print(f"Error: {e}")
            except fundsError as e:
                print(f"Error: {e}")

        elif choice == 3:
            print("Thanks for visiting our bank. Have a nice day!")
            break

        elif choice == 4:
            try:
                with open("transaction.txt", "r") as file:
                    print("\nTransaction History:")
                    print(file.read())
            except FileNotFoundError:
                print("No transaction history found.")

        else:
            print("Please select a valid number 1-4")


bank()