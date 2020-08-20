class CountLegAnimals:
    def init(self, animals: list):
        self.animals = animals

    def get_leg_count(self):
        for animal in self.animals:
            return animal.leg_count()
