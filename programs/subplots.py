import cv2
import matplotlib.pyplot as plt 

img = cv2.imread('sandro.jpg')
height, width, channels = img.shape

fig, axs = plt.subplots(nrows=2, ncols=2)

axs[1,1] = plt.imshow(img)
plt.show()