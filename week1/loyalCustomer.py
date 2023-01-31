loyalCust=True
totalBill=input('enter your ammount ')
totalBill=int(totalBill)
if loyalCust and totalBill>100:
            totalBill=totalBill-(float(totalBill)/100*20)
elif totalBill>100:
    totalBill=totalBill-(float(totalBill)/100*10)
elif totalBill<100:
    print('sorry no discount')
print('your total bil is '+str(totalBill))
