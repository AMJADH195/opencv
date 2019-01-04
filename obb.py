
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("C:\rono.jpg",1)
cv2.imshow("legend",img)
cv2.waitkey(0)
cv2.destroyAllWindows()
