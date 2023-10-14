import random

class BankAccount:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(1000, 9999)
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0



# deposit balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"${amount} deposited successfully."
        else:
            return "Invalid deposit amount."


# withdraw balance with exceed option
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")

            return f"${amount} withdrawn successfully......"
        else:
            return "Withdrawal amount exceeded...."


# balance check
    def check_balance(self):
        return f"Available balance is : ${self.balance}"

# history 
    def check_transaction_history(self):
        return self.transaction_history


#  loan functionality
    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.loan_taken += 1
            self.balance += amount
            self.transaction_history.append(f"Loan taken: ${amount}")

            return f"${amount} loan taken successfully."
        else:
            return "You have already taken the maximum number of loans."


# transfer to another account
    def transfer(self, recipient, amount):
        if recipient.account_number == self.account_number:
            return "Cannot transfer to the same account."
        
        if amount <= self.balance:
            recipient.balance += amount
            self.balance -= amount
            self.transaction_history.append(f"Transferred ${amount} to Account #{recipient.account_number}")
            recipient.transaction_history.append(f"Received ${amount} from Account #{self.account_number}")
            return f"${amount} transferred to Account #{recipient.account_number} successfully."
        else:
            return "Insufficient funds for transfer"



# User class
class User:
    def __init__(self):
        pass

    def user_operations(self, admin):
        print("\nUser Operations")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Take Loan")
        print("7. Transfer Money")
        print("8. Exit")
        choice = input("Select an option (1/2/3/4/5/6/7/8): ")


        if choice == "1":
            self.create_account(admin)
        elif choice == "2":
            self.deposit_money(admin)
        elif choice == "3":
            self.withdraw_money(admin)
        elif choice == "4":
            self.check_balance(admin)
        elif choice == "5":
            self.check_transaction_history(admin)
        elif choice == "6":
            self.take_loan(admin)
        elif choice == "7":
            self.transfer_money(admin)
        elif choice == "8":
            return
        else:
            print("Invalid choice. Please select a valid option.")

# create an account 
    def create_account(self, admin):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        account_type = input("Enter your account type (Savings/Current): ")

        user = admin.create_account(name, email, address, account_type)
        print(f"Account created successfully. Account number: {user.account_number}")

# deposit money 
    def deposit_money(self, admin):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the amount to deposit: "))
        user = self.find_user_by_account_number(admin, account_number)

        if user:
            print(user.deposit(amount))
        else:
            print("Account not found.")

    def withdraw_money(self, admin):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the amount to withdraw: "))
        user = self.find_user_by_account_number(admin, account_number)

        if user:
            print(user.withdraw(amount))
        else:
            print("Account not found...")

# balance check 
    def check_balance(self, admin):
        account_number = int(input("Enter your account number: "))
        user = self.find_user_by_account_number(admin, account_number)

        if user:
            print(user.check_balance())
        else:
            print("Account not found........")

# transaction history
    def check_transaction_history(self, admin):
        account_number = int(input("Enter your account number: "))
        user = self.find_user_by_account_number(admin, account_number)

        if user:
            print("Transaction History:")
            for transaction in user.check_transaction_history():
                print(transaction)
        else:
            print("Account not found............")


# loan option
    def take_loan(self, admin):
        account_number = int(input("Enter your account number: "))
        user = self.find_user_by_account_number(admin, account_number)

        if user:
            if user.loan_taken < 2:
                amount = float(input("Enter the loan amount: "))
                print(user.take_loan(amount))
            else:
                print("You have already taken the maximum number of loans.")
        else:
            print("Account not found.....")

# money transfer
    def transfer_money(self, admin):
        account_number_sender = int(input("Enter your account number (sender): "))
        account_number_recipient = int(input("Enter the recipient's account number: "))
        amount = float(input("Enter the amount to transfer: "))
        user_sender = self.find_user_by_account_number(admin, account_number_sender)
        user_recipient = self.find_user_by_account_number(admin, account_number_recipient)

        if user_sender and user_recipient:
            print(user_sender.transfer(user_recipient, amount))
        else:
            print("Account not found.")



# match the user wiht number
    def find_user_by_account_number(self, admin, account_number):
        for user in admin.user_accounts:
            if user.account_number == account_number:
                return user
        return None
