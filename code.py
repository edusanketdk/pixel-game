import cv2 as cv
import numpy as np

img = cv.imread(r'image.jpg', 0)
h, w = img.shape[:2]
clr = True
col = [0, 255]

print(f"Image dimensions: {h} X {w}")
I, J = int(input("Enter height of pixel: ")), int(input("Enter width of pixel: "))
print("Processing...")

for i in range(h):
    for j in range(w):
        img[i][j] = col[clr]
        if j%J == 0: clr = not clr
    if i%I == 0: clr = not clr

print("Displaying the image")

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

print("Program finished!")