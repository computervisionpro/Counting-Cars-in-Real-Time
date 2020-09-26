import cv2
import numpy as np
import imutils
import argparse
from centroidtracker import CentroidTracker

# python cars_count.py -v test_video.mp4 -b ./FP32/vehicle-detection-adas-0002.bin -x ./FP32/vehicle-detection-adas-0002.xml

ap = argparse.ArgumentParser()
ap.add_argument('-v','--video', required=True,
        help='path to the video')
ap.add_argument("-b", "--weights", required=True,
	help="path to bin file")
ap.add_argument("-x", "--model", required=True,
	help="path to xml file")
args = vars(ap.parse_args())

#initiate tracker for maintaining unique identity
ct = CentroidTracker()
(H,W) = (None,None)


print("[INFO]: Loading model....")
net = cv2.dnn.readNet(args['model'], args['weights'])
cap = cv2.VideoCapture(args['video'])


while True:
    ret, frame = cap.read()

    if not ret:
        break
    blob = cv2.dnn.blobFromImage(frame, size=(672,384), ddepth=cv2.CV_8U)
    net.setInput(blob)
    detections = net.forward()

    rects=[]

    for detection in detections.reshape(-1,7):
        confidence = float(detection[2])
        startX = int(detection[3]*frame.shape[1])
        startY = int(detection[4]*frame.shape[0])
        endX = int(detection[5]*frame.shape[1])
        endY = int(detection[6]*frame.shape[0])

        

        if confidence>0.3:
            cv2.rectangle(frame,(startX,startY),(endX,endY), color=(255,0,0))

            # list containing detected cars
            rects.append((startX,startY,endX,endY))

    # update tracker
    objects = ct.update(rects)

    for (ID,centroid) in objects.items():
        text = "vehicle_{}".format(ID+1)
        cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.circle(frame, (centroid[0], centroid[1]), 2, (0, 255, 200), 1)
            
            

    txt='Estimated Vehicles spotted: {}'.format(ID+1)
    cv2.putText(frame, txt, (20,520),cv2.FONT_HERSHEY_COMPLEX,
            0.7,(100,255,200),2)
    cv2.imshow('cars',frame)

    key = cv2.waitKey(2)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

print()
print('Cars counted:', ID+1)

