from .animal import Animal


class Duck(Animal):
    def make_sound(self) -> str:
        return 'Quack'

    def leg_count(self) -> int:
        return 2
