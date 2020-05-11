class Employee:
        def __init__(self,name,id,age,gender):
                self.name=name
                self.id=id
                self.age=age
                self.gender=gender

class Organisation(Employee):
        def __init__(self,O_name,employees):
                self.O_name=O_name
                self.employees=employees
                
        def addEmployee(self,name,id,age,gender):

            self.employees.append([name,id,age,gender])
            return self.employees
        
        def getEmployeeCount(self):
                return len(self.employees)

        def findEmployeeAge(self,id):
                for j in self.employees:
                    
                    if id in j: 
                        return j[2]  
                        
                   
                    if id not in j:
                        continue
                return -1

        def countEmployee(self,age):      
            count=[]
            for k in self.employees:
                    if k[2]>age:
                         count.append("1")
                         ###print(self.name)
                         
                    elif k[2]<=age:
                        continue
            l=len(count)
            if len(count)==0:
                return 0
            else:
                return l
                       

if __name__=='__main__':
        employees=[]  
        o=Organisation('XYZ',employees)
        n=int(input())
        for i in range(n):
                name=input()
                id=int(input())
                age=int(input())
                gender=input()
                o.addEmployee(name,id,age,gender)
        id=int(input())
        age=int(input())
        print(o.getEmployeeCount())
        print(o.findEmployeeAge(id))
        print(o.countEmployee(age))

       

