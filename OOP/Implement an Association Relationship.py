class Course:
    def __init__(self, course_name, duration):
        self.__course_name = course_name
        self.__duration = duration

    def set_course_name(self, course_name):
        self.__course_name = course_name

    def get_course_name(self):
        return self.__course_name

    def set_duration(self, duration):
        self.__duration = duration

    def get_course_duration(self):
        return self.__duration


class Student:
    def __init__(self, name, age, rollNumber):
        self.__name = name
        self.__age = age
        self.__rollNumber = rollNumber
        self.__Courses = []

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_rollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def get_rollNumber(self):
        return self.__rollNumber

    def add_Course(self, course):
        self.__Courses.append(course)

    def enrolledCourses(self):
        for i in self.__Courses:
            print(f"course {i.get_course_name()}  {i.get_course_duration()}")


S1 = Student("Abdalla", 20, 3)
S2 = Student("Mohamed", 40, 5)

C1 = Course("AI", 5)
C2 = Course("IT", 10)
C3 = Course("DS", 15)

S1.add_Course(C1)
S1.add_Course(C2)
S1.add_Course(C3)

S1.enrolledCourses()
