import random
with open ('E:/tilu.txt') as file:
    a = file.read()
    new_list = a.split('\n')
    print(new_list)
    print(random.choice(new_list))