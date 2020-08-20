from ishape import IShape


class Rectangle(IShape):
    def draw_circle(self):
        return self.draw_rectangle

    def draw_rectangle(self):
        return 'Drawing a rectangle'

    def draw_square(self):
        return self.draw_rectangle
