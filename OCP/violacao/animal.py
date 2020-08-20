class Animal:
    def __init__(self, name: str, specie: str):
        self.name = name
        self.specie = specie
    
    def get_name(self) -> str:
        pass

    def get_specie(self) -> str:
        pass

    def make_sound(self) - str:
        if self.specie = 'cat'
            return 'meow'
        elif self.specie = 'cow':
            return 'moo'
        elif self.specie = 'dog':
            return 'woof'
        pass
