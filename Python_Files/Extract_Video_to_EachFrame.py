# Onurcan Köken 20.03.2021
# References: https://gist.github.com/keithweaver/70df4922fec74ea87405b83840b45d57
#             https://www.reddit.com/r/Python/comments/c9dkuj/how_to_get_fps_of_a_video_file/
'''
Using OpenCV takes a mp4/mov/avi video and produces a number of images.
----
Open the Extract_Video_to_EachFrame.py and edit the path to the video. Then run:
$ python Extract_Video_to_EachFrame.py
'''
import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture("your own path")
# cap = cv2.VideoCapture('./Challange 2/AZURE Challenge 2.mov')
# cap = cv2.VideoCapture('AZURE Challenge 2.mov')

# Get Frame Per Second
fps = cap.get(cv2.CAP_PROP_FPS)
second = 0
sec = 0
print(fps)

ret = True

# create a directory to store each frame
try:
    if not os.path.exists('../DEU_ROV_Team_2021/azure/data'):
        os.makedirs('../DEU_ROV_Team_2021/azure/data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while ret:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Calculate each second for the current frame
    sec = currentFrame % fps
    if sec == 0:
        second += 1

    # there are 30 frames in each second, fps
    # i sampled 0., 10. and 20. frames in each 30 frame,
    # not all of it, so you can edit here as you wish
    if sec == 0 or sec == 10 or sec == 20:
        # Saves image of the current frame in jpg file
        name = './data/frame' + '_sec' + str(second) + '_' + str(currentFrame) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()