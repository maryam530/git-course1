number=int(input())
for x in range(2,number):
    if number % x == 0 :
        print('not prime')
        break
else :
    print('prime')
