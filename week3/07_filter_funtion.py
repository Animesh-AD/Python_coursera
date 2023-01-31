menu = ['chocolate','lotte','pizza','chalan']

def find_menu(found):
    if found[0] == 'c':
        return print(found)

new_find = filter(find_menu, menu)
print(new_find)
for i in new_find:   #Filters do the same, but take the results and creates a new list with only the true values.
    print(i)
