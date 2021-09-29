# loops over all pixels, calls rendererLIB to generate the pixel color from its coordinates, then saves the image

import cv2
import numpy as np
import rendererLIB as lib
from tqdm import tqdm
from glob import glob

images = glob("results/*.png")
images = [int(images[im].split("\\")[1].split(".")[0]) for im in range(len(images))]
picName = max(images) + 1

coef = 1
resolution = (80*coef,45*coef,3)
img = np.zeros((resolution[1],
                resolution[0],
                resolution[2]))

for y in tqdm(range(len(img))):
    for x in range(len(img[y])):
        img[y][x] = lib.ImageGen(x,resolution[1]-y,resolution)  # calling lib to generate pixel color from pixel coordinates

img *= 255
img = cv2.resize(img,(800,450))

cv2.imwrite("results/"+str(picName)+".png",img)
