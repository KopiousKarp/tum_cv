import cv2
import numpy as np
from pyzbar.pyzbar import decode
import csv

import rospy
from geometry_msgs.msg import PoseStamped

x = 0
y = 0

def callback(data):
    global x, y
    x = data.pose.position.x
    y = data.pose.position.y

rospy.init_node('listener', anonymous=True)
rospy.Subscriber("/dwm1001/tag/T/position", PoseStamped, callback)

cap = cv2.VideoCapture(0)

# Create a CSV file to store the coordinates of each QR code detected
csv_file = open("qr_codes.csv", mode="wb")
csv_writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(["QR Code Value", "X", "Y"])

while not rospy.is_shutdown():
    _, frame = cap.read()
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        # Extract QR code value as a string
        data = obj.data.decode('utf-8')

        # Add the coordinates to the CSV file
        csv_writer.writerow([data, x, y])
        print(data)
    # Show the frame in a window
    #cv2.imshow("QR code scanner", frame)

    # Wait for the 'q' key to be pressed to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
#cv2.destroyAllWindows()

# Close the CSV file
csv_file.close()
