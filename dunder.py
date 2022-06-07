class Toy:
    def __init__(self, color, age) -> None:
        self.color = color
        self.age = age

    def __str__(self) -> str:
        return f'{self.color}'

    def __call__(self):
        return('yes')

action_figure = Toy('red',0)

print(action_figure.__str__)

print(action_figure())