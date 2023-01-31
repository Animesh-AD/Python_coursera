from itertools import count


fav=['polau','maggie','chow','chicken']
fav=['maggie','chow','chicken','polau']
for food in fav:
    if food == 'polau':
        print('my favourite is',food)  
        break                           #In break if the condition is satisfied then it will terminate the execution
    elif food =='chicken':
        continue                         #If this condition is met then it will print all execp the chicken
        print("I am in continuee")#After continue no statement can be run within that block of code
    elif food:
        pass                            # Compiler will will not check this block if we write pass 
        print('foods are',food)

else:
    print('my favourite is not present in the list')