from abc import ABC , abstractmethod 

class Account(ABC) :
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @abstractmethod
    def calculateInterest(self) :
        pass

    def deposit(self , amount) : 
        self._balance += amount 
        return self._balance
    def withdraw(self , amount) : 
        if amount <= self._balance : 
            self._balance -= amount   
            return self._balance
        
        print(f"The current balance is not enough")
    
class SavingAccount(Account) : 
    
    def __init__(self, balance, account_number):
        super().__init__(balance, account_number)

    def calculateInterest(self) :
        return self ._balance * .03

class CheckingAccount(Account) : 
    def __init__(self, balance, account_number):
        super().__init__(balance, account_number)

    def calculateInterest(self) :
        return self ._balance * .01   

savingaccount   = SavingAccount(14500 , 5411148)
checkingaccount = CheckingAccount(32432 , 2201254)   

print(savingaccount.deposit(1220))
print(savingaccount.withdraw(198711) , end= "\n\n")

print(checkingaccount.deposit(190))
print(checkingaccount.withdraw(1990) , end="\n\n")

print(savingaccount.calculateInterest())
print(checkingaccount.calculateInterest())


     