import sympy # import sympy library make prime numbers more easily
import itertools # import itertoll make permutations
permu=[] #  12-digit number  that we get
primes=list(sympy.primerange(1000,9999)) # prime numbers that has 4 digits

for prime in primes: #prime is one of prime number in primes list
    if len((str(prime)))==4 and( '0' not in str(prime) ): #if  digit in prime two or  more is equal then it neglect
        permu_pr=list(itertools.permutations(str(prime),4))  # all the permutations of prime
        pr_permu=set() # this is prime permutations of prime
        for n in range(len(permu_pr)):
            permutation='' # this is one permutation of prime number
            li_permu=list(permu_pr[n])
            for i in li_permu:            
                #print(permutation,i)
                permutation+=i
            if sympy.isprime(int(permutation)): 
                pr_permu.add(permutation)
        lis_pr_permu_nu=list(pr_permu) # for collect prime permutations of prime in to list
        lis_pr_permu_nu.sort() # we make list small number  in to bigger number
        for pr_per2 in range(1,len(lis_pr_permu_nu)):
            for pr_per1 in range(len(lis_pr_permu_nu)-1):    # now we do is we subtraction number with another number in  lis_pr_permu_nu 
                differ=int(lis_pr_permu_nu[pr_per2])-int(lis_pr_permu_nu[pr_per1])
                #print(int(lis_pr_permu_nu[pr_per2]),int(lis_pr_permu_nu[pr_per1]),int(lis_pr_permu_nu[pr_per2])-int(lis_pr_permu_nu[pr_per1]))
                if str(int(lis_pr_permu_nu[pr_per2])+differ) in lis_pr_permu_nu and differ!=0 : # after we substract we get difference between 2 numbers it is differ
                    #Pr_permutations.append(prime)
                    #if prime not in Pr_permutations:
                    Pr_permutations=(lis_pr_permu_nu[pr_per1])+(lis_pr_permu_nu[pr_per2])+str(int(lis_pr_permu_nu[pr_per2])+differ) # this is concatenating the three terms in this sequence
                    if Pr_permutations not in permu :
                        print(prime,Pr_permutations)
                        permu.append(Pr_permutations)
                    #print(prime,int(lis_pr_permu_nu[pr_per2])+differ,int(lis_pr_permu_nu[pr_per2]),int(lis_pr_permu_nu[pr_per1]))
                    break # after we get prime permutation we go to break loop for that prime
        #print(lis_pr_permu_nu)

        
