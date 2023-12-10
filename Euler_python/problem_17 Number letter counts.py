n=1
letterscount=0 # letterscount is the letters used in total in 1 to 1000

while n<=19:
    if n==1:
        numberword='one'# numberword is the letters count just a number
    elif n==2:
        numberword='two'
    elif n==3:
        numberword='three'
    elif n==4:
        numberword='four'
    elif n==5:
        numberword='five'
    elif n==6:
        numberword='six'
    elif n==7:
        numberword='seven'
    elif n==8:
        numberword='eight'
    elif n==9:
        numberword='nine'
    elif n==10:
        numberword='ten'
    elif n==11:
        numberword='eleven'
    elif n==12:
        numberword='twelve'
    elif n==13:
        numberword='Thirteen'
    elif n==14:
        numberword='Fourteen'
    elif n==15:
        numberword='Fifteen'
    elif n==16:
        numberword='Sixteen'
    elif n==17:
        numberword='Seventeen'
    elif n==18:
        numberword='Eighteen'
    elif n==19:
        numberword='Nineteen'
    print(numberword)
    letterscount+=len(numberword)
    n+=1
print(n)
n=20    
print(letterscount)
while n<=99:
    nmberword1=''#nmberword1 is the first digit of the 20 to 100 numbers
    nmberword2=''#nmberword2 is the second digit of the 20 to 100 numbers
    strnum=str(n) # str n is the n in string form
    if strnum[0]=='2': 
        nmberword1='Twenty' 
    elif strnum[0]=='3': 
        nmberword1='Thirty'
    elif strnum[0]=='4': 
        nmberword1='Forty'
    elif strnum[0]=='5': 
        nmberword1='Fifty'
    elif strnum[0]=='6': 
        nmberword1='Sixty'
    elif strnum[0]=='7': 
        nmberword1='Seventy'
    elif strnum[0]=='8': 
        nmberword1='Eighty'
    elif strnum[0]=='9':
        nmberword1='Ninety'
        ###############
        
    if strnum[1]=='0': 
        nmberword2=''
    elif strnum[1]=='1': 
        nmberword2='one'
    elif strnum[1]=='2': 
        nmberword2='two'
    elif strnum[1]=='3': 
        nmberword2='three'
    elif strnum[1]=='4': 
        nmberword2='four'
    elif strnum[1]=='5': 
        nmberword2='five'
    elif strnum[1]=='6': 
        nmberword2='six'
    elif strnum[1]=='7': 
        nmberword2='seven'
    elif strnum[1]=='8': 
        nmberword2='eight'
    elif strnum[1]=='9': 
        nmberword2='nine'
    letterscount+=len(nmberword1)+len(nmberword2)
    print(nmberword1+nmberword2)

    n+=1
print(letterscount)
print(n)
######## for n=100 to 999
while n<=999:
    nmberword0=''#nmberword0 is the first digit of the 100 to 999 numbers
    nmberword1=''#nmberword1 is the second digit of the 100 to 999 numbers
    nmberword2=''#nmberword2 is the first digit of the 100 to 999 numbers
    strnum=str(n)
    if strnum[0]=='1': 
        nmberword0='Onehundred'
    elif strnum[0]=='2': 
        nmberword0='twohundred'
    elif strnum[0]=='3': 
        nmberword0='threehundred'
    elif strnum[0]=='4': 
        nmberword0='fourhundred'
    elif strnum[0]=='5': 
        nmberword0='fivehundred'
    elif strnum[0]=='6': 
        nmberword0='sixhundred'
    elif strnum[0]=='7': 
        nmberword0='sevenhundred'
    elif strnum[0]=='8': 
        nmberword0='eighthundred'
    elif strnum[0]=='9': 
        nmberword0='ninehundred'
    strlasttwodigit=''
    lasttwodigit=strnum[1:] #
    if int(lasttwodigit)==0: # for à00 toà19
        
        letterscount+=len(nmberword0)
        print(nmberword0)
    if int(lasttwodigit)<20 and int(lasttwodigit)>0:
        if int(lasttwodigit)==1:
            last2numberword='one'
        elif int(lasttwodigit)==2:
            last2numberword='two'
        elif int(lasttwodigit)==3:
            last2numberword='three'
        elif int(lasttwodigit)==4:
            last2numberword='four'
        elif int(lasttwodigit)==5:
            last2numberword='five'
        elif int(lasttwodigit)==6:
            last2numberword='six'
        elif int(lasttwodigit)==7:
            last2numberword='seven'
        elif int(lasttwodigit)==8:
            last2numberword='eight'
        elif int(lasttwodigit)==9:
            last2numberword='nine'
        elif int(lasttwodigit)==10:
            last2numberword='ten'
        elif int(lasttwodigit)==11:
            last2numberword='eleven'
        elif int(lasttwodigit)==12:
            last2numberword='twelve'
        elif int(lasttwodigit)==13:
            last2numberword='Thirteen'
        elif int(lasttwodigit)==14:
            last2numberword='Fourteen'
        elif int(lasttwodigit)==15:
            last2numberword='Fifteen'
        elif int(lasttwodigit)==16:
            last2numberword='Sixteen'
        elif int(lasttwodigit)==17:
            last2numberword='Seventeen'
        elif int(lasttwodigit)==18:
            last2numberword='Eighteen'
        elif int(lasttwodigit)==19:
            last2numberword='Nineteen'
        letterscount+=len(nmberword0)+3+len(last2numberword)
        print(nmberword0+'and'+last2numberword)

    
     
    if int(lasttwodigit)>=20:
    
            ######### 2nd digit
        if strnum[1]=='2': 
            nmberword1='Twenty' 
        elif strnum[1]=='3': 
            nmberword1='Thirty'
        elif strnum[1]=='4': 
            nmberword1='Forty'
        elif strnum[1]=='5': 
            nmberword1='Fifty'
        elif strnum[1]=='6': 
            nmberword1='Sixty'
        elif strnum[1]=='7': 
            nmberword1='Seventy'
        elif strnum[1]=='8': 
            nmberword1='Eighty'
        elif strnum[1]=='9':
            nmberword1='Ninety'
        
        if strnum[2]=='0': 
            nmberword2=''
        elif strnum[2]=='1': 
            nmberword2='one'
        elif strnum[2]=='2': 
            nmberword2='two'
        elif strnum[2]=='3': 
            nmberword2='three'
        elif strnum[2]=='4': 
            nmberword2='four'
        elif strnum[2]=='5': 
            nmberword2='five'
        elif strnum[2]=='6': 
            nmberword2='six'
        elif strnum[2]=='7': 
            nmberword2='seven'
        elif strnum[2]=='8': 
            nmberword2='eight'
        elif strnum[2]=='9': 
            nmberword2='nine'
        letterscount+=len(nmberword0)+len(nmberword1)+3+len(nmberword2)
        print(nmberword0+'and'+nmberword1+nmberword2)
    n=n+1

print(n)
print(letterscount+11) # 11 for the one thousand

       
        
        
