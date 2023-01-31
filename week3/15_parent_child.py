class employee():
    def __init__(self,name,last) -> None:
        self.name=name
        self.last=last
class supervisor(employee):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
class chef(employee):
    def leave(self,days):
        return "I need leave"+'for '+str(days)+'days'

Animesh = supervisor('Animesh','das','jack')
jack = chef('jack','j')

print(jack.leave(3))
print(Animesh.password)