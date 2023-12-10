f1=1 # f1 is the first fibonacci number 
f2=1 # f2 is the second fibonacci number
count=2
while True:
    
    fn=f1+f2
    f1=f2
    f2=fn
    count+=1
    strfn=str(fn) # fn value in the string form
    if len(strfn)==1000:
        print(fn)
        print(count,'term')
        break

        

