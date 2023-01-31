class payment_status():
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount
    def pay(self):
        self.payment='yes'
    def status(self):
        if self.payment =='yes':
            return (self.name +' paid whole amount ')
        else:
            return(self.name+' due amount '+str(self.amount))
raju = payment_status('raju','no',1000)  # here we can see that raju status in no 
kalu= payment_status('raju','yes',1000)
raju.pay()  # but after calling that function it became yes like how we get out status paid after paying online

print(raju.status(),'\n', kalu.status())
