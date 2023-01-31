set_a={1,2,3,4,5,5}  # set is collection of uniq values
set_b={4,5,7,8,9} # set us collection of unorders values means you can not access through index
set_a.add(6) #for adding the data
set_a.remove(6) # for removing datpa
set_a.discard(5) # work same as remove
print(set_a)
print(set_a.union(set_b)) #it will merge the set into one
print(set_a |set_b) #same as union
print(set_a.intersection(set_b)) # it will pritn the common value from sets
print(set_a & set_b) #intersection
print(set_a.difference(set_b)) #it will print all the value only present in set a
print(set_a - set_b) # same as difference
print(set_a.symmetric_difference(set_b)) # it will print all accept the common values
print(set_a ^ set_b)

