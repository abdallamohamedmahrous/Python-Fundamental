class University:
    def __init__(self, name ):
       self.__name=name
       self.department=[]

    def set_name(self,name):self.__name=name
    def get_name(self):return self.__name

    def add_department(self, department):
        self.department.append(department)

    def displa__department(self):
        for i in self.department:
            print(f"The Name Of department:  {i.get_departmentName()}\nThe location Of department: {i.get_location()} \nThe Head Of Department: {i.get_headOfDepartment()}")
            print("*"*40)     

class Department:
    def __init__(self,departmentName,location,headOfDepartment):
        self.__departmentName=departmentName
        self.__location=location
        self.__headOfDepartment=headOfDepartment

    def set_departmentName(self,departmentName):self.__departmentName=departmentName
    def get_departmentName(self):return self.__departmentName

    def set_location(self,location):self.__location=location
    def get_location(self):return self.__location

    def set_headOfDepartment(self,headOfDepartment):self.__headOfDepartment=headOfDepartment
    def get_headOfDepartment(self):return self.__headOfDepartment

dep1=Department(departmentName=input("Enter The department Name OF department one: "),location=input("Enter The location Of department one: "),headOfDepartment=input("Enter the head Of Department one: "))
dep2=Department(departmentName=input("Enter The department Name OF department two: "),location=input("Enter The location Of department two: "),headOfDepartment=input("Enter the head Of Department two: "))
print("\n")
Univer=University("EELU University")

Univer.add_department(dep1)
Univer.add_department(dep2)
Univer.displa__department()
print(Univer.get_name())
