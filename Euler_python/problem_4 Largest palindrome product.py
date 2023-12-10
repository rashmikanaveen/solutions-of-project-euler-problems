large_pali=0 # large_pali is the Largest palindrome product 
for i in range(100,1000): 
    for n in range(100,1000):
        pali_num=i*n
        strpali_num=str(pali_num)
        if strpali_num[::]==strpali_num[::-1]: # find  i*n is  palindrome product 
            pali=pali_num ###    if i*n is palindrome product then ;pali=pali_num 
            
            if pali>large_pali:  # choosing  Largest palindrome product
                large_pali=pali
                

print(large_pali) # print the Largest palindrome product in series of palindrome products
