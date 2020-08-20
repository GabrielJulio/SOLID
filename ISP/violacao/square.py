from ishape import IShape


class Square(IShape):
    def draw_circle(self):
        return self.draw_square

    def draw_rectangle(self):
        return self.draw_square

    def draw_square(self):
        return 'Drawing a square'
