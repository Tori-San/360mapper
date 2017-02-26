from PIL import Image as Pimg
from lerp import lerp2d

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        return Color(self.r * other, self.g * other, self.b * other)

    def __rmul__(self, other):
        return self * other

    def getrgb(self):
        return int(0xFF * self.r), int(0xFF * self.g), int(0xFF * self.b)


def rgbcolor(r, g, b):
    return Color(r / 255, g / 255, b / 255)


def clamp(c):
    (r, g, b) = tuple(map(lambda ch: min(1, max(0, ch)), (c.r, c.g, c.b)))
    return Color(r, g, b)


class Image:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.data = [ 0 for _ in range(width * height) ]

    def read(self, filename):
        with Pimg.open(filename, "r") as im:
            self.width, self.height = im.size
            self.data = im.getdata()

    def write(self, filename):
        im = Pimg.new("RGB", (self.width, self.height))
        im.putdata(self.data)
        im.save(filename)

    def __getitem__(self, item):
        x, y = item
        x = min(self.width-1, max(0, x))
        y = min(self.height-1, max(0, y))
        (r, g, b) = self.data[self.width * y + x][:3]
        return rgbcolor(r, g, b)

    def __setitem__(self, key, value):
        x, y = key
        x = min(self.width-1, max(0, x))
        y = min(self.height-1, max(0, y))
        r, g, b = clamp(value).getrgb()
        self.data[self.width * y + x] = (r, g, b)

    def interpolate(self, u, v):
        x = u * self.width
        y = v * self.height
        a00 = self[int(x), int(y)]
        a10 = self[int(x) + 1, int(y)]
        a01 = self[int(x), int(y) + 1]
        a11 = self[int(x) + 1, int(y) + 1]
        return lerp2d(a00, a10, a01, a11, x - int(x), y - int(y))
