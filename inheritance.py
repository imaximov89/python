class User:
    def __init__(self, email) -> None:
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')

class Wizard(User):
    def __init__(self, name, power, email) -> None:
        #User.__init__(self, email)
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        #User.attack(self)
        print(f'Attack with power {self.power}')

class Archer(User):
    def __init__(self, name, arrows) -> None:
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'Attack with arrows: {self.arrows}')


wizard1 = Wizard('Peter', 50, 'Peter@parker.com')
archer1 = Archer('Robin', 100)
wizard1.attack()
print(wizard1.email)

print(isinstance(wizard1, object))

print(dir(wizard1))