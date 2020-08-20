class Animal:
    def __init__(self, name: str, legs: int):
        self.name = name
        self.legs = legs
    
    def get_name(self) -> str:
        return self.name

    def get_legs(self) -> int:
        return self.legs

    def make_sound(self) -> str:
        pass
