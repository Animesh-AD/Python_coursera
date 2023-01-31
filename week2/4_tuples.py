from tokenize import maybe


myTouple=(5,'hi',9.0, True,'hi',9.0,9.0) #like list we can strote different data typesbut the main difference is list is mutable and touple is immutable 
print(myTouple[5]) #accecing Touple through index
print(myTouple.count(9.0)) # It will count how many times hi has been occur 
print(myTouple.index(9.0)) #it will print the only nearest one index 

# Iterating 
for i in myTouple:
    print(i)