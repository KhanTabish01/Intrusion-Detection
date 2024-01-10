import cv2
from cvzone.PoseModule import PoseDetector
import send

# Create a PoseDetector object.
detector = PoseDetector()

# Create a VideoCapture object to capture the video stream from the webcam.
cap = cv2.VideoCapture(0)

# Set the resolution of the video stream to 640x480 pixels.
cap.set(3, 1080)
cap.set(4, 720)

# Create an empty list to store the number of frames in which a human has been detected.
l = []

# Create a flag variable to indicate whether a human has been detected for more than 50 frames.
flag = True

while True:
    # Read a frame from the video stream.
    success, img = cap.read()

    # Use the PoseDetector object to detect humans in the frame.
    img = detector.findPose(img)

    # Get a list of image landmarks and bounding boxes for any humans detected in the frame.
    imlist, bbox = detector.findPosition(img)

    # If a human is detected, append a 1 to the l list.
    if len(imlist) > 0:
        print("Intrusion Detected")
        l.append(1)

    # If the length of the l list is greater than 50 and the flag variable is True, send an SMS notification.
    if len(l) > 1000 and flag:
        flag = False
        send.sendSms()

    # Display the frame in a window called "Output".
    cv2.imshow("Output", img)

    # Wait for a key press.
    q = cv2.waitKey(1)

    # If the key pressed is 'q', break out of the while loop.
    if q == ord('q'):
        break

# Destroy all windows and release the VideoCapture object.
cv2.destroyAllWindows()
cap.release()
