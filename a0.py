class Apartment:
    def __init__(self,fno,owner,amount):
        self.fno=fno
        self.owner=owner
        self.amount=amount 
         
class Apartment_demo(Apartment):
    def __init__(self):
        self.people=people
        super().__init__(fno,owner,amount)
        pass  
   
    def getSecondMinBill(self):
        self.people.append([self.fno,self.owner,self.amount])
        bill=[]
        for i in self.people:
            bill.append(i[2])
            bill.sort() 
        print(self.people)
        print(bill)  
        k=bill[1]
        return k      
#o1=apartment_demo(201,"a",1000)  #o2=apartment_demo(202,"b",2000)    #o3=apartment_demo(203,"c",3000)
#   bill[1000,2000,3000] ==> return 2000-->> bill[1]
if __name__=='__main__':
        people=[]  
        
        n=int(input())
        for i in range(n):
                fno=int(input())
                owner=input()
                amount=int(input())
                a=Apartment_demo()
        l=a.getSecondMinBill()
        print(people)
        print(l)
       
