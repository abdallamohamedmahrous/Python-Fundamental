class Student:
    def __init__(self,name="",age=0,grade=0.0):
        self.__name=name
        self.__age=age
        self.__grade=grade

    def set_name(self,name):self.__name=name
    def get_name(self):return self.__name

    def set_age(self,age):self.__age=age 
    def get_age(self):return self.__age

    def set_grade(self,grade):self.__grade=grade 
    def get_grade(self):return self.__grade     

    def printDetails(self):
        print(f"My name is {self.__name} \nMy age is {self.__age} \nMy grade is {self.__grade}")

name=input("Enter Your Nmae: ")
age=int(input("Enter Your Age : "))
grade=float(input("Enter Your Grade :")) 

S1=Student(name,age,grade)
S1.printDetails()

      
  