import cv2 

cam = cv2.VideoCapture(0)
cv2.namedWindow("Find Contour")

while True:
	ret,frame = cam.read()
	cv2.imshow("Find Contour",frame)

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray = cv2.bilateralFilter(gray, 11, 17, 17)
	edged = cv2.Canny(gray,30,200)

	cv2.imshow("Edged",edged)

	k=cv2.waitKey(1)
	if k == 27:
		break

cam.release()
cv2.destroyAllWindows()