class House:
    room_number = 8
    bathroom_number = 4

    def cost_calculation(self,rate):
        return rate *self.room_number
    
house = House()
print(house.room_number)
print(House.room_number)
house.room_number=9  # here we can see that only objects room_number is changed not in main class
print(House.room_number)
print(house.room_number)
print(house.cost_calculation(10)) # it will work for instance not for main function it i understand the process then i will update