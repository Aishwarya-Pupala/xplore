b=['abc','asd','bef']
char=input()
c=0
for i in b:
    if i[0]==char:
        c+=1
        continue
print(c)