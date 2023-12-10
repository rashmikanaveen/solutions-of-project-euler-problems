#import math library
import math
#create a definition for ncr notation
def ncr(n,r): # ncrn in the ncr notation
    ncrn=int((math.factorial(n))/((math.factorial(r))*(math.factorial(n-r))))
    return ncrn
#print(ncr(5,3))
# count is the count of numbers they are ncr values greater than one-million?
count=0
for n in range(1,101): # because n must  1<=n<=100
    for r in range(1,n+1):# this r's range
        value=ncr(n,r)
        if value>1000000:
            count+=1
print(count)
            
