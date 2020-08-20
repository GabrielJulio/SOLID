from .cat import Cat
from .duck import Duck
from .snake import Snake

class CountLegAnimals:
    def __init__(self, animals: list):
        self.animals = animals

    def get_leg_count(self):
        for animal in self.animals:
            if isinstance(animal, Cat):
                print(cat_leg_count(animal))
            elif isinstance(animal, Cow):
                print(duck_leg_count(animal))
            elif isinstance(animal, Dog):
                print(snake_leg_count(animal))


def cat_leg_count(cat: Cat):
    return cat.get_legs()

def duck_leg_count(duck: Duck):
    return duck.get_legs()

def snake_leg_count(snake: Snake):
    return snake.get_legs()
