list=[{'id':123, 'Name':'Kuhu', 'dept':'capgemeni'}, {'id':193, 'Name':'Animesh', 'dept':'Intern'}]
def emp(id):
    for employee in list:
        if employee['id'] == id:
            return employee
        else:
            return("you are not emplyee of this organization")
employeeId= int(input ("enter employee id "))
print(emp(employeeId))