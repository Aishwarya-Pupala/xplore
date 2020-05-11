
#a:1 b=:2 c=3
l=[]
def smallest_vowel(s):
    for i in s:
    
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
            l.append(ord(i))
            l.sort()
            k=l[0]
    return k
    
s=input()
r=smallest_vowel(s)
print(r)