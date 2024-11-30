class Role:
    roles = []

    def __init__(self, role_id, role_title, role_description):
        self.role_id = role_id
        self.role_title = role_title
        self.role_description = role_description

    @classmethod
    def addRole(cls, role_id, role_title, role_description):
        new_role = Role(role_id, role_title, role_description)
        cls.roles.append(new_role)
        print(f"Role '{role_title}' added successfully.")

    @classmethod
    def displayRoles(cls):
        if not cls.roles:
            print("No roles available.")
            return
        for role in cls.roles:
            print(f"ID: {role.role_id}, Title: {role.role_title}, Description: {role.role_description}")

class User:
    users = []

    def __init__(self, user_id, user_name, user_email, user_password, user_role):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.user_role = user_role

    @classmethod
    def register(cls, user_id, user_name, user_email, user_password, user_role="User"):
        new_user = User(user_id, user_name, user_email, user_password, user_role)
        cls.users.append(new_user)
        print(f"User '{user_name}' registered successfully with role '{user_role}'.")

    @classmethod
    def login(cls, user_email, user_password):
        for user in cls.users:
            if user.user_email == user_email and user.user_password == user_password:
                print(f"Welcome, {user.user_name} ({user.user_role})!")
                return user
        print("Invalid credentials.")
        return None

class Operator:
    operators = []

    def __init__(self, operator_id, operator_name, operator_address, operator_mobile):
        self.operator_id = operator_id
        self.operator_name = operator_name
        self.operator_address = operator_address
        self.operator_mobile = operator_mobile

    @classmethod
    def addOperator(cls, operator_id, operator_name, operator_address, operator_mobile):
        new_operator = Operator(operator_id, operator_name, operator_address, operator_mobile)
        cls.operators.append(new_operator)
        print(f"Operator '{operator_name}' added successfully.")

    @classmethod
    def displayOperators(cls):
        if not cls.operators:
            print("No operators available.")
            return
        for operator in cls.operators:
            print(
                f"ID: {operator.operator_id}, Name: {operator.operator_name}, Address: {operator.operator_address}, Mobile: {operator.operator_mobile}"
            )

class Bus:
    buses = []

    def __init__(self, bus_id, bus_name, bus_type, bus_ticket_price):
        self.bus_id = bus_id
        self.bus_name = bus_name
        self.bus_type = bus_type
        self.bus_ticket_price = bus_ticket_price

    @classmethod
    def addBus(cls, bus_id, bus_name, bus_type, bus_ticket_price):
        new_bus = Bus(bus_id, bus_name, bus_type, bus_ticket_price)
        cls.buses.append(new_bus)
        print(f"Bus '{bus_name}' added successfully.")

    @classmethod
    def displayBuses(cls):
        if not cls.buses:
            print("No buses available.")
            return
        for bus in cls.buses:
            print(f"ID: {bus.bus_id}, Name: {bus.bus_name}, Type: {bus.bus_type}, Price: {bus.bus_ticket_price}")

class PremiumBus(Bus):
    def __init__(self, bus_id, bus_name, bus_ticket_price, wifi_available, meal_service):
        super().__init__(bus_id, bus_name, "Premium", bus_ticket_price)
        self.wifi_available = wifi_available
        self.meal_service = meal_service

    def displayFeatures(self):
        print(
            f"Premium Features - WiFi: {'Yes' if self.wifi_available else 'No'}, Meal Service: {'Yes' if self.meal_service else 'No'}"
        )

class EconomyBus(Bus):
    def __init__(self, bus_id, bus_name, bus_ticket_price, stop_count):
        super().__init__(bus_id, bus_name, "Economy", bus_ticket_price)
        self.stop_count = stop_count

    def calculateTravelTime(self):
        return f"Estimated travel time is {self.stop_count * 20} minutes."

class Booking:
    bookings = []

    def __init__(self, booking_id, user_name, bus_name, booking_date):
        self.booking_id = booking_id
        self.user_name = user_name
        self.bus_name = bus_name
        self.booking_date = booking_date

    @classmethod
    def addBooking(cls, booking_id, user_name, bus_name, booking_date):
        new_booking = Booking(booking_id, user_name, bus_name, booking_date)
        cls.bookings.append(new_booking)
        print(f"Booking ID '{booking_id}' for bus '{bus_name}' created successfully.")

    @classmethod
    def displayBookings(cls, user_name=None):
        if not cls.bookings:
            print("No bookings available.")
            return
        for booking in cls.bookings:
            if user_name is None or booking.user_name == user_name:
                print(
                    f"Booking ID: {booking.booking_id}, User: {booking.user_name}, Bus: {booking.bus_name}, Date: {booking.booking_date}"
                )

class GroupBooking(Booking):
    def __init__(self, booking_id, user_name, bus_name, booking_date, group_size, discount):
        super().__init__(booking_id, user_name, bus_name, booking_date)
        self.group_size = group_size
        self.discount = discount

    def applyGroupDiscount(self):
        print(f"Group discount applied: {self.discount * 100}%")

class SingleBooking(Booking):
    def __init__(self, booking_id, user_name, bus_name, booking_date, group_size, discount):
        super().__init__(booking_id, user_name, bus_name, booking_date)
        
    def applyGroupDiscount(self):
        print(f"Group discount applied: {self.discount * 100}%")

class Agent(User):
    def __init__(self, user_id, user_name, user_email, user_password):
        super().__init__(user_id, user_name, user_email, user_password, "Agent")
        self.assigned_tickets = []

    def bookTickets(self, bus, customer_name):
        print(f"Agent {self.user_name} booked a ticket for {customer_name} on bus {bus.bus_name}.")

class Customer(User):
    def __init__(self, user_id, user_name, user_email, user_password):
        super().__init__(user_id, user_name, user_email, user_password, "Customer")

    def displayBuses():
        Bus.displayBuses()

    def bookTickets(user):
        if not Bus.buses:
            print("No buses available!")
            return

        print("\nAvailable Buses:")
        Bus.displayBuses()
        bus_id = input("Enter the Bus ID to book: ")
        selected_bus = next((bus for bus in Bus.buses if bus.bus_id == bus_id), None)

        if not selected_bus:
            print("Bus not found!")
            return

        booking_id = f"BKG{len(Booking.bookings) + 1}"
        booking_date = input("Enter Booking Date (YYYY-MM-DD): ")
        Booking.addBooking(booking_id, user.user_name, selected_bus.bus_name, booking_date)
    
    def displayBookings(user):
        Booking.displayBookings(user.user_name)

class Admin(User):
    def __init__(self, user_id, user_name, user_email, user_password):
        super().__init__(user_id, user_name, user_email, user_password, "Admin")

    def addBus():
        bus_id = input("Enter Bus ID: ")
        bus_name = input("Enter Bus Name: ")
        bus_type = input("Enter Bus Type (Premium/Economy): ")
        bus_ticket_price = float(input("Enter Ticket Price: "))

        if bus_type.lower() == "premium":
            wifi_available = input("Is WiFi available? (yes/no): ").lower() == "yes"
            meal_service = input("Is meal service available? (yes/no): ").lower() == "yes"
            new_bus = PremiumBus(bus_id, bus_name, bus_ticket_price, wifi_available, meal_service)
            Bus.buses.append(new_bus)
        elif bus_type.lower() == "economy":
            stop_count = int(input("Enter number of stops: "))
            new_bus = EconomyBus(bus_id, bus_name, bus_ticket_price, stop_count)
            Bus.buses.append(new_bus)
        else:
            print("Invalid bus type!")
            return

        print(f"Bus '{bus_name}' added successfully!")

    def displayBuses():
        Bus.displayBuses()

    def addOperator():
        operator_id = f"O{len(Operator.operators) + 1:03}"
        name = input("Enter Operator Name: ")
        address = input("Enter Operator Address: ")
        mobile = input("Enter Operator Mobile: ")
        Operator.addOperator(operator_id, name, address, mobile)

    def displayOperator():
        Operator.displayOperators()




