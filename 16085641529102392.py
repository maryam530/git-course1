###new motarjem###
n = int(input())
a =dict()

for i in range(0,n):
    
    t_str=input()
    l =t_str.split()
    a[l[0]]=l[1]

l= list(a.keys())
string=input()
w =string.split()

final1=""

for harf in w:
    if harf in l:
        final1=final1+a[harf]+" "
       
    else:
         final1=final1+harf+" "
print(final1)
