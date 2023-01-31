list_size=int(input('enter your list size '))
list1=[]
for i in range (list_size):
    user_input=int(input('enter the no '))
    list1.append(user_input)
print(list1)
sum_num= 0
for i in list1:
    sum_num+=i
print(sum_num)