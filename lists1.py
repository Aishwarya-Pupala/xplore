List = [1,2,3,4] 
List.insert(0, -1) 
List.insert(5, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 
List.extend([5, 'Geeky', 'Always']) 

print("\nList after performing Extend Operation: ") 
print(List)
print("Accessing a element from the list") 
print(List[0])  
print(List[2]) 

# Creating a Multi-Dimensional List # (By Nesting a list inside a List) 
List1 = [['Geeks', 'For'] , ['Geeks']] 
# accessing a element from the  # Multi-Dimensional List using # index number 
print("Acessing a element from a Multi-Dimensional list") 
print(List1[0][1]) #For
print(List1[1][0])  #Geeks


l3=[[1,'a',1000],[2,'b',2000],[3,'c',3000]] 
for i in range(3):
    print(l3[i][2])

print("\nList after Removal of two elements: ") 
print(List) # Removing elements from List # using iterator method 

# for j in range(0,2): 
#     List.remove(j) 
# print("\nList after Removing a range of elements: ") 
# print(List) 

List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 

Sliced_List = List[:-4] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 


list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
# Will print the index of '4' in list1 
print(list1.index(4))
list2 = ['cat', 'bat', 'mat', 'cat', 'pet'] 
# Will print the index of 'cat' in list2  
print(list2.index('cat')) 

numbers = [1, 3, 4, 2] 
numbers.sort()  
print(numbers) 
  
# List of strings 
words = ["Geeks", "For11","For2", "Geeks"] 
# Sorting list of strings 
words.sort() 
print(words) 

numbers.sort(reverse=True) 
print(numbers) 
  
# List of strings 
words = ["Geeks", "For", "Geeks"]   
# Sorting list of strings 
words.sort(reverse=True) 
print(words) 

list1 = [1, 1, 1, 2, 3, 2, 1]   
# Counts the number of times 1 appears in list1 
print(list1.count(1))    
list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']  
# Counts the number of times 'b' appears in list2 
print(list2.count('b'))  



lis1 = [ 1, 2, 3, 4 ]   
# Using copy() to create a shallow copy 
lis2 = lis1.copy()   
# Printing new list  
print ("The new list created is copy() : " + str(lis2)) 


lis = [2, 1, 3, 5, 4, 3, 8] 
  
# using del to delete elements from pos. 2 to 5 
# deletes 3,5,4 
del lis[2 : 5] 
print("delete del()",str(lis))

lis1.clear()  #clear all elements of the list


num = [1,2,3,4,5,1,4,5] 
Sum = sum(num) 
print(Sum) 
# start = 10 
Sum = sum(numbers, 10)   # sum +10
print(Sum) 

