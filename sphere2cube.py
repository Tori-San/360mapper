from image import *
from geometry import *
import sys

if len(sys.argv) < 2:
    sys.exit(1)
else:
    filename = sys.argv[1]
    outputname = ".".join(filename.split(".")[:-1]) + "_out.tiff"

sphereImg = Image()
sphereImg.read(filename)
tilesize = sphereImg.width // 4
cubeImg = Image(4 * tilesize, 3 * tilesize)
tiles = [
    Tile((tilesize, tilesize), Vector(-1, 1, -1), Vector(2, 0, 0), Vector(0, -2, 0)),       # front
    Tile((2 * tilesize, tilesize), Vector(1, 1, -1), Vector(0, 0, 2), Vector(0, -2, 0)),    # right
    Tile((0, tilesize), Vector(-1, 1, 1), Vector(0, 0, -2), Vector(0, -2, 0)),             # left
    Tile((3 * tilesize, tilesize), Vector(1, 1, 1), Vector(-2, 0, 0), Vector(0, -2, 0)),    # back
    Tile((tilesize, 0), Vector(-1, 1, 1), Vector(2, 0, 0), Vector(0, 0, -2)),               # top
    Tile((tilesize, 2 * tilesize), Vector(-1, -1, -1), Vector(2, 0, 0), Vector(0, 0, 2))    # bottom
]

for t in tiles:
    ou, ov = t.offset
    for u in range(tilesize):
        for v in range(tilesize):
            x, y, z = normalise(t.getray(u / tilesize, v / tilesize)).components()
            zenithAngle = math.acos(-y)
            equatorialAngle = math.acos(x)
            if z > 0:
                equatorialAngle = 2 * math.pi - equatorialAngle
            cubeImg[u + ou, v + ov] = sphereImg.interpolate(
                equatorialAngle / (2 * math.pi),
                zenithAngle / math.pi
            )

cubeImg.write(outputname)
