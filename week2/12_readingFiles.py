'''with open ('text.txt.','r') as file: 
    #print(file.read()) # It will print the entire file like file.readlines()
    print(file.read(4)) #It will print the first 4 letter from the text
   # print(file.readlines()) #it will pritn in [] list but in straight line
    file.readline # wille print the first line of the text

    for i in file: #with function allow us to itterate because its output is list

        print(i) # it will print the content line by line'''
 
with open('newtext.txt','r') as file:
    print(file.read())