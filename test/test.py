import cv2

cam = cv2.VideoCapture(1)
cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    cv2.imshow("test",frame)

    FPS = cam.get(cv2.CAP_PROP_FPS)
    print(FPS)
    #cv2.putText(frame, FPS, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),3)

    k=cv2.waitKey(1)
    if k==27:
        break

cam.release()
cv2.destroyAllWindows()

