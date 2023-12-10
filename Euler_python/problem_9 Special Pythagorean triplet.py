


n=int(input('enter the a+b+c: '))
for a in range(1,n-1):
    for b in range(1,n-1):
        if (n-(a+b))**2==a**2+b**2:
            if a<b:
                print(a,b)
                c=(n-(a+b))
                print(c)
                print(a*b*c)
            
        
