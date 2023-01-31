erroCode=int(input('enter ther error code '))
match erroCode:  #match function is intruduced after pyton 3.10
    case 400 | 401:  # it will mach the value with given value, here | is or
        print('Eroor in server')
    case 503 :
        print("Network error") 
print('unknown error')
