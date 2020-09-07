import cv2
import numpy
import sys

caption = ''
if len(sys.argv) > 1:
	caption = sys.argv[1]

cap = cv2.VideoCapture(0)
save_frame = None
font = cv2.FONT_HERSHEY_DUPLEX

while True:
	ret, o = cap.read()
	if ret == False:
		continue
	f = cv2.cvtColor(o, cv2.COLOR_RGB2GRAY)
	f = cv2.Canny(f, 100,200)
	cv2.imshow('capture', f)
	key = chr(cv2.waitKey(1) & 0xFF)
	if key == 'q':
		break
	elif key == 'c':
		f = cv2.cvtColor(f, cv2.COLOR_GRAY2RGB)
		o = cv2.GaussianBlur(o, (51, 51), 0)
		save_frame = cv2.add(f, o // 3 * 2)
		if len(caption) > 0:
			width, _ = cv2.getTextSize(caption, font, 1, 2)
			offset = (640 - width[0]) // 2
			cv2.putText(save_frame, caption, (offset, 50), font, 1, (255,255,255), 2)
		cv2.imwrite('saveimg.jpg', save_frame)
		break

cap.release()
cv2.destroyAllWindows()
