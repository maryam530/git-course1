####shomsresh arae#####

n =int(input())

    

l =[]
for i in range(0,n):
    test_string = input()
    l.append(test_string)
wordfreq = [l.count(p) for p in l]
k=dict(zip(l,wordfreq))
print(dict(zip(l,wordfreq)))
for word in  k.keys():
    print(word,l.count(word)) 

