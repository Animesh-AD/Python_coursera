def devide(a,b):
    return print(a / b)

try:
    ans=devide(20,0) 
except Exception as c:
    print(c,'something went wrong !')
    print(c.__class__) # for which the error is occuring