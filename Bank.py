class Person:   
    def __init__(self,bal,d1): 
        self.bal=bal
        self.d1=d1
        
class Employee(Person): 
    #super.__init()
    def deposit(self):
        balance=self.d1+self.bal
        return balance
        
if __name__ == "__main__":  
    
    d1=int(input())
    emp1 = Employee(1000,d1)  
    dep=emp1.deposit()
    print(dep)