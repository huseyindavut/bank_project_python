def show_balance(balance):
    print("********************")
    print(f"Your balance is ${balance:.2f}")
    print("********************")
    
def deposit():
    amount = float (input("Enter an amount to be deposited: "))
    
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount    
 
def withdraw(balance):
    print("********************")
    amount = float(input("Enter amount to be withdrawn: "))
    
    if amount > balance:
        print("Insufficent funds")
        return 0
    elif amount < 0:
        print("Amount must be greter than 0")
        return 0
    else:
        return amount
    print("********************")
    

def main():
    balance = 0
    is_running = True

    while is_running:
        print("********************")
        print("  Banking program   ") 
        print("********************") 
        print("1.Show the balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("********************")
        choice = input("Enter your choice (1-4): ")
    
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':  
            balane -= withdraw(balance)  
        elif  choice == '4':
            is_running = False
        else:
            print("********************")
            print("That is not a valid choice")
            print("********************")
        
    print("Thank you! Bye")        
        

if __name__== '__main__':
    main()
