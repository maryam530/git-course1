####1+3+2+1##
def con(string):
    final=""
    for i in range(len(string)):
        final = final+string[i]+"+"
    s= len(final)-1
    final = final[:s]
    return final 
           
    

def modify(string):
    final=""
    for i in range(len(string)):
        if i% 2 == 0:
            final = final+string[i]
    return final
string = input()
string =modify(string) 
string1= ""
count = "3"
for i in string:
    if i ==count :
        string1="3" + string1
count2 = "2"
for i in string:
    if i ==count2 :
        string1="2" + string1
count1 = "1"
for i in string:
    if i ==count1 :
        string1="1" + string1
string1=con(string1)


print(string1)


