string = input()
string = string.lower()
vow = 'aeiou'
for harf in string:
    if harf in vow:
         s=string.find(harf)
         string_j =string[:s] +string[s+1 :]
         string = string_j

t = 0
for char in string :
   
   string =string[:t] +'.'+string[t:]
   t= t+2
print(string)
