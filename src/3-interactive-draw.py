import cv2
import numpy as np


# True while mouse button down, False while mouse button Up
is_drawing = False
dx = -1
dy = -1

def drawRectangle(event, x, y, flags, params):
    global dx, dy, is_drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        is_drawing = True
        dx, dy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing == True:
            cv2.rectangle(img, (dx, dy), (x, y), (0, 2555, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False
        cv2.rectangle(img, (dx, dy), (x, y), (0, 2555, 0), -1)


img = np.zeros((512, 512, 3))
cv2.namedWindow(winname="Image")
cv2.setMouseCallback('Image',drawRectangle)

while True:
    cv2.imshow('Image', img)

    # checks for ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break