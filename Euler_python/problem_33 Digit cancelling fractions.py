product=1# product is product of 
#import fractions library
import fractions
productlist=[]
# let get numerator as num and denominator as den
for num in range(10,100):
    for dem in range(10,100):
        if num/dem<1 :  #check wether after division is less dan 1
            strnum=str(num)# num in string form
            strdem=str(dem)# dem in string form
            listrnum=list(strnum) #assign digit of strnum in to a list
            listrdem=list(strdem) #assign digit of strdem in to a list
            if int(listrnum[0])==int(listrdem[0])  and (int(listrnum[-1])!=0 and int(listrdem[-1])!=0):
                if ((num/dem)==(int(listrnum[-1])/int(listrdem[-1]))) :
                    fract=fractions.Fraction(num,dem)
                    strfra='{}'.format(fract)
                    #print(strfra)
                    if '{}/{}'.format(num,dem)!=strfra:
                        print(num,dem)
                        if (fract in productlist) is False:
                            productlist.append(fract)
                            product=product*fract
                
            elif int(listrnum[0])==int(listrdem[-1]) and (int(listrnum[-1])!=0 and int(listrdem[-1])!=0) :
                if ((num/dem)==(int(listrnum[-1])/int(listrdem[0]))) :
                    fract=fractions.Fraction(num,dem)
                    strfra='{}'.format(fract)
                    #print(strfra)
                    if '{}/{}'.format(num,dem)!=strfra:
                        print(num,dem)
                        if (fract in productlist) is False:
                            productlist.append(fract)
                            product=product*fract
            elif int(listrnum[-1])==int(listrdem[0]) and (int(listrnum[-1])!=0 and int(listrdem[-1])!=0):
                if ((num/dem)==(int(listrnum[0])/int(listrdem[-1]))) :
                    fract=fractions.Fraction(num,dem)
                    strfra='{}'.format(fract)
                    #print(strfra)
                    if '{}/{}'.format(num,dem)!=strfra:
                        print(num,dem)
                        if (fract in productlist) is False:
                            productlist.append(fract)
                            product=product*fract
            elif int(listrnum[-1])==int(listrdem[-1]) and (int(listrnum[-1])!=0 and int(listrdem[-1])!=0):
                if ((num/dem)==(int(listrnum[0])/int(listrdem[0]))) :
                    fract=fractions.Fraction(num,dem)
                    strfra='{}'.format(fract)
                    #print(strfra)
                    if '{}/{}'.format(num,dem)!=strfra:
                        print(num,dem)
                        if (fract in productlist) is False:
                            productlist.append(fract)
                            product=product*fract
            
##            if ((num/dem)==(int(listrnum[0])/int(listrdem[0]))) :#and (int(listrnum[-1])!=0 and int(listrdem[-1])!=0) and (int(listrnum[0])!=int(listrnum[-1]))and (int(listrdem[0])!=int(listrdem[-1])) :##check wether num/dem is curious fraction
##                    fract=fractions.Fraction(num,dem)
##                    strfra='{}'.format(fract)
##                    #print(strfra)
##                    if '{}/{}'.format(num,dem)!=strfra:
##                        print(num,dem)
##                        if (fract in productlist) is False:
##                            productlist.append(fract)
                        

               
print(product)##print fraction then you can get denominator 

