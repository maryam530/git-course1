def divisor (num):
    
    

    count = 1
    for i in range (1,num):
        if num % i==0 :
           count = count + 1
    return(count)

count = 1
for i in range (1,21):
    
                     
    num = int(input())
    a = divisor(num)
    if a > count:
        count=a
        b= num
    if a==count:
        if num > b:
            b = num
print(b,count)
    
   
