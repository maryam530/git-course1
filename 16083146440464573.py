####shomaresh ara###
n =int(input())

    

l =[]
for i in range(0,n):
    test_string = input()
    l.append(test_string)
wordfreq = [l.count(p) for p in l]
k=dict(zip(l,wordfreq))

s=k.keys()
tuplex =()
for harf in s:
   tuplex=tuplex+(harf,)
    

bim=sorted(tuplex)

    



for word in  bim:
    print(word,l.count(word)) 

