class Occupant:
    def __init__(self, name, phone_number, cell_phone_number, rooms, people, in_date, Days, Rooms):
        self.guest_name=name
        self.user_phone = phone_number
        self.ID = cell_phone_number
        self.amount_of_rooms = rooms
        self.party_size = people
        self.check_in = in_date
        self.trip_length= Days
        self.room_type = Rooms

    def price(self):
        self.Base_cost = 100
        self.large_bed = 125
        self.small_bed = 60
        self.tax = 15
        if self.room_type == "Double Bed":
                self.price = (self.Base_cost + self.large_bed) * self.trip_length
        elif self.room_type == "Single Bed":
                self.price = (self.Base_cost + self.small_bed) * self.trip_length
        return self.price

    def get_tax(self):
        return self.tax
# display the booking details of standard customer
    def display(self):
        print("Custome Name: %s" % (self.guest_name))
        print("Check In date: %s"%(self.check_in))
        print("Number of Days: %d" % (self.trip_length))
        print("Price: %d" % self.price)

class Room_type:
    def __init_(self, number_of_people, number_of_rooms):
        self.number_of_people = number_of_people
        self.number_of_rooms = number_of_rooms
        self.twin_bed = 1000
        self.tax = 14
        self.price = (self.twin_bed + ((self.twin_bed * self.tax) * 100))
    def get_bed_price(self):
        self.price = self.price * self.number_of_rooms
        if self.number_of_people > 2:
            self.price = self.price + self.number_of_people * 50
        print("ordinary room", self.price)
    def set_tax(self):
        self.tax = 14
    def get_no_of_people(self):
        return self.number_of_people
    def get_no_of_rooms(self):
        return self.number_of_rooms
    def get_tax(self):
        return self.tax
    def set_twin_bed_size(self):
        self.twin_bed = 1000
    def get_twin_bed_size(self):
        return self.twin_bed
# Inheriting the Occupant class
class Penthouse(Occupant):
    def __init__(self, name, phone_number, cell_phone_number, rooms, people, in_date, Days, Rooms):
        super().__init__(name, phone_number, cell_phone_number, rooms, people, in_date, Days, Rooms)
        self.price = (Occupant.price(self) + 100)*self.amount_of_rooms
        self.price = self.price * self.amount_of_rooms
        self.total_price = self.price+(self.price*15)/100
    def get_bed_price(self):
        print("Deluxe room price: ", self.total_price)
    def display(self):
        print("Custome Name: %s" % (self.guest_name))
        print("Check In date: %s"%(self.check_in))
        print("Number of Days: %d" % (self.trip_length))
        print("Price: %d"%(self.total_price))

class upgraded_room(Room_type):
    def __init_(self, no_of_people, number_of_rooms):

        super().__init_(no_of_people, number_of_rooms)
        self.no_of_people = no_of_people
        self.no_of_rooms = number_of_rooms
        self.price = (Room_type.get_twin_bed_size(self) + 300) + (
                (Room_type.get_twin_bed_size(self) + 300) / Room_type.get_tax(self)) * 100
        self.price = self.price * self.no_of_rooms
        if self.no_of_people > 2:
            self.price = self.price + self.no_of_people * 50
    def get_bed_price(self):
        print("Luxury room price", self.price)
# inheriting the classes DeluxRoom LuxuryRoom & Ouccupant
class BookingInformation(upgraded_room, Penthouse, Occupant):
    def __init_(self, number_of_people, number_of_rooms):
        self.no_of_people = number_of_people
        self.no_of_rooms = number_of_rooms
        super().__init__(number_of_people, number_of_rooms)
        Penthouse.get_bed_price(self)
        upgraded_room.get_bed_price(self)
        Room_type.get_bed_price(self)
    pass

while True:
    choice= int(input(" 1. Book Standard Room\n 2. Book Delux Room\n 3. Display Booking\n 4. To End\n Enter The choice: "))
    if (choice == 1):
        guestName= input("Enter the name of customer: ")
        guestPhone = input("Enter the phone number of customer: ")
        guestID = input("Enter the id of customer: ")
        Rooms = int(input("Enter the number of rooms : "))
        Group_size= int(input("Enter the number of people: "))
        Day_in=input("Enter check in date: ")
        length_of_trip=int(input("Number of days: "))
        type_of_room = input("Enter the room type: ")
        Guest = Occupant(guestName, guestPhone, guestID, Rooms, Group_size, Day_in, length_of_trip, type_of_room)
        print(Guest.price())
    if (choice == 2):
        guestName = input("Enter the name of customer: ")
        guestPhone = input("Enter the phone number of customer: ")
        guestID = input("Enter the id of customer: ")
        Rooms = int(input("Enter the number of rooms : "))
        Group_size = int(input("Enter the number of people: "))
        Day_in = input("Enter check in date: ")
        length_of_trip = int(input("Number of days: "))
        type_of_room = input("Enter the room type: ")
        Guest = Penthouse(guestName, guestPhone, guestID, Rooms, Group_size, Day_in, length_of_trip, type_of_room)
        Guest.get_bed_price()
    if (choice == 3):
        Guest.display()
    if (choice == 4):
        break