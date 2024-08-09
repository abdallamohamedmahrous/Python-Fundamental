class City:
    def __init__(self,name_city) -> None:
        self.__name_city=name_city

    def set_name_city(self,name_city):self.__name_city=name_city
    def get_name_city(self):return self.__name_city

class State:
    def __init__(self,stateName) -> None:
        self.__stateName=stateName 
        self.cities=[] 

    def set_stateName(self,stateName):self.__stateName=stateName
    def get_stateName(self):return self.__stateName    

    def add_cities(self ,cities):
        self.cities.append(cities)

    def display_cities(self):
        for i in self.cities:
         print(f"The City in {self.get_stateName()} is: {i.get_name_city()}")

                
class Country:
    def __init__(self,countryName) -> None:
        self.__countryName=countryName
        self.states=[]

    def set_countryName(self,countryName):self.__countryName=countryName
    def get_countryName(self):return self.__countryName


    def add_states(self ,states):
        self.states.append(states)    

    def display_states(self):
        for i in self.states:
         print(f"The State in {self.get_countryName()} is: {i.get_stateName()}")    


Country=Country("Egypt")
City1=City("City")
City2=City("Fesal")

State1=State("Sohag")
State2=State("Geza")

State1.add_cities(City1)
State2.add_cities(City2)

Country.add_states(State1)
Country.add_states(State2)

print("The Country Name:",str(Country.get_countryName()))
Country.display_states()
State1.display_cities()
State2.display_cities()