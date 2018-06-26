#!/usr/bin/python

import cv2
import numpy as np
face_data=cv2.CascadeClassifier('harrfile_facedetectiondata.xml')
cap=cv2.VideoCapture(0)
while True:
	status,frame=cap.read()
#convert into BnW image
	grayimage=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	faces=face_data.detectMultiScale(grayimage,1.15,5)
	for(x,y,z,w) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+z),(0,255,0),2)
		roi_gray=grayimage[y:y+z,x:x+w]
		roi_color=frame[y:y+z,x:x+w]

	cv2.imshow("camera1",frame)
	if cv2.waitKey(30) & 0xFF == ord ('q'):
		break

cap.release()
cv2.destroyAllWindows()


	
