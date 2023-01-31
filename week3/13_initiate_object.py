class preparation:
    def __init__(self,dish, items,time) -> None:
        self .dish =dish
        self.items =items
        self.time = time
    def contents(self):
        print('The Dish is',self.dish,'containts',self.items,
        'will take',self.time, 'minit')
pasta = preparation('pasta',['pasta','water','sauce','chili'],30)
chow = preparation('chow',['chow','water','sauce','chili'],30)
print(pasta.items)
print(chow.items)
print(pasta.contents())