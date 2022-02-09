######HELLO##########

string = input()
sum =0


k=string.find("h")

if k!= -1:
    sum = sum+1
    
    string1 =string[k+1:]
    
    k=string1.find("e")
    
    if k!= -1:
        sum = sum+1
        string2 =string1[k+1:]
        
        k=string2.find("l") 
        if k!= -1:
           sum = sum+1 
           string3 =string2[k+1:] 
           k=string3.find("l")
           
           if k!= -1:
               sum = sum+1 
               string4 =string3[k+1:]
               k=string4.find("o")
               if k!= -1:
                   sum = sum+1 
                  
                     
if sum>= 5:
    print("YES")
else:
    print("NO")

    
                                      
    

        
        
    
   
    
