##n=int(input('enter n:'))
##total=0
##for i in range(1,n+1):
##    total+=i**i
##    
##print(total)
##        
##

def Self_powers(n):
    total=0
    for i in range(1,n+1):
        total+=i**i
    return total
all_digits_in_series=Self_powers(1000)
str_all_digits=str(all_digits_in_series)
print(str_all_digits[-10:])
    

