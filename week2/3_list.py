# remember list act as dynamic array in python 
list1 = [1, 2, 3, 4, 5]  
list2 = ['a', 'b', 'c', 7,8.0] #the main difference between list and array is that in array we can store the variable of same data type but in list we can strote different date types
list3 = [5, [5,3,2], 6, 8] #nested list
list1.insert(5,3) #inserting 5 in 3rd index
list1.insert(len(list1),9) # it will add the data in the end of the list
list3.extend([7,8,7,8]) # we can add multiple values in once like this
print(list1)
list2.append(6) #appending list in the end of the list witout any specific index
print(list2)
print(*list1) #for only printing the value inside the list
print(list2, sep=" ") #sep  is used to separate the list strings 
print(list3)

# Deletion on list

list1.pop(4) # it will delete the no 4 index item
print(list1)

del list3[1] #usign this del keyword use can delete no 1 index item 
print(list3)

# iterating in list
for i in list1:
    print('The value is: ',i)