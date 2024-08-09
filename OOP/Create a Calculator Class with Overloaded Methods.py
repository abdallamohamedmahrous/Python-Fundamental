class Calculator:
    def add(self, num1=0, num2=0):
        return num1 + num2
    
    def add_three(self, num1=0.0, num2=0.0, num3=0.0):
        return num1 + num2 + num3
    
    def add_array_int(self, array):
        sum = 0
        for i in array:
            sum += i
        return sum
    
    def add_array_float(self, array):
        sum = 0.0
        for i in array:
            sum += i
        return sum

C1 = Calculator()

result1 = C1.add(5, 2)
print(result1) 

result2 = C1.add_three(1.0, 2.0, 3.0)
print(result2)  

array_int = [1, 2, 3, 4]
result3 = C1.add_array_int(array_int)
print(result3)  

array_float = [1.1, 2.2, 3.3]
result4 = C1.add_array_float(array_float)
print(result4) 
