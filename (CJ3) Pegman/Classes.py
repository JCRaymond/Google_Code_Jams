class Bounds():

    def __init__(self, lower = None, upper = None):
        self.lower = lower
        self.upper = upper

    #Checks to see if val is greater than or equal to lower, and less than upper
    def check_val(self, val):
        if self.lower is not None and val < self.lower:
            return False
        if self.upper is not None and val >= self.upper:
            return False
        return True

class Pos:

    def __init__(self, x, y, x_bounds = None, y_bounds = None):
        self.x = x
        self.y = y
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds

    def __add__(self, other):
        if not isinstance(other, Pos):
            raise TypeError("You can only add type Pos to a Pos, not " + str(type(other)))

        return Pos(self.x+other.x, self.y+other.y)

    def __iadd__(self, other):
        if not isinstance(other, Pos):
            raise TypeError("You can only add type Pos to a Pos, not " + str(type(other)))

        self.x += other.x
        self.y += other.y

        return self

    def is_in_bounds(self):
        x_in_bounds = True
        if self.x_bounds is not None and not self.x_bounds.check_val(self.x):
            x_in_bounds = False
        y_in_bounds = True
        if self.y_bounds is not None and not self.y_bounds.check_val(self.y):
            y_in_bounds = False

        return x_in_bounds and y_in_bounds


class Dir(Pos):
    pass