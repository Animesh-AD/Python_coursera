globa_v=25 # Global variable can be accessed from anywhe
def f1():
    enclose_V=21
    def f2():
        local_b=13
        print('acces to global',globa_v)
        print('access to local',local_b) # Only can be accessed within the nested funtion
        print('access to enclose',enclose_V)
    f2() # We have to call the nested funtion inside the funtion
#print('enclose',enclose_V) #we can no access the values from outside
f1() 
