import cv2
import numpy as np
from pyzbar.pyzbar import decode
import time

cap = cv2.VideoCapture(0)

# Set a variable to store the time when the last QR code was detected
last_detection_time = time.time()

while True:
    _, frame = cap.read()
    decoded_objects = decode(frame)
    
    for obj in decoded_objects:
        # Extract QR code value as a string
        data = obj.data.decode('utf-8')
        
        # Check if it's been at least 3 seconds since the last QR code was detected
        if time.time() - last_detection_time >= 3:
            print("Found QR code with value:", data)
            
            # Update the last detection time
            last_detection_time = time.time()
    
    # Show the frame in a window
    cv2.imshow("QR code scanner", frame)
    
    # Wait for the 'q' key to be pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

