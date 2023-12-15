class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin):
        if self.pin == pin:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Недостатъчен баланс")
        else:
            print("Грешен пин")

    def get_account_info(self):
        print(f"Account Number: {self.account_number} Balance: {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, pin, interest_rate):
        super().__init__(account_number, balance, pin)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def calculate_balance_with_interest(self):
        return self.calculate_interest() + self.balance

    def get_savings_account_info(self):
        print(f"Account Number: {self.account_number} Balance: {self.balance}")

# ... (your existing class definitions)

account_number = input("Account Number: ")
balance = float(input("Balance: "))
pin = input("PIN: ")

while True:
    account_type = input("Choose account type (Savings or Current): ").lower()
    if account_type == "savings":
        interest_rate = float(input("Interest Rate: "))
        account = SavingsAccount(account_number, balance, pin, interest_rate)
        break
    elif account_type == "current":
        account = Account(account_number, balance, pin)
        break
    else:
        print("Invalid account type.")

while True:
    operation_choice = input("Choose 1, 2, or 3 for an operation: ==================\n"
                             "       МЕНЮ\n"
                             "==================\n"
                             "1. Депозит\n"
                             "2. Теглене\n"
                             "3. Инфо за сметката\n"
                             "================== ")
    if operation_choice not in ["1", "2", "3"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    if operation_choice == "1":
        amount = float(input("Enter amount to be deposited: "))
        account.deposit(amount)
        print(f"New balance {account.balance}")

    elif operation_choice == "2":
        if account.balance >= 0:
            pin_code = input("Enter PIN code: ")
            amount = float(input("Enter amount to be withdrawn: "))
            if pin_code == account.pin:
                account.withdraw(amount, pin_code)
                print(f"New balance {account.balance}")
            else:
                print("Invalid Pin")
        else:
            print("Negative Balance")

    elif operation_choice == "3":
        account.get_account_info()

    another_operation = input("Do you like to continue with another operation: YES/NO").lower()
    if another_operation != "yes":
        break