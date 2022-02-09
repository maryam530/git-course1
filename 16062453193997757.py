NUM=int(input())
a=NUM%10
d=(NUM-a)//10
b=d%10
c=d//10
axNUM=a*100+b*10+c
print(axNUM*2)
