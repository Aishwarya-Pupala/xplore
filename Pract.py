class Pract:
    def __init__(self,np):
    
        self.np=np
    def num(self):
        print("no is : "+self.np)
    

if __name__ == "__main__": 
    np=input()
    ob=Pract(np)
    ob.num()
    print("Executed when invoked directly")