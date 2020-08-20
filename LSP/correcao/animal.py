class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

    def make_sound(self) -> str:
        pass

    def leg_count(self) -> int:
        pass
