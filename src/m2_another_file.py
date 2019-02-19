# Tommys file for more stuff


class Bowl:
    def __init__(self):
        self.flour_count, self.water_count, self.yeast_count = initialize_variables()

    def add_to_the_bowl(self, color):
        if color is 'white':
            self.flour_count = self.flour_count + 1
        elif color is 'blue':
            self.water_count = self.water_count + 1
        elif color is 'yellow':
            self.yeast_count = self.yeast_count + 1


def initialize_variables():
    flour_count = 0
    water_count = 0
    yeast_count = 0

    return flour_count, water_count, yeast_count
