class Person:   
    def __init__(self,name,bal): 
        self.name=name
        self.bal=bal
      
class Employee(Person): 
    #super.__init()
    def deposit(self,d_amount):
        self.bal=d_amount+self.bal
        return self.bal
    
    def withdraw(self,w_amount):
        if w_amount<=self.bal:
            self.bal=self.bal-w_amount
            return self.bal
        
if __name__ == "__main__":   
    
    d_amount=int(input())
    w_amount=int(input())
    emp1 = Employee("Jack",1000)
    deposit_amount=emp1.deposit(d_amount)
    with_d=emp1.withdraw(w_amount)
    print("Balance after deposit is {0} ".format(deposit_amount))
    print("Balance after wihdrawing is {0}".format(with_d))
 