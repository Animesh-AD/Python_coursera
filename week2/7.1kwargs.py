def add(**kwargs): #keyword arguments can be passed 
                #using kwargs ** shoud be used before that
    sum=0
    for key, value in kwargs.items():
        sum +=value
    return round(sum,2) # rouding the value 

print(add(kola = 10.2501, ruti = 3.25, lassi = 11.25)) #for passing the key and valueuse (=) sign 
