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

progress = 0
for v in range(sphereImg.height):
    for u in range(sphereImg.width):
        progress += 1
        print(5 * "\r" + "{:.2f}%".format(100 * progress / (sphereImg.width * sphereImg.height)))
        phi = 2 * math.pi * u / sphereImg.width
        theta = math.pi * v / sphereImg.height

        y = math.cos(theta)
        x = math.sin(theta) * math.sin(phi)
        z = math.sin(theta) * math.cos(phi)

        # TODO determine which tile was hit

        sphereImg[u, v] = cubeImg.interpolate(hitX, hitY)

print("")
sphereImg.write(outputname)
