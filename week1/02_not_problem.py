current = True

if current: # Here current is true that is the reason it enters into that block
    current = False # Next we assign current to False
    print('Turning light off')

if not current:  # in the previous conditon current set to False then the condition is true it will enter into that block
    current = True
    print('Turning light on')