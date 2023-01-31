def add(*args): # We use args for passing infinite no of non keyword arguments
    sum=0
    for i in args:
        sum +=i
    return sum

print(add(5,25,30))