
class Student:
    def __init__(self,pro):
        self.pro=pro

class Project(Student):
    def __init__(self):
        super().__init__(pro)

        
    def proj_chk(self):
        print(self.pro)
        for p in range(len(pro)):   # 0,1,2
            for k in range(1,len(pro)):  # 1,2
                if pro[p][3]==pro[k][3] and k>p and p!=k:
                    print("project name repeated for title :{0} for group no {1} and {2}".format(pro[p][3],pro[p][4],pro[k][4]))
                    
                if pro[p][3]!=pro[k][3] and k>p and p!=k:
                    print("project registration done for title {0} for group no {1} ".format(pro[p][3],pro[p][4]))
                
            

if __name__=='__main__':

    pro=[]
    icount=int(input())         #    [ [],[] ,[]]
    for i in range(icount):
        stud_d={}
        for j in range(3):
            id=int(input())           
            name=input()
            stud_d[id]=name
        cls=input()
        batch=input()
        p_name=input()
        g_no=int(input())
        pro.append([stud_d,cls,batch,p_name,g_no]) 
    
        p=Project()
    
    p.proj_chk()



#####inputs###############
# 3
# 1
# a
# 2
# b
# 3
# c
# a
# a1
# ovccd
# 001
# 4
# t
# 5
# 6
# 7
# 8
# a
# a1
# bcs
# 002
# 7
# q
# 8
# w
# 9
# e
# a
# a1
# ovccd
# 003   
