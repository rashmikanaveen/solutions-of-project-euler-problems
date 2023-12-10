sum_Pand=[]  #  make list for colect Pandigital products
n=1000# n is the whole numbres
while n<=10000:
    n_list=list(str(n)) # n_list is n in str form
    #print(n_list)
    for i in range(1,int(n**0.5)+1): # for find factors of n
        if n%i==0:   # for find factors of n
            #print(i,int(n/i))
            str_i=str(i)   # assign i in to in to string form
            str_ni=str(int(n/i))  # assign n/i in to string form
            l_i=list(str_i)   # assign str_i in to list
            #print(l_i)
            l_ni=list(str_ni)  # assign str_i in to list
            #print(l_ni,i)
            #print(l_i+l_ni)
            #print(set(l_i+l_ni+n_list))
            if len(l_i+l_ni+n_list)==9:
                if (set(l_i+l_ni+n_list))=={'1','2','3','4','5','6','7','8','9'}:
                    sum_Pand.append(n) # append Pandigital products to list
                    print(n,i)
                    break
            if len(l_i+l_ni+n_list)>9:
                break
    
    sum_Pand_set=set(sum_Pand)
    sum_Pand=list(sum_Pand)
    n+=1
    
print(sum(sum_Pand)) #print sum of Pandigital products numbers
