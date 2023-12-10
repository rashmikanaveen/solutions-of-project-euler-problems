##firstyou want to downlord sympy


# make definition to makes all rotations of  n
def rota(n):
    str_n=str(n)# n in string form
    rot_of_n=[] # for collect rotations of  n 
    for i in range(len(str_n)):
        rot_of_n.append(int(str_n[i:]+str_n[:i]))
    return rot_of_n # return a list it include all rotations of  n
#print(rota(37))


import sympy # import sympy library generate prime numbers below k,k numberis we wont
Cir_primes=[] # for collect all Circular primes
pr_num=list(sympy.primerange(1000000)) # all prime numbers below k
for prime in pr_num : # get each primes in list individually
    rota_of_n=rota(prime)# this is rotations of prime number 
    chea_ro=[sympy.isprime(i) for i in rota_of_n ]# we check rotations are prime or not
    if all(chea_ro) is True:
        Cir_primes.append(prime)
#print(Cir_primes)
print(len(Cir_primes))
