import os
from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw

image = Image.open("S1_DSC09754.jpg").convert("RGBA")

xImage, yImage = image.size

draw = ImageDraw.Draw(image)
draw.rectangle(((1540, 143), (1292, 671)), fill=None, outline="red")
x = (1540 - 1292)/2 + 1292
y = (671 - 143)/2 + 143
draw.ellipse(((x-20,y-20),(x+20,y+20)),fill="red")
image.show()