class Person:
    def __init__(self,name,age) -> None:
        self.__name=name
        self.__age=age

    def displayInfo(self):
        print(f"My Name Is: {self.__name}\nMy Age Is: {self.__age}")

class Employee(Person):
    def __init__(self, name, age,employeeID,department) -> None:
        super().__init__(name, age)
        self.__employeeID=employeeID
        self.__department=department

    def showDepartment(self):print(f"I Work In department: {self.__department}")   

    def displayInfo(self):
         super().displayInfo()
         print(f"The Employee ID is: {self.__employeeID}\nI Work In department: {self.__department} ")    

class Manager(Employee):
    def __init__(self, name, age, employeeID, department,numTeams) -> None:
        super().__init__(name, age, employeeID, department)
        self.__numTeams=numTeams

    def displayInfo(self):
         super().displayInfo()   
         print(f"Number Of Team is: {self.__numTeams}") 
   
    def showTeams(self):print(f"Number Of Team is: {self.__numTeams}")

class Engineer(Employee): 
    def __init__(self, name, age, employeeID, department,specialization) -> None:
        super().__init__(name, age, employeeID, department)
        self.__specialization=specialization

    def showspecializatio(self):print(f"The specialization is: {self.__specialization}")

    def displayInfo(self):
         super().displayInfo()
         print(f"The specialization is: {self.__specialization}") 
    
Manager1=Manager(name=input("Enter Your name: "),age=input("Enter Your Age: "),employeeID=input("Enter Your ID: "),department=input("Enter your department: "),numTeams=input("Enter Number Of Team You Have: "))
print("\nThe Manger Info:")
Manager1.displayInfo()
print("__"*40)
Engineer1=Engineer(name=input("Enter Your name: "),age=input("Enter Your Age: "),employeeID=input("Enter Your ID: "),department=input("Enter your department: "),specialization=input("Enter your specialization: "))
print("\nThe Enginner Info:")
Engineer1.displayInfo()