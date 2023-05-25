class Account:
    def __init__(self):
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
    
    def check_balance(self):
        total_deposits = sum(transaction['amount'] for transaction in self.deposits)
        total_withdrawals = sum(transaction['amount'] for transaction in self.withdrawals)
        return total_deposits - total_withdrawals
    
    def deposit(self, amount):
        transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction)
    
    def withdrawal(self, amount):
        transaction = {
            "amount": amount,
            "narration": "withdrawal"
        }
        self.withdrawals.append(transaction)
    
    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(f"{transaction['narration']} - {transaction['amount']}")
    
    def borrow_loan(self, amount):
        total_deposits = sum(transaction['amount'] for transaction in self.deposits)
        if self.loan_balance == 0 and amount > 100 and len(self.deposits) >= 10 and amount <= total_deposits / 3:
            self.loan_balance += amount
            print("Loan approved!")
        else:
            print("Loan request denied.")
    
    def repay_loan(self, amount):
        if amount > self.loan_balance:
            overpayment = amount - self.loan_balance
            self.loan_balance = 0
            self.deposit(overpayment)
        else:
            self.loan_balance -= amount
    
    def transfer(self, amount, destination_account):
        if amount <= self.check_balance():
            self.withdrawal(amount)
            destination_account.deposit(amount)
            print("Transfer successful!")
        else:
            print("Insufficient balance for transfer.")


# instances
account1 = Account()

account1.deposit(1000)
account1.deposit(2000)

account1.withdrawal(500)

balance = account1.check_balance()
print("Account Balance:", balance)

print("Account Statement:")
account1.print_statement()

account1.borrow_loan(500)

account1.repay_loan(200)

account2 = Account()

account1.transfer(300, account2)


print("Account 1 Statement:")
account1.print_statement()
print("Account 2 Statement:")
account2.print_statement()
