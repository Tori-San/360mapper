from image import Image

img = Image()
img.read("test.tiff")
img[0, 0] = img[1, 1]
img.write("test_out.tiff")
