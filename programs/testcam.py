import cv2

cap = cv2.VideoCapture(0)
cap.open(0)

for n in range(3):
	ret, o = cap.read()
	print(ret)
	if ret == False:
		continue
	print(o.shape)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
