from PIL import Image as Pimg


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class Image:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.data = None

    def read(self, filename):
        im = Pimg.open(filename, "r")
        self.width, self.height = im.size
        self.data = im

    def write(self, filenamme):
        self.data.save(filenamme)

    def __getitem__(self, item):
        (r, g, b) = self.data.getpixel(item)
        return Color(r, g, b)

    def __setitem__(self, key, value):
        self.data.putpixel(key, (value.r, value.g, value.b))
