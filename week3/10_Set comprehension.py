set_a = {x for x in range(10,20) if x not in [14,16,18]}  # same as list but list uses square bracket and its uses curly braces
print(set_a)  #You can see the code format is similar to what I used in list comprehensions.
# For the sake of showing versatility, I used the "not in" keywords to check the values in the list. The output is the values in ranges 10 and 20 that are not present in that list.

list_b= [x for x in range(10,20) if x not in [14,16,18]]   # this is in list for showing the differneces 
print(list_b)