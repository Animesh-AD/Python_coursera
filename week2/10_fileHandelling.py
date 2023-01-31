file=open('text.txt','r') #if you use like this you have to close the file
data=file.read().splitlines() #Only readlines() will give you the output like that is the reson to use the read()and splitlines()
                      #['hi \n', 'my name is animesh\n', 'i an currenly in cdac\n'] 
print(data)
file.close() #clossing the file
