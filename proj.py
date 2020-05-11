
class Student:
    def __init__(self,id,name,cls,batch):
        self.id=id
        self.name=name
        self.cls=cls
        self.batch=batch
    
class   Project(Student):
    def __init__(self,ilist,p_name,p_guide):
        self.ilist=ilist
        self.p_name=p_name
        self.p_guide=p_guide

    def proj(self):
        print(new)
        
        
#[{},,cls,batch,p_name,p_guide]

if __name__=='__main__':
    ilist={}
    pro=[]
    new=[]  #,cls,batch,p_name,p_guide
    icount=int(input())
    for i in range(icount):
        id=int(input())
        name=input()
        cls=input()
        batch=input()
        ilist[id]=name
        p_name=input()
        pro.append(p_name)
        p_guide=input()
        
        s=Student(id,name,cls,batch)
        p=Project(ilist,p_name,p_guide)
        new.append([ilist,cls,batch,p_name,p_guide])
    p.proj()