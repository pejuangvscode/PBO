from sugeng_rahayu import *

def preload_data():
    Role.addRole("1", "User", "Regular user with basic privileges")
    Role.addRole("2", "SuperAdmin", "Administrator with full access")
    User.register("SA001", "AdminSugeng", "sugeng@gmail.com", "sugeng123", "SuperAdmin")
    Bus.addBus("A001", "Sugeng Rahayu Express", "Premium", 700000)
    Bus.addBus("A002", "Sugeng Rahayu Premium", "Premium", 600000)
    Bus.addBus("B003", "Sugeng Rahayu Economy", "Economy", 200000)
    Bus.addBus("B004", "Sugeng Rahayu Economy", "Economy", 300000)

def main_menu():
    print("\n=== Sugeng Rahayu Booking App ===")
    print("1. Login")
    print("2. Register")
    print("3. Exit")


def superadmin_menu():
    print("\n--- SuperAdmin Menu ---")
    print("1. Add Bus")
    print("2. Display Buses")
    print("3. Add Operator")
    print("4. Display Operators")
    print("5. Logout")


def user_menu():
    print("\n--- User Menu ---")
    print("1. View Buses")
    print("2. Book Ticket")
    print("3. View My Bookings")
    print("4. Logout")

def run_application():
    preload_data()
    current_user = None

    while True:
        if not current_user:
            main_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                email = input("Enter Email: ")
                password = input("Enter Password: ")
                current_user = User.login(email, password)
            elif choice == "2":
                user_id = f"U{len(User.users) + 1:03}"
                name = input("Enter Name: ")
                email = input("Enter Email: ")
                password = input("Enter Password: ")
                User.register(user_id, name, email, password)
            elif choice == "3":
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        else:
            if current_user.user_role == "SuperAdmin":
                superadmin_menu()
                choice = input("Choose an option: ")

                if choice == "1":
                    SuperAdmin.addBus()
                elif choice == "2":
                    print("\n--- Bus List ---")
                    SuperAdmin.displayBuses()
                elif choice == "3":
                    SuperAdmin.addOperator()
                elif choice == "4":
                    print("\n--- Operator List ---")
                    SuperAdmin.displayOperator()
                elif choice == "5":
                    print("Logging out...")
                    current_user = None
                else:
                    print("Invalid option. Please try again.")

            elif current_user.user_role == "User":
                user_menu()
                choice = input("Choose an option: ")

                if choice == "1":
                    print("\n--- Bus List ---")
                    Customer.displayBuses()
                elif choice == "2":
                    Customer.bookTickets(current_user)
                elif choice == "3":
                    print("\n--- My Bookings ---")
                    Customer.displayBookings(current_user)
                elif choice == "4":
                    print("Logging out...")
                    current_user = None
                else:
                    print("Invalid option. Please try again.")

if __name__ == "__main__":
    run_application()
