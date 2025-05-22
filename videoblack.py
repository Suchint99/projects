import cv2
import numpy as np

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Define range for black color in HSV
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 30])

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to detect black color
    mask = cv2.inRange(hsv_frame, lower_black, upper_black)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, mask, and result
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Black Color Mask", mask)
    cv2.imshow("Detected Black Areas", result)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

