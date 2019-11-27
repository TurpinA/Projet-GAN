## image_cutter.py
# Importing required libraries
import os
from PIL import Image
import numpy as np

PATH_Images = 'DATA/Images/'
PATH_POSITION = 'DATA/Position/'
Path_SAVE = 'DATA/Images_Coupees/'

imageFilename = []
positionFilename = []

for filename in os.listdir(PATH_Images):
    imageFilename.append(os.path.join(PATH_Images, filename))
for filename in os.listdir(PATH_POSITION):
    positionFilename.append(os.path.join(PATH_POSITION, filename))

for i in range(len(imageFilename)):
    image = Image.open(imageFilename[i], "r")

    position = open(positionFilename[i], "r")
    line = position.readline()
    position.close()
    positionString = line.split("\t")

    left = int(positionString[1])
    top = int(positionString[0])
    right = int(positionString[3])
    bottom = int(positionString[2])

    newImage = image.crop((left, top, right, bottom))
    name = (imageFilename[i].split("/")[2]).split(".")[0]
    newImagePath = os.path.join(Path_SAVE, f"{name}_coupé.jpg")
    print(newImagePath)
    newImage.save(newImagePath)
