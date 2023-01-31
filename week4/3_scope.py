
def d():
    animal = 'elephant'
    def e():
            nonlocal animal   # for calling the function which is not local to that function
            animal = 'giraffe'    # it will override the base functions varibale 
            print('I am in Nested '+animal)
    print('before callling function '+animal)
    e()
    print('after calling nested function'+animal)  # as we can see the effect of line 6 it changes the value of animal but for this function not in global variable
animal = 'camel'
d()
print('the animal is '+animal+' here')

