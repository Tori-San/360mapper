from image import *
from geometry import *
import sys
import math

if len(sys.argv) < 2:
    sys.exit(1)
else:
    filename = sys.argv[1]
    outputname = ".".join(filename.split(".")[:-1]) + "_sphere.tiff"

cubeImg = Image()
cubeImg.read(filename)
tilesize = cubeImg.width // 4
sphereImg = Image(4 * tilesize, 2 * tilesize)

def mktile(u, v, su, sv):
    return Tile(((u + 0.5) * tilesize, (v + 0.5) * tilesize), None, su * tilesize / 2, sv * tilesize / 2)

tiles = {
        "top":      mktile(1, 0, 1, 1),
        "left":     mktile(0, 1, 1, 1),
        "front":    mktile(1, 1, 1, 1),
        "right":    mktile(2, 1, 1, 1),
        "back":     mktile(3, 1, 1, 1),
        "bottom":   mktile(1, 2, 1, 1)
        }

progress = 0
for v in range(sphereImg.height):
    for u in range(sphereImg.width):
        progress += 1
#        print(5 * "\r" + "{:.2f}%".format(100 * progress / (sphereImg.width * sphereImg.height)), end = '')
        phi = 2 * math.pi * u / sphereImg.width
        theta = math.pi * v / sphereImg.height

        y = math.cos(theta)
        x = math.sin(theta) * math.sin(phi)
        z = math.sin(theta) * math.cos(phi)

        absvals = (abs(x), abs(y), abs(z))
        if abs(x) == max(absvals):
            hit = "right" if x > 0 else "left"
            hu = z / abs(x)
            hv = y / abs(x)
        elif abs(y) == max(absvals):
            hit = "top" if y > 0 else "bottom"
            hu = x / abs(y)
            hv = z / abs(y)
        else:
            hit = "back" if z > 0 else "front"
            hu = x / abs(z)
            hv = y / abs(z)
        hu, hv = tiles[hit].getpixel(hu, hv)
        hu /= sphereImg.width
        hv /= sphereImg.height
        print("hit {} at ({}, {})".format(hit, hu, hv))
        sphereImg[u, v] = cubeImg.interpolate(hu, hv)

print("")
sphereImg.write(outputname)
