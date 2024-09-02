import numpy as np
import cv2

# Load the image
image_path = 'Assets/DatasetGenerator/Dataset/test/image_0309.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# print(image.shape)


cv2.imwrite('testinggg.png', image)

# Parameters
max_distance = 30  # Maximum distance represented in the image

# Coordinates of the dot (replace these with the actual coordinates)
dot_x = 125  # Example X coordinate
dot_y = 192  # Example Y coordinate

# Get the dimensions of the image
height, width = image.shape

origin_y = height - 1  # y-coordinate of the vertex (bottom of the image)

# Calculate the distance as a proportion of the total height
distance = (origin_y - dot_y) / height * max_distance

print(f"The calculated distance of the dot is: {distance:.2f} units")
