import cv2
import numpy as np

# Load the image
image = cv2.imread("image.jpeg")

# Convert the image to HSV color space (for better color range detection)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range for black color in HSV
# These values may need adjustment based on lighting or specific needs
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])

# Create a mask for black color
mask = cv2.inRange(hsv_image, lower_black, upper_black)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=mask)

# Display the original image, mask, and result
cv2.imshow("Original Image", image)
cv2.imshow("Black Color Mask", mask)
cv2.imshow("Detected Black Areas", result)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()

