class Person:
    def __init__(self, name, email, phone_number):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number

    def set_name(self, name): 
        self.__name = name
    def get_name(self): 
        return self.__name

    def set_email(self, email): 
        self.__email = email
    def get_email(self): 
        return self.__email

    def set_phone_number(self, phone_number): 
        self.__phone_number = phone_number
    def get_phone_number(self): 
        return self.__phone_number

    def display_info(self):
        print(f"My Name : {self.get_name()}\nMy Email : {self.get_email()}\nMy Phone Number : {self.get_phone_number()}")

class Manager(Person):
    def __init__(self, name, email, phone_number, ID, salary, Date_of_appointment):
        super().__init__(name, email, phone_number)
        self.__ID = ID
        self.__salary = salary
        self.__Date_of_appointment = Date_of_appointment

    def set_ID(self, ID): 
        self.__ID = ID
    def get_ID(self): 
        return self.__ID

    def set_salary(self, salary): 
        self.__salary = salary
    def get_salary(self): 
        return self.__salary

    def set_Date_of_appointment(self, Date_of_appointment): 
        self.__Date_of_appointment = Date_of_appointment
    def get_Date_of_appointment(self): 
        return self.__Date_of_appointment   

    def display_info(self):
        super().display_info()
        print(f"My ID : {self.get_ID()}\nI get a salary of {self.get_salary()}\nDate Of Appointment: {self.get_Date_of_appointment()}")

class Customer(Person):
    def __init__(self, name, email, phone_number, car_type, amount_paid, purchase_date):
        super().__init__(name, email, phone_number)
        self.__car_type = car_type
        self.__amount_paid = amount_paid
        self.__purchase_date = purchase_date
    
    def set_car_type(self, car_type): 
        self.__car_type = car_type
    def get_car_type(self): 
        return self.__car_type

    def set_amount_paid(self, amount_paid): 
        self.__amount_paid = amount_paid
    def get_amount_paid(self): 
        return self.__amount_paid
   
    def set_purchase_date(self, purchase_date): 
        self.__purchase_date = purchase_date
    def get_purchase_date(self): 
        return self.__purchase_date
    
    def display_info(self):
        super().display_info()
        print(f"The Type of car : {self.get_car_type()}\nCar purchase price : {self.get_amount_paid()}\nPurchase date : {self.get_purchase_date()}")

class Car:
    def __init__(self, name, model, year, price):
        self.name = name
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"The Car Name : {self.name}\nThe Car Model : {self.model}")
        print(f"The Car Year : {self.year}\nThe Car Price : {self.price}")

class Car_rental(Car):
    def __init__(self, name, model, year, price, Lease_period, Rental_date):
        super().__init__(name, model, year, price)
        self.__Lease_period = Lease_period
        self.__Rental_date = Rental_date

    def set_Lease_period(self, Lease_period): 
        self.__Lease_period = Lease_period
    def get_Lease_period(self): 
        return self.__Lease_period

    def set_Rental_date(self, Rental_date): 
        self.__Rental_date = Rental_date
    def get_Rental_date(self): 
        return self.__Rental_date

    def display_info(self):
        super().display_info()
        print(f"Lease period: {self.get_Lease_period()}\nRental date: {self.get_Rental_date()}") 

class Buy_Car(Car):
    def __init__(self, name, model, year, price, the_signature):
        super().__init__(name, model, year, price)
        self.__the_signature = the_signature

    def set_the_signature(self, the_signature): 
        self.__the_signature = the_signature
    def get_the_signature(self): 
        return self.__the_signature
    
    def display_info(self):
        super().display_info()
        print(f"Your signature: {self.get_the_signature()}")

class CarStore:
    def __init__(self):
        self.inventory = []

    def add_car(self, car):
        self.inventory.append(car)

    def remove_car(self, car):
        if car in self.inventory:
            self.inventory.remove(car)
        else:
            print("Car not found in inventory.")

    def list_cars(self):
        if not self.inventory:
            print("No cars available.")
        else:
            for car in self.inventory:
                car.display_info()
                print("*" * 40)


manager1 = Manager( name="Abdalla Mohamed",email="AbdallaMohamed@gmail.com",phone_number="01144552", ID="11145", salary=75000, Date_of_appointment="2002-01-15")
print("Display Manager information:")
manager1.display_info()
print("\n" + "-"*40 + "\n")

customer1 = Customer(name="Abdalla",email="abdalalmahrous@gmail.com",phone_number="01154775040",car_type="Tesla Model S",amount_paid=800000,purchase_date="2024-08-10")
print("Display Customer information:")
customer1.display_info()
print("\n" + "-"*40 + "\n")

rental_car = Car_rental("MOhamed", "Altima", 2023, 30000, "12 months", "2024-08-01")
print("Display Car Rental information:")
rental_car.display_info()
print("\n" + "-"*40 + "\n")

buy_car = Buy_Car("Tesla", "Model 3", 2024, 40000, customer1.get_name())
print("Display Buy Car information:")
buy_car.display_info()
print("\n" + "-"*40 + "\n")


store = CarStore()
car1 = Car("Tesla", "Model S", 2024, 80000)
car2 = Car("BMW", "X5", 2023, 60000)
car3 = Car("Audi", "A6", 2022, 55000)
car4 = Car("Mercedes-Benz", "C-Class", 2023, 65000)
car5 = Car("Ford", "Mustang", 2022, 45000)
car6 = Car("Chevrolet", "Camaro", 2021, 40000)
car7 = Car("Honda", "Accord", 2024, 35000)
car8 = Car("Toyota", "Camry", 2023, 30000)

store.add_car(car1)
store.add_car(car2)
store.add_car(car3)
store.add_car(car4)
store.add_car(car5)
store.add_car(car6)
store.add_car(car7)
store.add_car(car8)

print("Listing cars in the store:\n")
store.list_cars()