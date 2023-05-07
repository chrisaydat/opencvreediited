# Import necessary libraries and modules
from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import os
import platform

# Define the eye aspect ratio (EAR) calculation function
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Function to play a sound file
def play_sound(sound_file):
    if platform.system() == 'Darwin':  # Check for macOS
        os.system(f'afplay {sound_file}')
    else:
        print("Unsupported platform for playing sounds.")

# Set the threshold for EAR and the number of continuous frames to trigger an alert
thresh = 0.25
frame_check = 20

# Initialize the face detector and facial landmark predictor from Dlib
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Define the start and end indices for the left and right eyes in the facial landmarks array
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

# Start the video capture using the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Initialize the flag counter and the drowsiness alert counter
flag = 0
drowsiness_alert_count = 0

# Continuously read frames from the video stream
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Resize the frame for faster processing
    frame = imutils.resize(frame, width=450)

    # Convert the frame to grayscale for facial detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    subjects = detect(gray, 0)

    # Iterate through the detected faces
    for subject in subjects:
        # Predict the facial landmarks for the current face
        shape = predict(gray, subject)

        # Convert the facial landmarks to a NumPy array
        shape = face_utils.shape_to_np(shape)

        # Extract the left and right eye landmarks
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        # Calculate the EAR for both eyes
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # Calculate the average EAR
        ear = (leftEAR + rightEAR) / 2.0

        # Draw the contours of the eyes on the frame
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # Check if the average EAR is below the threshold
        if ear < thresh:
            flag += 1
            print(flag)

            if flag >= frame_check:
                drowsiness_alert_count += 1
                if drowsiness_alert_count >= 5:
                
                    play_sound('alarm-no3-14864.mp3')
                    cv2.putText(frame, "PARK AND DO 5 MIN EXERCISES!", (10, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    play_sound('alarm-no3-14864.mp3')
                    cv2.putText(frame, "****************ALERT!****************", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(frame, "****************ALERT!****************", (10, 325),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                print("Drowsy")
        else:
            flag = 0

    # Display the frame with eye contours and potential alert messages
    cv2.imshow("Frame", frame)

    # Wait for a key press, if the user presses 'q', break the loop and exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
