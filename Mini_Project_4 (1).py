class Flight:
    def __init__(self, flight_number, destination, departure_time, available_seats):
        self.__flight_number = flight_number
        self.__destination = destination
        self.__departure_time = departure_time
        self.__available_seats = available_seats  
        self.__passenger = []
    
    @property
    def get_available_seats(self):
        return self.__available_seats
    
    @get_available_seats.setter
    def set_available_seats(self, amount):
        self.__available_seats += amount
        
    def adding_passenger(self, passenger_with_reserved_seat):
        self.__passenger.append(passenger_with_reserved_seat)
        
    def removing_passenger(self, name, age, passport_number):
        for passenger in self.__passenger:
            if passenger.check(name, age, passport_number):
                self.__passenger.remove(passenger)
                return 1
        
        return 0
            
    def flight_display(self):
        print(f"Flight Number: {self.__flight_number}")
        print(f"Destination: {self.__destination}")
        print(f"Departure Time: {self.__departure_time}")
        print(f"Reserved Seats: {len(self.__passenger)}")
        print(f"Available Seats: {self.__available_seats}")
        
    def passenger_display(self):
        for passenger in self.__passenger:
            passenger.display()
        
class Passenger:
    def __init__(self, name, age, passport_number):
        self.__name = name
        self.__age = age
        self.__passport_number = passport_number
        
    def check(self, name, age, passport_number):
        if self.__name == name and self.__age == age and self.__passport_number == passport_number:
            return True
        else:
            return False
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_passport_number(self):
        return self.__passport_number
    
    def display(self):
        print(f" - Passenger: {self.__name}, {self.__age} years old, Passport Number: {self.__passport_number} - ")

class Reservation(Passenger):
    def __init__(self, name, age, passport_number, flight_number):
        Passenger.__init__(self, name, age, passport_number)
        self.__flight_number = flight_number
        
    def get_flight_number(self):
        return self.__flight_number
    
    def display(self):
        print(f" - Passenger: {self.get_name()}, {self.get_age()} years old, Passport Number: {self.get_passport_number()}, In Flight: {self.__flight_number} - ")

class AirlineSystem():
    def __init__(self):
        self.flights = {}
    
    def adding_flight(self, flight_number, destination, departure_time, available_seats):
        flight = Flight(flight_number, destination, departure_time, available_seats)
        self.flights[flight_number] = flight
        print(f"Flight {flight_number} added successfully.")
        
    def book_a_seat(self, name, age, passport_number, flight_number):
        flight = self.flights.get(flight_number)
        
        if flight:
            if flight.get_available_seats >= 1:
                reserve = Reservation(name, age, passport_number, flight_number)
                flight.adding_passenger(reserve)
                flight.set_available_seats = -1
                print(f"Reservation confirmed for {reserve.get_name()} on flight {reserve.get_flight_number()}.")
            else:
                print(f"No available seats on flight {flight_number}")
        else:
            print(f"Flight {flight_number} not found.")        
        
    def cancel_reservation(self, name, age, passport_number, flight_number):
        flight = self.flights.get(flight_number)
        
        if flight:
            if flight.removing_passenger(name, age, passport_number) == 1:
                flight.set_available_seats = 1
                print(f"Successfully removed passenger {name} from flight {flight_number}")
            else:
                print("Passenger not found.")
        else:
            print(f"Flight {flight_number} not found.")
        
    def View_Flight_Details(self, flight_number):
        flight = self.flights.get(flight_number)
        
        if flight:
            flight.flight_display()
        else:
            print(f"Flight {flight_number} not found.")
        
    def View_Passenger_Details(self, flight_number):
        flight = self.flights.get(flight_number)
        
        if flight:
            flight.passenger_display()
        else:
            print(f"Flight {flight_number} not found.")
        
system = AirlineSystem()

print("--- Wellcome To Our Airline Reservation System ---")
while True:
    print()
    print()
    print("1. Add Flight")
    print("2. Book a Seat")
    print("3. Cancel Reservation")
    print("4. View Flight Details")
    print("5. View Passenger Details")
    print("6. Exit")
    print()
    choice = input("PLease enter your choice: ")
    print()
    if choice == "1":
        flight_number = input("Enter flight number: ")
        destination = input("Enter destination: ")
        departure_time = input("Enter departure time: ")
        available_seats = int(input("Enter total seats: "))
        print()
        system.adding_flight(flight_number, destination, departure_time, available_seats)
        
    elif choice == "2":
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        passport_number = input("Enter passenger passport number: ")
        flight_number = input("Enter flight number: ")
        print()
        system.book_a_seat(name, age, passport_number, flight_number)
        
    elif choice == "3":
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        passport_number = input("Enter passenger passport number: ")
        flight_number = input("Enter flight number: ")
        print()
        system.cancel_reservation(name, age, passport_number, flight_number)
        
    elif choice == "4":
        flight_number = input("Enter flight number: ")
        print()
        system.View_Flight_Details(flight_number)
    
    elif choice == "5":
        flight_number = input("Enter flight number: ")
        print()
        system.View_Passenger_Details(flight_number)
    
    elif choice == "6":
        print("Exiting the system. Goodbye and see you again!")
        break
    
    else:
        print("Invalid choice. Please try again.")