import cv2

img = cv2.imread('./test2.jpg')

while True:
    cv2.imshow('Untitled',img)

    # If we've waited at least 1ms and we've pressed the Esc key
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()