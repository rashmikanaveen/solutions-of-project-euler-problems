total_sum=0
for n1 in range(1,10000): # first number that we compare
    total1=0
    for f1 in range(1,n1):  # find a factors of n1
        if n1%f1==0:
            total1+=f1    # find sumof factors
    #print(total1)    
    total2=0
    for n2 in range(1,total1): # second number that we compare
        
     
        if total1%n2==0:
            total2+=n2  # find sum of a factors total2
    if total2==n1 and n1!=total1:
        #print(n1)
        total_sum+=n1
    #print(total2)
    


##total_sumset=set(total_sum)
##total_sum=list(total_sumset)
print(total_sum)  
        
