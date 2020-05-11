class Person(object): 
       
    # Constructor 
    def __init__(self, name,salary): 
        self.name = name 
        self.salary=salary

class Employee(Person): 
    def getSal(self,other):
        if self.salary>other.salary:
            print("Emp1 has higher salary")
        elif self.salary<other.salary:
            print("Emp2 has higher salary")  
        else:
            print("Both emp1 and emp2 has equal salary")  

if __name__ == "__main__":  
    s1=int(input())
    s2=int(input())

    emp1 = Employee("Geek1",s1)  # An Object of Person \
    emp2= Employee("Geek2",s2)
    emp1.getSal(emp2)
   