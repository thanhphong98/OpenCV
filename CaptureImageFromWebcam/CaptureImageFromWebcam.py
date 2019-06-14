import cv2
import os

buttonCapture= 32
buttonStop = 27

outputPath = 'Output'

cam = cv2.VideoCapture(1)
cv2.namedWindow("CaptureImageFromWebcam")

img_counter=606

while True:
	ret, frame = cam.read()
	cv2.imshow("CaptureImageFromWebcam", frame)

	k = cv2.waitKey(1)

	if k == buttonStop:
		print("Stop...")
		break
	elif k == buttonCapture:
		img_name = "Rubik_{}.jpg".format(img_counter)
		cv2.imwrite(os.path.join(outputPath,img_name),frame)
		print("Saved {}".format(img_name))
		img_counter += 1

cam.release()
cv2.destroyAllWindows()
