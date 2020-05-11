x=list(map(int,input().split()))              #x=input().split()
#1 2
#[1, 2]
                                              # 1 2 3 4 5
                                              # ['1', '2', '3', '4', '5']   --->STRING
print(x)                  


y,z=input().split()                  # 1 2   #extra space--  > problem
print(y)                             # 1
print(z)                             # 2



n = int(input("Enter number of elements : ")) 
# Below line read inputs from user using map() function  
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]   
print("\nList is - ", a) 


#l,m=list(map(int,input().split()))


