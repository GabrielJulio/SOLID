from .animal import Animal


class Duck(Animal):
    def make_sound(self) -> str:
        return 'Quack'
