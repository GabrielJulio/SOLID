from .animal import Animal


class Snake(Animal):
    def make_sound(self) -> str:
        return 'Shh'
