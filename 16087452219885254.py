###SQRT###

from math import sqrt
user_input = int(input())
my_list = []
for i in range(user_input):
    
    
    num = float(input())
    new = str(sqrt(num))
    new2 = new.split('.')
    
    sahih = new2[0]
    ashari = new2[1]
    ashari = str(ashari[:4])
    if ashari == '0':
        ashari = '0000'
    
    final = sahih+"."+ashari
    my_list.append(final)
for i in my_list:
    print(i)
