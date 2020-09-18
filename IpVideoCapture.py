#Make Sure that you have OpenCv installed in your System

import cv2

video = cv2.VideoCapture('your ip adress')

while True:
	_,frame = video.read()
	cv2.imshow("live",frame)
	k = cv2.waitKey(1)
	if k == ord('q'):
		break

video.release()
cv2.destroyAllWindows()
