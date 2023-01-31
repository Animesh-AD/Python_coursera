import pandas as pd
a =pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                    'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})
print(a)
print (a.describe())
b = pd.DataFrame({'letters':['a','b','c','d','e'],
                'numbers':[12,9,8,4,5]})
print(b.sort_values(by='numbers'))
# print(b)
b = b.assign(new_value= b['numbers']*3)
print(b)
'''
The first output is for the DataFrame called a that displays the output in a very systematic format.

The second output uses the describe() function in pandas that will give the count, frequency, top 
values and frequency among other values.

In the second DataFrame, b consists of letters and numbers in random order.

The third output is a sorting function that will provide a sorted table leading to shuffling of
 the data entries in the table.

Lastly, the assign() function takes the values present inside the table, performs an operation
 over them and creates a new variable called new_values that is then added to the table.'''