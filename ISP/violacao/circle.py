from ishape import IShape


class Circle(IShape):
    def draw_circle(self):
        return 'Drawing a circle'

    def draw_rectangle(self):
        return self.draw_circle

    def draw_square(self):
        return self.draw_circle
