class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return ("Deposited $"+str(amount)+". New balance is $" + str(self.balance)+".")

    #define the other two methods here


#create an object here. The object should be an instance of the class


user_account_number = input("What is your account number?")
if user_account_number == 0:
    print("Account verified!")
        
        
    while True:
        print("\nWhat would you like to do?")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
            
        user_choice = input("Enter the number of your choice: ")
            
        if user_choice == '1':
            pass #delete this pass line
            #call function here
            #be sure to specify the self (i.e., the object/instance name... this would be variable name)
           
        

else:
        print("Incorrect account number. Please try again.")