s="welcome"

count=0


keyList =list(s)
  
# initialize dictionary 
d = {} 

for i in keyList: 
    if i not in d:
        d[i] = 0
counter=0       

l=list(s)
m=len(l)
for j in range(0,m):
    for k in range(1,m):
        if l[j]==l[k] and j!=k and j<k:
            char=l[j]
            for p,q in d.items():
                if d[p]==char:
                    counter+=1
                    d[q]=counter
                    print(d[q])
    
print(d) 
print(d.values())