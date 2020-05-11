# x=0
# if ["a"] or ("a"):
#     x+=1
# print(x)

List = [1, 2, 3, 4, 5, 6,  
        7, 8, 9, 10, 11, 12] 
print("Intial List: ") 
print(List) 
  
# Removing elements from List 
# using Remove() method 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 
  
# Removing elements from List 
# using iterator method 
for i in range(1, 5): 
    List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 