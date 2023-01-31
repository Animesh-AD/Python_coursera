class superc():
    def __init__(self,fruit) -> None:
        print('i love',fruit)
class child(superc):
    def __init__(self,dub) -> None:
        super().__init__(dub)
        print("i am in base class")
apple = child('apple')