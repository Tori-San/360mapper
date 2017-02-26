from image import *
from geometry import *
import sys
import math

if len(sys.argv) < 2:
    sys.exit(1)
else:
    filename = sys.argv[1]
    outputname = ".".join(filename.split(".")[:-1]) + "_cube.tiff"

sphereImg = Image()
sphereImg.read(filename)
tilesize = sphereImg.width // 4
cubeImg = Image(4 * tilesize, 3 * tilesize)
tiles = [
        Tile((tilesize, tilesize), Vector(-1, 1, -1), Vector(2, 0, 0), Vector(0, -2, 0)),       # front
        Tile((2 * tilesize, tilesize), Vector(1, 1, -1), Vector(0, 0, 2), Vector(0, -2, 0)),    # right
        Tile((0, tilesize), Vector(-1, 1, 1), Vector(0, 0, -2), Vector(0, -2, 0)),              # left
        Tile((3 * tilesize, tilesize), Vector(1, 1, 1), Vector(-2, 0, 0), Vector(0, -2, 0)),    # back
        Tile((tilesize, 0), Vector(-1, 1, 1), Vector(2, 0, 0), Vector(0, 0, -2)),               # top
        Tile((tilesize, 2 * tilesize), Vector(-1, -1, -1), Vector(2, 0, 0), Vector(0, 0, 2))    # bottom
        ]

progress = 0

for t in tiles:
    ou, ov = t.offset
    for u in range(tilesize):
        progress += 1
        print(5 * "\r" + "{:.2f}%".format(100 * progress / (len(tiles) * tilesize)), end='')
        for v in range(tilesize):
            x, y, z = normalise(t.getray(u / tilesize, v / tilesize)).components()

            phi = -math.atan2(x, z) % (2 * math.pi)
            theta = math.acos(y)

            cubeImg[u + ou, v + ov] = sphereImg.interpolate(
                    phi / (2 * math.pi),
                    theta / math.pi
                    )
print("")
cubeImg.write(outputname)
