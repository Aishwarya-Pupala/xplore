people = {"Jay", "Idrish", "Archi"} 
  
print("People:", end = " ") 
print(people) 
  
# This will add Daxit  # in the set 
people.add("Archi") 
print(people) 

no={1,2,3,4}
no.add(4)
print(no)

people1= {"Jay", "Idrish", "Archil"} 
vampires = {"Karan", "Arjun"} 
dracula = {"Deepanshu", "Raju"} 
  
# Union using union()  # function 
population = people1.union(vampires) 
  
print("Union using union() function") 
print(population) 
  
# Union using "|" # operator 
population = people1|dracula 
  
print("\nUnion using '|' operator") 
print(population) 

set1 = set() 
set2 = set() 
for i in range(5): 
    set1.add(i)   
for i in range(3,9): 
    set2.add(i) 
# Intersection using # intersection() function 
set3 = set1.intersection(set2) 
print("Intersection using intersection() function") 
print(set3) 
  # Intersection using  # "&" operator 
set3 = set1 & set2 
  
print("\nIntersection using '&' operator") 
print(set3) 

set3 = set1.difference(set2)  
print(" Difference of two sets using difference() function") 
print(set3) 
# Difference of two sets # using '-' operator 
set3 = set1 - set2 
print("\nDifference of two sets using '-' operator") 
print(set3) 


set1 = {1,2,3,4,5,6}   
print("Initial set") 
print(set1)  
# This method will remove # all the elements of the set 
set1.clear()  
print("\nSet after using clear() function") 
print(set1) 
