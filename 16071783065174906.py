num = int(input())
age = []
while num != -1 :
    age.append(num)
    num = int(input())
    a=0
for i in age:
    if i >a :
        a=i
b = 0
for i in age:
    if  i!=a :
        if i > b:
            b=i
print(a,b)

    
