#Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets. 
# They are also more memory efficient as compared to list comprehensions. For example:

data = [2,3,5,7,11,13,17,19,23,29,31]
generator_obj = (x for x in data )
print(generator_obj)
print(type(generator_obj))
for i in generator_obj:
    print(i, end=' ')