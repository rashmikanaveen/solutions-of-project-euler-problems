count89=0 #count is the count count of the starting numbers below ten million will arrive at 89
count1=0
n=1
while n<10000000: # below ten million
    #print(n)
    n2=n
     
    while True:
        inter_sum=0
        strn=str(n2)
         # inter_sum is the sum of digits square
        for i in range(len(strn)):
            inter_sum+=int(strn[i])**2
        #print(n2)
        
        if n2==1:
            count1+=1
            break             #Therefore any chain that arrives at 1 or 89 
        elif n2==89:            #will become stuck in an endless loop
            #print(n)
            count89+=1
            break
        n2=inter_sum
        
    n+=1
        
        
print(count89)
print(count1)
