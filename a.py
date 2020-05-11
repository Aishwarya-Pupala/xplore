class Apartment:
    def __init__(self,fno,owner,amount):
        self.fno=fno
        self.owner=owner
        self.amount=amount 

class Apartment_demo(Apartment):
    def __init__(self): 
        pass  
   
    def getSecondMinBill(self,fno,owner,amount):
        people.append([fno,owner,amount])
        bill=[]
        if len(people)==n:
            if len(people)>1:
                for k in people:
                    bill.append(k[2])
                    bill.sort()                   # [[1,a,1000],[2,b,2000],[3,c,3000]]  len=3   
                print(bill)  
                m=bill[1]
                print(m)
            if len(people)==1:
                for l in people:
                    print(l[2])
#o1=apartment_demo(201,"a",1000)  #o2=apartment_demo(202,"b",2000)    #o3=apartment_demo(203,"c",3000)
#   bill[1000,2000,3000] ==> return 2000-->> bill[1]
if __name__=='__main__':
        people=[]  
        a=Apartment_demo()
        n=int(input())
        for i in range(n):
                fno=int(input())
                owner=input()
                amount=int(input())
                a.getSecondMinBill(fno,owner,amount)
                
        print(people)
        print()
       
