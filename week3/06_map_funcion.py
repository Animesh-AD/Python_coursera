menu = ['chocolate','lotte','pizza','chalan']

def find_menu(found):
    if found[0] == 'c':
        return print(found)

new_find = map (find_menu, menu)   # Maps take all objects in a list and applies a function. 
print(new_find)

for i in new_find:
    print(i)