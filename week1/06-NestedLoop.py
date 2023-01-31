import time
start_time=time.time() # Start time will intialize when we run the script
for i in range(1000): #The no of times the loop will continue  means 2 rows
    for j in range(100): # the no of time inner loop will exeute means 5 colloums
        print(0, end=" ") #Here (end=' ') indicates that the end character has to be identified by whitespace and not a newline.
    print() # It will print a blank like after one full iteration

print(round(time.time()-start_time),2) # we are substraction present time - initial time where we starte