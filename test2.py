import numpy as np
import pandas as pd
# import cv2 as cv
from cv2 import cv2
# from google.colab.patches import cv2_imshow # for image display
from skimage import io
from PIL import Image
import matplotlib.pylab as plt
import copy


image = io.imread("riceimage.jpg")
image_2 = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
center_find = copy.deepcopy(image_2)
# final_frame = cv2.hconcat((image, image_2))
hueavg = 0
satavg = 0
brightavg = 0
no_of_green = 0

for i,image in enumerate(image_2):
    for j,img in enumerate(image):
        flag = False
        if 35<img[0]<100:
            if img[1]>60:
                if img[2]>35:
                    hueavg += img[0]
                    satavg += img[1]
                    brightavg += img[2]
                    no_of_green += 1
                    center_find[i][j][0] = 255
                    center_find[i][j][1] = 255
                    center_find[i][j][2] = 255
                else:
                    flag = True
            else:
                flag = True
        else:
            flag = True
        if flag:
            center_find[i][j][0] = 0
            center_find[i][j][1] = 0
            center_find[i][j][2] = 0

# cv2.imshow('Original image',image)
# cv2.waitKey(0)
cv2.imshow('HSV image',image_2)
cv2.waitKey(0)
cv2.imshow('center find',center_find)
cv2.waitKey(0)
print(center_find)
print("Hue avg : ",hueavg/no_of_green)
print("Sat avg : ",satavg/no_of_green)
print("Brght avg : ",brightavg/no_of_green)