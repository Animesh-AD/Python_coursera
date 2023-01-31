list1 = [1,2,3,4]    # pure function means which does not effect the data outside of its scope

def add_list (passing_list, item): # here we are passign one list and another item what we want to update in the new list 
    l2 = passing_list.copy()    # here we are coping the value into another list        

    l2.append(item) # here appending the argument value to the new copy list name as l2
    return l2

new_list = add_list(list1, 6 )  # storing the returned list 

print(list1)
print(new_list)   ,


