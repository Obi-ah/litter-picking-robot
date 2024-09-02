import cv2
import numpy as np

img = cv2.imread('image_0005.png')
def click_event(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked at:", (x, y))
        cv2.imwrite('saved_frame.jpg', img)
        # Add your custom logic here (e.g., draw a circle, print values)

# img = cv2.imread("image_0005.png")  # Replace with your image path

cv2.imshow("Image", img)
cv2.setMouseCallback("Image", click_event)

# print(f'Outisde: {x},{y}')

cv2.waitKey(0)
cv2.destroyAllWindows()