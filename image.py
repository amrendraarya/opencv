import cv2
import numpy as np
#reading the images
img=cv2.imread("pic2.jfif",-1)
# plot the images
cv2.imshow("image",img)
#window will not distroy itself (0) stands for it
cv2.waitKey(0)
# wriiting the images
cv2.imwrite("pic.jpg",img)

# if we wnt to destroy windows with esc key
cv2.destroyAllWindows()