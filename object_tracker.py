from centroidtracker import CentroidTracker
from imutils.video import VideoStream

import numpy as np
import argparse
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True, help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True, help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

ct = CentroidTracker()
(H, w) = (None, None)

print("[INFO]  Loading model ...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

print("[INFO] Starting video stream ....")
vs = VideoStream(src=0).start()
time.sleep(2.0)

while True:

    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    if W in None or H is None:

        (H, W) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 1.0, (W,H)), (104.0,177.0,123.0)
    net.setInput(blob)
    detections = net.foward()
    rects = []

    for i in range(0, detections.shape[2]):

        if detections[0,0,i,2] > args["confidence"]:

            box = detections[0,0,i,3:7] * np.array([W, H, W, H])
            rects.append(box.astype("int"))

            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0,255,0), 2)

    objects = ct.update(rects)

    for (objecID, centroid) in objects.items():

        text = "ID {}".format(objecID)
        cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        cv2.circle(frame, (centroid[0], centroid[1]), 4, (0,255,0), -1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()