#####capital###

string =input()
count1 =0
count2 =0
for i in string:
    if(i.islower()):
       count1=count1+1
    elif(i.isupper()):
       count2=count2+1
if count1<count2 :
    string1 =string.upper()
    
else:
    string1=string.lower()
print(string1)
        
