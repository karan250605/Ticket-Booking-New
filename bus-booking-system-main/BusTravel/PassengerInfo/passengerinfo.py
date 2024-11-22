import csv

class PassengerRegistration():
    #constructor
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
        self.countcol= 0
        
    def getPassengerInfo(self):
        self.passengerName     = input("Enter Passenger Name  :")
        self.noOfPassenger     = int(input("Enter Number Of Passengers :"))
        print("1: Trichy")
        print("2: Chennai")
        print("3: Thanjavur")
        print("4: Madurai")

        # Enter departure Location Name START
        self.dl = int(input("Enter Departure Location :"))
        if self.dl == 1:
            self.departureLocation = "Trichy"
        elif self.dl == 2:
            self.departureLocation = "Chennai"
        elif self.dl == 3:
            self.departureLocation = "Thanjavur"
        elif self.dl == 4:
            self.departureLocation = " Madurai"
        else:
            print("Please Enter correct choice  :")
        # departure Location Name END
        
        print("1: Karur")
        print("2: Ooty")
        print("3: Erode")
        print("4: Coimbatore")
        # Enter destination Location Name START
        self.dpl = int(input("Enter Destination Location  :"))
        if self.dpl == 1:
            self.destinationLocation = "Karur"
        elif self.dpl == 2:
            self.destinationLocation = "Ooty"
        elif self.dpl == 3:
            self.destinationLocation = "Erode"
        elif self.dpl == 4:
            self.destinationLocation = "Coimbatore"
        # Enter destination Location Name END

        self.ddmmyyyy = input("Enter Date of Journey Like 07-05-1992   :")  #Date of Journey

        #Booking Seat Start 
        print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
        print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
        print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")

        seatNoList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.bookingList=[]
        while True:
            self.seatNo = int(input("Choose a Seat Number & Max To Max You Can Book Two Ticket  :"))
            if self.seatNo <=30:
                
                if  self.seatNo in seatNoList:
                    self.bookingList.append(self.seatNo)
                    del seatNoList[self.seatNo+1]
                    count = len(seatNoList)
                else:
                    print("Ticket Already Booked")
                print("Do You Want To Book One More Seat Enter (Yes/No)") 
                y = input("") 
                if y == "Yes":
                    pass
                else:
                    break

            else:
                print("Don't Choose a Seat Number Which is Not Available")    
        # Booking Seat END
        
        print(" 1. AC BUS     = 5000 Fare")
        print(" 2. NON AC BUS = 3000 Fare")
        self.busType = int(input("Select Bus Type  :"))
        
        if self.busType == 1:
            self.selectBusType = "AC BUS"
            self.busFare = self.noOfPassenger*5000
        elif self.busType == 2:
            self.selectBusType = "NON AC BUS"
            self.busFare = self.noOfPassenger*3000
           
        # Booking Seat END
#=============================================
#saving Passenger Data into csv File
#=============================================
class PassengerDataCsv(PassengerRegistration):
    def saveInfo(self):
        try:
            with open("passengerData.csv",'r+',newline="") as f:
                r =  csv.reader(f)
                data = list(r)
                #print(self.data)
                for  i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol +=1
                    print()
                print("Number of Records Are Found In Database :",self.autoInc)    
            
        except:
            print("File has not available")
        finally:     
            with open("passengerData.csv",'a+',newline="") as f:
                w =  csv.writer(f)
                #w.writerow(["Auto Increment","passenger Name","Number of Passenger","Departure Location","Destination Location","ddmmyyyy","Seat No","Select Bus Type","Bus Fare"])
                w.writerow([self.autoInc,self.passengerName,self.noOfPassenger,self.departureLocation,self.destinationLocation,self.ddmmyyyy,self.bookingList,self.selectBusType,self.busFare])
                print("Data Save successfully")
                print()
        

'''pd_obj = PassengerDataCsv()
pd_obj.getPassengerInfo()
pd_obj.saveInfo()'''
