## image_cutter_V2.py
# Importing required libraries
import os
from PIL import Image
from PIL import ImageOps
import numpy as np

PATH_Images = 'DATA/Images/'
PATH_POSITION = 'DATA/Position/'
Path_SAVE = 'DATA/Images_Coupees_V2/'

# Découpage des images originales

imageFilename = []
positionFilename = []

for filename in os.listdir(PATH_Images):
    imageFilename.append(os.path.join(PATH_Images, filename))
for filename in os.listdir(PATH_POSITION):
    positionFilename.append(os.path.join(PATH_POSITION, filename))

print("Starting cutting and rotating...")

for i in range(len(imageFilename)):
    image = Image.open(imageFilename[i], "r")

    xImage, yImage = image.size

    position = open(positionFilename[i], "r")
    line = position.readline()
    NbLine = 0

    while line and line != "\n":
        positionString = line.split("\t")

        left = int(positionString[1]) - 20
        top = int(positionString[0]) - 20
        right = left + 256
        bottom = top + 256

        # On tourne les images
        for j in range(0, 36):
            test = (right - left) / 2 + left, (bottom - top) / 2 + top
            image_rotated = image.rotate(j * 10, center=test)
            newImage = image_rotated.crop((left, top, right, bottom))
            name = (imageFilename[i].split("/")[2]).split(".")[0]
            newImagePath = os.path.join(Path_SAVE, f"{name}({NbLine})_cutted_R{j * 10}.jpg")
            print(newImagePath)
            newImage.save(newImagePath)
        NbLine = NbLine + 1
        line = position.readline()

position.close()

print("Cutting finished")
print("")

# Inversion à la vertical des images

print("Starting inversion ...")

for filename in os.listdir(Path_SAVE):
    path = os.path.join(Path_SAVE, filename)
    image = ImageOps.mirror((Image.open(path)))
    newImagePath = os.path.join(Path_SAVE, filename.split(".")[0] + "_inversed.jpg")
    print(newImagePath)
    image.save(newImagePath)

print("Inversion finished")
print("")
