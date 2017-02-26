import math


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector(other * self.x, other * self.y, other * self.z)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (1 / other)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def components(self):
        return self.x, self.y, self.z


def normalise(a):
    return a / abs(a)


def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z


def cross(a, b):
    return Vector(a.y * b.z - b.y * a.z, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)


class Tile:
    def __init__(self, offset, pos, vx, vy):
        self.offset = offset
        self.pos = pos
        self.vx = vx
        self.vy = vy

    def getray(self, x, y):
        return self.pos + x * self.vx + y * self.vy

    def getpixel(self, x, y):
        return self.offset[0] + x * self.vx, self.offset[1] + y * self.vy
