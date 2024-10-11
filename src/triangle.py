from src.figure import Figure

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_b <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        elif side_a > side_b + side_c:
            raise ValueError("Every side of Triangle should be less than sum of other sides")
        elif side_b > side_a + side_c:
            raise ValueError("Every side of Triangle should be less than sum of other sides")
        elif side_c > side_b + side_a:
            raise ValueError("Every side of Triangle should be less than sum of other sides")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


    @property
    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c)/2
        return (s*(s-self.side_a)*(s-self.side_b)*(s-self.side_c)) ** 0.5

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b + self.side_c) * 2