from interfaces.ishape_square import IShapeSquare


class Square(IShapeSquare):
    def draw_square(self):
        return 'Drawing a square'
