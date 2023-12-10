
count=0
for x in range(2,2000001):
    for r in range(2,x):
        if x%r==0:
            break
    else:
        
        count=count+x
print(count)




##for x in range(2,2000001):
##    for r in range(2,x):
##        if x%r!=0:
##            break
##    else:
##        
##        count=count+x
##print(count)
