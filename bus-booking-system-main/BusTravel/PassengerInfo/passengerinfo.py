class PassengerRegistration():
    def __init__(self):
        self.passengerName = None
        self.noOfPassenger = None
        self.departureLocation = None
        self.destinationLocation = None
        self.ddmmyyyy = None
        self.seatNo = None
        self.selectBusType = None
        self.busFare = None
        self.autoInc = 1
        self.countcol = 0

    def getPassengerInfo(self):
        self.passengerName = input("Enter Passenger Name  :")
        self.noOfPassenger = int(input("Enter Number Of Passengers :"))
        print("1: Trichy\n2: Chennai\n3: Thanjavur\n4: Madurai")
        self.dl = int(input("Enter Departure Location :"))
        # Set departure location based on input (unchanged logic)

        print("1: Karur\n2: Ooty\n3: Erode\n4: Coimbatore")
        self.dpl = int(input("Enter Destination Location  :"))
        # Set destination location based on input (unchanged logic)

        self.ddmmyyyy = input("Enter Date of Journey Like 03-06-1990   :")

        # Booking Seat
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        # Available seats: using set for fast lookup
        available_seats = set(range(1, 31))
        self.bookingList = []

        while len(self.bookingList) < self.noOfPassenger:
            print(f"Seats available: {sorted(available_seats)}")
            self.seatNo = int(input("Choose a seat number:"))
            if self.seatNo in available_seats:
                self.bookingList.append(self.seatNo)
                available_seats.remove(self.seatNo)
                print(f"Seat {self.seatNo} booked successfully.")
            else:
                print("Seat already booked or invalid choice.")
            
            if len(self.bookingList) < self.noOfPassenger:
                print(f"Do you want to book another seat? (Yes/No)")
                y = input()
                if y.lower() != "yes":
                    print("Booking cancelled. You've booked the following seats:", self.bookingList)
                    break

        # Bus selection and fare calculation (unchanged logic)
        print("1. AC BUS = 5000 Fare\n2. NON AC BUS = 3000 Fare")
        self.busType = int(input("Select Bus Type  :"))
        if self.busType == 1:
            self.selectBusType = "AC BUS"
            self.busFare = self.noOfPassenger * 5000
        elif self.busType == 2:
            self.selectBusType = "NON AC BUS"
            self.busFare = self.noOfPassenger * 3000

# Saving passenger data (no change)
class PassengerDataCsv(PassengerRegistration):
    def saveInfo(self):
        try:
            with open("passengerData.csv", 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)
                for i in data:
                    self.autoInc += 1
                print("Number of Records Found In Database:", self.autoInc)
        except FileNotFoundError:
            print("File not available, creating a new file.")
            self.autoInc = 1  # If file doesn't exist, start at 1

        with open("passengerData.csv", 'a+', newline="") as f:
            w = csv.writer(f)
            w.writerow([self.autoInc, self.passengerName, self.noOfPassenger, self.departureLocation, self.destinationLocation, self.ddmmyyyy, self.bookingList, self.selectBusType, self.busFare])
            print("Data saved successfully.")
