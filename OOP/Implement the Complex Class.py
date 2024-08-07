class Complex:
    def __init__(self,real,img):
        self.__real=real
        self.__img=img
    def set_real(self,real):self.__real=real
    def get_real(self):return self.__real

    def set_img(self,img):self.__img=img
    def get_img(self):return self.__img

    def AddComplex(self, complex_numbe):
        self.__real+=complex_numbe.__real
        self.__img +=complex_numbe.__img
        return self 
    
    def subComplex(self, complex_numbe):
        self.__real-= complex_numbe.__real
        self.__img-=complex_numbe.__img
        return self 
     
    def PrintComplex(self):
        print(f"The Complex Number  is {self.__real} + {self.__img}i")
real1=int(input("Enter The Real Number Of Complex one: "))
img1=int(input("Enter The Imag Number Of Complex one: "))
C1=Complex(real1,img1)
real2=int(input("Enter The Real Number Of Complex two: "))
img2=int(input("Enter The Imag Number Of Complex two: "))
C2=Complex(real2,img2) 
C1.AddComplex(C2)
C1.PrintComplex()
print("########################")
C3=Complex(real1,img1)
C4=Complex(real2,img2)
C3.subComplex(C4)
C3.PrintComplex()



