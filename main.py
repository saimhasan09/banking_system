from user import User
from admin import Admin

def main():
    admin = Admin()
    user = User()

    while True:
        print("\nWelcome to the #### MAMAR BANK ####")
        print("1. User Operations")
        print("2. Admin Operations")
        print("3. Exit")
        choice = input("Select an option by number: (1/2/3): ")

        if choice == "1":
            user.user_operations(admin)
        elif choice == "2":
            admin.admin_operations(admin)
        elif choice == "3":
            print("Exiting the MAMAR BANK .")
            break
        else:
            print("SORRY sir, please choose an valid option.")

if __name__ == "__main__":
    main()
