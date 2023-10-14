
from user import BankAccount  


class Admin:
    def __init__(self):
        self.user_accounts = []

# create ans account
    def create_account(self, name, email, address, account_type):
        user = BankAccount(name, email, address, account_type)
        self.user_accounts.append(user)
        return user

# delete accounts
    def delete_account(self, account_number):
        for user in self.user_accounts:
            if user.account_number == account_number:
                self.user_accounts.remove(user)
                return f"Account #{account_number} deleted successfully."
        return "Account not found."


# 
    def list_accounts(self):
        return [f"Account #{user.account_number} - {user.name}" for user in self.user_accounts]

# balance
    def total_balance(self):
        return sum(user.balance for user in self.user_accounts)

    def total_loan_amount(self):
        return sum(user.loan_taken for user in self.user_accounts)

# choose for the loan
    def toggle_loan_feature(self, status):
        BankAccount.loan_enabled = status

    def admin_operations(self, admin):
        print("\nAdmin Operations")
        print("1. Delete Account")
        print("2. List Accounts")
        print("3. Total Balance")
        print("4. Total Loan Amount")
        print("5. Toggle Loan Feature")
        print("6. Create User Account")
        print("7. Deposit Money")
        print("8. Withdraw Money")
        print("9. Check Balance")
        print("10. Transaction History")
        print("11. Take Loan")
        print("12. Transfer Money")
        print("13. Exit")

        choice = input("Select an option by number: (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

        if choice == "1":
            account_number = int(input("Enter the account number to delete: "))
            print(admin.delete_account(account_number))

        elif choice == "2":
            accounts = admin.list_accounts()
            if accounts:
                print("List of Accounts:")
                for account in accounts:
                    print(account)
            else:
                print("No accounts found.")

        elif choice == "3":
            print(f"Total balance: ${admin.total_balance()}")

        elif choice == "4":
            print(f"Total loan amount: ${admin.total_loan_amount()}")

        elif choice == "5":
            status = input("Enable (1) or Disable (0) the loan feature: ")
            admin.toggle_loan_feature(status == "1")

        elif choice == "6":
            admin.create_user_account()

        elif choice == "7":
            admin.deposit_money()
        elif choice == "8":
            admin.withdraw_money()
        elif choice == "9":
            admin.check_balance()
        elif choice == "10":
            admin.check_transaction_history()
        elif choice == "11":
            admin.take_loan()
        elif choice == "12":
            admin.transfer_money()
        elif choice == "13":
            return
        else:
            print("Sir you provide an invalid option please try again ......")
