class Account:
    account_type = "Bank Account"

    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. New balance is {self.balance}")
        else:
            print("Withdrawal failed. Insufficient balance.")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance is {self.balance}") 
        
    def transfer(self, recipient_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred {amount} to {recipient_account.account_holder_name}. New balance is {self.balance}")
        else:
            print(f"Cannot transfer {amount}. Insufficient balance.")
            
            
my_account = Account("12345", "Sparks Njoroge", 10000)
my_account.withdrawal(500)
my_account.deposit(5000)

recipient_account = Account("987654321", "Jane Smith", 10000)


my_account.transfer(recipient_account, 1000)
            
       
        
           