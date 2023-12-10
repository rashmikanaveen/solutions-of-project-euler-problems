import math # import math library
count=0 #count is the chains, with a starting number below one million, contain exactly sixty non-repeating terms 
for n in range(1000000): # number below one million
    n2=n  #assign value of n in to n2
    #str_n2=str(n2)
    fact_ter=[n]
    non_re_turms=0 # this is the  count non-repeating terms
    while len(fact_ter)<=60:
        str_n2=str(n2) # n2 in string form
        n3=0
        for digit in str_n2:
            n3+=math.factorial(int(digit))
        if n3 not in fact_ter:
            fact_ter.append(n3) #append 
        else: 
            break
        n2=n3
    if len(fact_ter)==60:  # if  numbers  contain exactly sixty non-repeating terms 
        count+=1           # then count= count+1
        
        
        
        
print(count)
    
