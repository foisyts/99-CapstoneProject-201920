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
        if color is 'Red':
            self.flour_count = self.flour_count + 1
        elif color is 'Blue':
            self.water_count = self.water_count + 1
        elif color is 'Black':
            self.yeast_count = self.yeast_count + 1

    def check_if_done(self):
        if self.yeast_count == 1 and self.flour_count == 1 and self.water_count == 1:
            return 'bread'
        elif self.yeast_count == 0 and self.flour_count == 0 and self.water_count == 3:
            return 'water'
        elif self.yeast_count == 1 and self.flour_count == 2 and self.water_count == 0:
            return 'fake sugar'
        elif self.yeast_count > 3 or self.flour_count > 3 or self.water_count > 3:
            return 'failure'
        else:
            return False


class delegate_on_laptop(object):
    def get_bowl(self, bowl):
        value = bowl.check_if_done()
        print("Congrats! You've made", value)
