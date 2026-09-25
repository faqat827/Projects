class fundsError(Exception):
        pass
class AddZeroError(Exception):
    pass

def bank():
    balance = 1000
    while True:
        print("Our Menu")
        print(f"Current balance : {balance}")
        print("1 Deposit")
        print("2 withdraw")
        print("3 Exist")
        
        try:
            choice = int(input("Select 1-3"))
        except ValueError:
            print("Please chose the valid number")
        
            continue
    
        if choice == 1:
            try:
                amount = int(input("Enter your amount"))
                if amount <=0:
                    raise AddZeroError("You canot add zero")
                balance += amount
                print(f"Your amount add sucessfull. Now your balance is : {balance}")
            
            except ValueError:
                print("Please write the valid amount") 
            except AddZeroError as e:
                print(f"Error: {e}")

        elif choice == 2:
            try:
                amount = int(input("Enter your amount"))
                if amount <=0:
                    raise AddZeroError("You canot withdraw 0")
                if amount > balance:
                    raise fundsError(f"You cannot with draw this amount. Your balance is {balance}")
            
                balance -= amount
                print(f"You withdraw sucessfull. Now your balance is {balance}")
            except ValueError:
                            print("Please put the valid amount")
            except AddZeroError as e:
                print(f"Error: {e}")
            except fundsError as e:
                print(f"Error: {e}")
                
        elif choice == 3:
            print("Thanks for visit our bank")
            break
        
        else:
            print("Please selcet the valid number 1-3")

      
        
bank()            