dict1={1:"aish",2:"pupala"}
print(dict1.keys())
print(dict1.values())
print(dict1.items())


dict1[1]="Aish"
dict1['0']="Ms"

print(dict1[1])
print(dict1.get(1))
print(dict1.get(4,"not found"))

for i,j in dict1.items():
    print(i,end=' :')
    print(j)
    
d=[(1,'a'),(2,'b'),(3,'c')]
j=dict(d)
print(type(j))
print(j)

print(j.pop(5,"non existent key"))

print(j.popitem())   #removes an arbitrary item 

del j[2] #key
print(j)

j.clear()  #clears all items
print(j)

#del j   ##deletes the dictionary
#print(j) # error    name 'j' is not defined

j2={5:"five",6:"six"}
j.update(j2)
print(j)
 
j2.update('seven'=7)
print(j2)
