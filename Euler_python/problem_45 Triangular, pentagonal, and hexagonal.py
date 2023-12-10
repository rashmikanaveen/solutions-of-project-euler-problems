def Tri_num(n1):  # Tri_num is the Triangle numbers 
    Triangle_num=int((n1*(n1+1))/2)
    return Triangle_num
    #print(Triangle_num)

def Pent_num(n2):  # Tri_num is the Pentagonal numbers 
    Pentagonal_num=int((n2*(3*n2-1))/2)
    return Pentagonal_num
    #print(Pentagonal_num)

      
def Hex_num(n3):  # Tri_num is the Hexagonal numbers 
    Hexagonal_num=int((n3*(2*n3-1)))
    return Hexagonal_num
    #print(Hexagonal_num)
equal_count=0 # the triangle number that is also pentagonal and hexagonal
Triangle=[] # Triangle is the list of Triangle numbres
Pentagonal=[]  # Pentagonal is the list of Pentagonal numbers
Hexagonal=[]  # Hexagonal is the list of Hexagonal number
n=1 # start a seqence
max_tri=0
while True:
    Hexagonal.append(Hex_num(n))
    Pentagonal.append(Pent_num(n))
    Triangle.append(Tri_num(n))
    

    if (Tri_num(n) in Pentagonal)and (Tri_num(n) in Hexagonal):
        if n>285:
            print(Tri_num(n))
            break
    n+=1    
            
##    for t3 in Hexagonal: # t3 is the term of Hexagonal
##        for t2 in Pentagonal:    # t2 is the term of Pentagonal
##            for t1 in Triangle:  # t1 is the term of Triangle
##                #print(n,t1,t2,t3,sep='\t')
##                if t3==t2:
##                    if t3==t1:
##                        
##                        break
##                    
##    n+=1                     
####                    
##                    #print(n,t1,t2,t3,sep='\t')
##                    
##                    #print(n)
##                    #break
####                    equal_count+=1
####                    if equal_count==2:
####                        print(n)
##                    
##      
##    
##print(Triangle)
##print(Pentagonal)
##print(Hexagonal)




