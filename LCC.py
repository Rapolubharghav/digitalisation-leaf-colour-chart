import cv2
import PIL
import numpy as np
import sys
import colorsys
list1=["colour-1.jpg","colour-2.jpg","colour-3.jpg","colour-4.jpg"]
riceimage=cv2.imread("ricecrop1.jpg")
image1 = cv2.cvtColor(riceimage, cv2.COLOR_RGB2HSV)

image= cv2.imread("colour-1.jpg")
images=np.array(image)
image1 = cv2.cvtColor(images, cv2.COLOR_RGB2HSV)

print(image1.shape)
np.set_printoptions(threshold=sys.maxsize)
red=np.average(image1[0:241,0:112,0])
green=np.average(image1[0:241,0:112,1])
blue=np.average(image1[0:241,0:112,2])
overall_average=np.average(image1[0:241,0:112,0:3])
#
print("Red Average",red)
print("green Average",green)
print("blue Average",blue)
print("overall average",overall_average)

