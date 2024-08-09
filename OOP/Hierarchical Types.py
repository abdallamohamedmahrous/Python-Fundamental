class Vehicl:
    def __init__(self,brand,model) -> None:
        self.__brand=brand
        self.__model=model
    def displayInfo(self):
        print(f"The Brand is: {self.__brand}\nThe model is: {self.__model}")

class Car(Vehicl):
    def __init__(self, brand, model,numDoors) -> None:
        super().__init__(brand, model)
        self.__numDoors=numDoors

    def displayInfo(self):
        super().displayInfo()
        print(f"This Car Have Number door is : {self.__numDoors}")    

class Bike(Vehicl):
    def __init__(self, brand, model,numGears) -> None:
        super().__init__(brand, model)
        self.__numGears=numGears 
    def displayInfo(self):
        super().displayInfo()  
        print(f"The Number Of Gears is:{self.__numGears}")  

car1=Car(brand=input("Enter The brand car: "),model=input("Enter The Model Of Car: "),numDoors=input("Enter The Number Of Door Car:"))
print("\nThe Info Of Car: ")
car1.displayInfo()
print("#"*40)
Bike1=Bike(brand=input("\nEnter The brand Bike: "),model=input("Enter The Model Of Bike: "),numGears=input("Enter The Number Of Grears: "))
print("\nThe Info Of Bike: ")
Bike1.displayInfo()
