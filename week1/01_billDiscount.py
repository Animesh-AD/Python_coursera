total_bill=int(input("Enter the customer Bill: ")) # we are getting input from the user and we are Expecitly typecasting
if total_bill>100 and total_bill<200: # It will check the both conditon then it will execute
    print("You got Discount! Your Bill is more than 100 ")
    total_bill=(total_bill*90)/100
    print("Your total bill is :"+str(total_bill))
elif total_bill>200: # elif condition will execute if above code does not execute
    print("You got Discount! Your Bill is more than 200 ")
    total_bill=(total_bill*85)/100
    print("Yout total Bill is: "+str(total_bill))
else:                                                   
    print("Your total Bill is :"+str(total_bill))
