########laptop###

n =int(input())
price =[]
value=[]
for i in range(1,n+1):
    s=input()
    l=s.split()
    #print(l)

    price.append(int(l[0]))
    value.append(int(l[1]))
#print(price)
#print(value)
count =0
for i in range(0,n):
    for j in range(0,n):
        
        if price[i]<price[j] and value[i]>value[j]:
            
            count =count+1
#print(count)
if count>=1 :
    print("happy irsa")
else:
    print("poor irsa")
    
        


