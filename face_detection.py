import cv2
from cv2 import *
import argparse
import os.path

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, default="friends.jpg", help="the source material to work on")
    parser.add_argument("--type", type=int, default=1, help="source type, 1 for image, 2 for video")
    parser.add_argument("--webcam", action="store_true", default=False)
    return parser.parse_args()

def webcam_picture():
    # initialize the camera
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        namedWindow("cam-test")
        imshow("cam-test", img)
        # waitKey(0)
        destroyWindow("cam-test")
        imwrite("media\webcam_image.jpg", img) #save image

def face_detection_image(arglist):
    # Getting the model path
    my_path = os.path.abspath(os.path.dirname(__file__))
    model_path = os.path.join(my_path, 'models\haarcascade_frontalface_default.xml')
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(model_path)
    # Getting the image path
    if arglist.webcam:
        webcam_picture()
        source = "media\webcam_image.jpg"
    else:
        source = "media\\" + arglist.source
    img_path = os.path.join(my_path, source)
    # Read the input image
    img = cv2.imread(img_path)
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()

def face_detection_video(arglist):
    # Getting the model path
    my_path = os.path.abspath(os.path.dirname(__file__))
    model_path = os.path.join(my_path, 'models\haarcascade_frontalface_default.xml')
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(model_path)

    if arglist.webcam:
        # To capture video from webcam. 
        cap = cv2.VideoCapture(0)
    else:
        # To use a video file as input
        if arglist.source != "fancy.jpg":
            source = "media\\" + arglist.source
        else:
            source = "media\Faces from around the world.mp4"
        video_path = os.path.join(my_path, source)
        cap = cv2.VideoCapture(video_path)

    while True:
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    # Release the VideoCapture object
    cap.release()

if __name__ == '__main__':
    arglist = parse_args()
    if arglist.type == 1:
        face_detection_image(arglist)
    else:
        face_detection_video(arglist)