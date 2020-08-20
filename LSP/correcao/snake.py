from .animal import Animal


class Snake(Animal):
    def make_sound(self) -> str:
        return 'Shh'

    def leg_count(self) -> int:
        return 0
