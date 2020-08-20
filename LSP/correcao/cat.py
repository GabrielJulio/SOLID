from .animal import Animal


class Cat(Animal):
    def make_sound(self) -> str:
        return 'Meow'

    def leg_count(self) -> int:
        return 4
