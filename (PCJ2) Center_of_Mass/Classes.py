from numbers import Number

class Vec3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        ret = None
        if isinstance(other, Number):
            ret = Vec3(self.x*other, self.y*other, self.z*other)
        if isinstance(other, Vec3):
            ret = self.elemul(other).lnorm()
        return ret

    def __rmul__(self, other):
        return self*other

    def lnorm(self, l=1):
        if l == 1:
            return self.x+self.y+self.z

        return pow(pow(self.x, l) + pow(self.y, l) + pow(self.z, l),(1./l))

    def elemul(self, other):
        return Vec3(self.x*other.x, self.y*other.y, self.z*other.z)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"