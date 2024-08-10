class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def displayInfo(self):
        print(f"My Name Is: {self.__name}\nMy Age Is: {self.__age}")

class Worker:
    def __init__(self, workerID, role) -> None:
        self.__workerID = workerID
        self.__role = role

    def displayWorkerInfo(self):
        print(f"My Worker ID is {self.__workerID}\nI'm {self.__role}")

class Employee(Person, Worker):
    def __init__(self, name, age, workerID, role, employeeID, department) -> None:
        Person.__init__(self, name, age)
        Worker.__init__(self, workerID, role)
        self.__employeeID = employeeID
        self.__department = department

    def showDepartment(self):
        print(f"I Work In department: {self.__department}")    

    def displayInfo(self):
        Person.displayInfo(self)
        Worker.displayWorkerInfo(self)
        print(f"The Employee ID is: {self.__employeeID}\nI Work In department: {self.__department}")

class Contractor(Person, Worker):
    def __init__(self, name, age, workerID, role,contractDuration,project) -> None:
        Person.__init__(self, name, age)
        Worker.__init__(self, workerID, role)
        self.__contractDuration =contractDuration 
        self.__project =project 

    def displayInfo(self):
        Person.displayInfo(self)
        Worker.displayWorkerInfo(self)
        print(f"contract Duration: {self.__contractDuration}\nMy Projects is: {self.__project}")    

class Manager(Employee):
    def __init__(self, name, age, workerID, role, employeeID, department, numTeams) -> None:
        super().__init__(name, age, workerID, role, employeeID, department)
        self.__numTeams = numTeams

    def displayInfo(self):
        super().displayInfo()   
        print(f"Number Of Teams: {self.__numTeams}") 
   
    def showTeams(self):
        print(f"Number Of Teams: {self.__numTeams}")         

class Engineer(Employee): 
    def __init__(self, name, age, workerID, role, employeeID, department, specialization) -> None:
        super().__init__(name, age, workerID, role, employeeID, department)
        self.__specialization = specialization

    def showspecialization(self):
        print(f"The specialization is: {self.__specialization}")

    def displayInfo(self):
        super().displayInfo()
        print(f"The specialization is: {self.__specialization}") 

class Freelancer(Contractor):   
    def __init__(self, name, age, workerID, role, contractDuration, project,hourlyRate) -> None:
        super().__init__(name, age, workerID, role, contractDuration, project) 
        self.__hourlyRate =hourlyRate

    def displayInfo(self):
         super().displayInfo()
         print(f"hourly Rate {self.__hourlyRate}")
          

Manager1=Manager(name=input("Enter Your name: "),age=input("Enter Your Age: "),workerID=input("Enter Work ID: "),role=input("What is your Role: "),employeeID=input("Enter Your ID: "),department=input("Enter your department: "),numTeams=input("Enter Number Of Team You Have: "))
print("\nThe Manger Info:")
Manager1.displayInfo()
print("__"*40)
Engineer1=Engineer(name=input("Enter Your name: "),age=input("Enter Your Age: "),workerID=input("Enter Work ID: "),role=input("What is your Role: "),employeeID=input("Enter Your ID: "),department=input("Enter your department: "),specialization=input("Enter your specialization: "),)
print("\nThe Enginner Info:")
Engineer1.displayInfo()
print("__"*40)
Freelancer=Freelancer(name=input("Enter Your name: "),age=input("Enter Your Age: "),workerID=input("Enter Work ID: "),role=input("What is your Role: "),contractDuration=input("Enter your contract Duration: "),project=input("Enter your project: "),hourlyRate=input("Enter your hourlyRate: "))
print("\nThe Freelancer Info:")
Freelancer.displayInfo()