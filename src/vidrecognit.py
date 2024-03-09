import cv2
import dlib
from deepface import DeepFace

# Load the pre-trained face detection model
face_detector = dlib.get_frontal_face_detector()

# Load the pre-trained facial landmark detection model
landmark_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

def detect_facial_expression(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    # Read video frames
    while True:
        ret, frame = cap.read()

        # If there are no more frames, break the loop
        if not ret:
            break

        # Detect faces in the frame
        faces = face_detector(frame)

        # Iterate over detected faces
        for face in faces:
            # Extract the facial ROI
            x, y, w, h = face.left(), face.top(), face.width(), face.height()
            facial_roi = frame[y:y+h, x:x+w]

            # Predict facial expression
            try:
                analysis = DeepFace.analyze(facial_roi, actions=['emotion'], enforce_detection=False)
                expression = analysis['dominant_emotion']

                # Print the predicted expression
                print(expression)
            except Exception as e:
                print("Error in emotion analysis:", e)

        # Display the frame
        cv2.imshow('Frame', frame)

        # Check if the user pressed the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Path to the video file
video_path = 'path_to_your_video_file.mp4'

# Call the function to detect facial expressions in the video
detect_facial_expression(video_path)
