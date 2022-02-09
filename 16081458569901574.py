####kabedi player###

t= int(input())
s= input()
p= s.split()
p1 =[]
p2 =[]
for i in range(len(p)):
    p1.append(p[i])
for ozv in p1:
    if int(ozv)<3:
        p2.append(ozv)
d =len(p2)//3
print(d)
