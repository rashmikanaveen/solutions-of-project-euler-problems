n=1 # 1 is the biginig number
count=0 # count is the count of Lychrel numbers

while n<10000:
    n2=n  # n's value assign tothe n2
    route=0
    while True: # make iterations until n2 is Lychrel number
        route+=1 # no of iterations
        str_n=str(n2) # n2 as a string
        st_re_n2=str_n[::-1] #n2's reverse as a string
        n3=n2+int(st_re_n2)
        str_n3=str(n3)
        #print(n,n2,n3)
        if route>50: # check wether n is Lychrel numbers
            #print(n)  # if iterations more than 50 then n is Lychrel number
            count+=1
            break
        if n3==int(str_n3[::-1]):
            #print(n,n2,n3)
            break
        n2=n3  # n3's value assign to the n2
        
        
        
        
    n+=1  # to continue n seqence
    
    
print(count) # to print How many Lychrel numbers are there below ten-thousand?
