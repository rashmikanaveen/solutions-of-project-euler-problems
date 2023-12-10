max_sum=0
for a in range(100):      # a is the base
    for b in range(100):   # b is the power
        sum_of_digits=0  # sum of the digits in the power_numbres
        power_numbres=a**b
        str_num=str(power_numbres)  # str form of numbers
        for digit in str_num:   # calculate sum of the digits 
            sum_of_digits+=int(digit)
        if sum_of_digits>=max_sum:
            max_sum=sum_of_digits # assign max  tibit sum of a**b in to max_sum
print(max_sum)
