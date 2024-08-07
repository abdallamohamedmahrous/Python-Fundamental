from datetime import date
class Date:
    def __init__(self,day,month,year):
        self.__day=day
        self.__month=month
        self.__year=year
    def set_day(self,day):self.__day=day 
    def get_day(self):return self.__day

    def set_month(self,month):self.__month=month 
    def get_month(self):return self.__month
    
    def set_year(self,year):self.__year=year 
    def get_year(self):return self.__year

    def subtractDate(cls , date):
        days1 = cls.__day + cls.__month * 30 + cls.__year * 365
        days2 = date.__day + date.__month * 30 + date.__year * 365
        return abs(days1-days2) 
date1  = Date(day=int(input("Enterh The Your Day date1: ")), month=int(input("Enterh The Your Month date1: ")) ,year=int(input("Enterh The Your year date1: ")))  
date2  = Date(day=int(input("\nEnterh The Your Day date2: ")), month=int(input("Enterh The Your Month date2: ")) ,year=int(input("Enterh The Your year date2: ")))  
print(date1.subtractDate(date2))
     