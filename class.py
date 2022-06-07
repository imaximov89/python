class PlayerChar:
    membership = True

    def __init__(self, name='anonymous', age=0):
        self._name = name
        self._age = age

    def shout(self):
        print(f'My name is {self._name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

player1 = PlayerChar('Mike', '22')
player1.adding_things(2,3)

print(PlayerChar.adding_things(4,5))