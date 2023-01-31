with open('F:\hi.txt',mode='r') as file: #better as Exeption handelling it will close the file automaically
    data=file.readlines()
    print(data)
    