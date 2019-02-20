# Tommys file for more stuff
# import m2_extra

class Bowl(object):
    def __init__(self):
        self.flour_count = 0
        self.water_count = 0
        self.yeast_count = 0

    def __repr__(self):
        return 'Bowl(flour={:}, water={:}, yeast={:})'.format(self.flour_count, self.water_count,
                                                              self.yeast_count)

    def add_to_the_bowl(self, color):
        if color is 'red':
            self.flour_count = self.flour_count + 1
        elif color is 'blue':
            self.water_count = self.water_count + 1
        elif color is 'black':
            self.yeast_count = self.yeast_count + 1

# def main(color, yeast_count, water_count, flour_count):
#     bowl = m2_extra.lets_get_this_bread(color, yeast_count, water_count, flour_count)
#     value = m2_extra.check_if_done(bowl)
#     return value
#
