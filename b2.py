class Person:   
    def __init__(self,l) :
        self.l=l
class Employee(Person): 
    
    def leaveCheck(self):
       
        for i,j in leave.items():
            if i!=self.l:
                continue
            else:
                print(j)
 
if __name__ == "__main__":   
    leave={"l":2,"m":3,"h":5}
    l=input()
    emp1=Employee(l)
    emp1.leaveCheck()
    