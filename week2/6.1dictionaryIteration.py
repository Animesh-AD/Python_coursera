myDict={1:'hello', 'animesh':'kuhu', 1:'hi'}
for i in myDict:
    print(i) #it will print the only key 

#For printing the key with value we have to iterate like below
for key, value in myDict.items():
    print(str(key) +' :' + value)