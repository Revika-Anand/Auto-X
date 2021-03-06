import mediapipe as mp
import numpy as np
import cv2
import time
from tkinter import messagebox
from register import *

# executes the code in file register.py
root = Tk()
obj = Register(root)
root.mainloop()

class extra:                   # imports required data from register.py
    def find(self):
        self.o = obj.coord
        return self.o
    def number(self):
        self.n = obj.number
        return self.n

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# video
cap = cv2.VideoCapture(0)

## capture image of patient for records
ret, frame = cap.read()
messagebox.showinfo("Important!", "Please stand still, an image will be taken in 5 seconds.")
time.sleep(5)
p_no = extra().number()
img_name = "{}.png".format(p_no)
cv2.imwrite(img_name, frame)

## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence = 0.75, min_tracking_confidence = 0.75) as pose:
    while cap.isOpened():
        ret, frame = cap.read()       

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
      
        # Make detection
        results = pose.process(image)
    
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            #print(landmarks)
        except:
            pass
                
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)               
        
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    coords = extra().find()    # contains the list of indexes of all required joints
    # print(coords)
    # for i in coords:
    #     print(landmarks[i])
    #     print(type(landmarks))
        #print(landmarks[i][3])
    # print(type(landmarks))
    # print(len(landmarks))
    

