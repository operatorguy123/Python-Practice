class BankAccount:
    def __init__(self, AccountHolder, Balance=0):
        self.AccountHolder = AccountHolder
        self.Balance = Balance
        
    def deposit(self,Amount):
        if Amount > 0:
            self.Balance += Amount
            print(f"Successfully deposited {Amount}.")
        else:
            print("Invalid Entry!")
            
    def withdraw(self,Amount):
        if 0 < Amount <= self.Balance:
            print(f"Successfully withdrawn {Amount}.")
            self.Balance -= Amount
        else:
            print("Invalid Entry!")
            
    def display_balance(self):
        print(f"Your current balance is {self.Balance}")
        
arun = BankAccount("Arun")
arun.deposit(5000)
arun.display_balance()
arun.withdraw(2500)
arun.display_balance()
arun.withdraw(3000)
