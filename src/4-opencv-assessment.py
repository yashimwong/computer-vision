import cv2
import numpy as np

# Task: Create scripts that open the dog picture and allow 
# you to draw empty circles whenever you click the right mouse
# button down.

def drawCircle(event, x, y, flags, params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=50, color=(255, 0, 0), thickness=-1)

    


window_name = 'Task Circles'
img = cv2.imread('dog_backpack.jpg')
cv2.namedWindow(winname = window_name)
cv2.setMouseCallback(window_name, drawCircle)

while True:
    cv2.imshow(window_name, img)

    # checks for ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break