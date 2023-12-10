all_terms=[] # make a list for terms
for a in range(2,101):  # a is base and 2 ≤ a ≤ 100
    for b in range(2,101):  #  b is power and 2 ≤ b ≤ 100
        all_terms.append(a**b) # add terms to list
all_terms_set=set(all_terms) # eliminate  same items from list
all_terms=list(all_terms_set) # again make list
print(len(all_terms))
