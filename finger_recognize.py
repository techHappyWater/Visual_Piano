import cv2
import numpy as np

def finger_detect(img_input):
	#定义字典，用于存放指尖坐标
	finger = {}
	img = cv2.flip(img_input, 1)			#图像镜像   1：左右镜像   -1：上下镜像
#	cv2.imshow('palm image',img)

	#图像处理：灰度转化、阈值分割（将手掌区域从原图像中抠出来）
	hsvim = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower = np.array([0, 48, 80], dtype = "uint8")
	upper = np.array([20, 255, 255], dtype = "uint8")
	skinRegionHSV = cv2.inRange(hsvim, lower, upper)
	blurred = cv2.blur(skinRegionHSV, (2,2))
	ret,thresh = cv2.threshold(blurred,0,255,cv2.THRESH_BINARY)
#	cv2.imshow("thresh", thresh)

	#手掌轮廓绘制
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = max(contours, key=lambda x: cv2.contourArea(x))
	cv2.drawContours(img, [contours], -1, (255,255,0), 2)
#	cv2.imshow("contours", img)

	#凸包检测
	hull = cv2.convexHull(contours)
	cv2.drawContours(img, [hull], -1, (0, 255, 255), 2)
#	cv2.imshow("hull", img)
#	print(hull)

	#手掌凸缺陷检测
	hull = cv2.convexHull(contours, returnPoints=False)
	defects = cv2.convexityDefects(contours, hull)
#	print(hull)

	#手指个数计数
	if defects is not None:
		cnt = 0
		for i in range(defects.shape[0]): # calculate the angle
			s, e, f, d = defects[i][0]
			start = tuple(contours[s][0])
			end = tuple(contours[e][0])
			far = tuple(contours[f][0])

			a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
			b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
			c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
			angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) # cosine theorem
			if angle <= np.pi / 2: # angle less than 90 degree, treat as fingers
				cnt += 1
				cv2.circle(img, far, 4, [0, 0, 255], -1)
				finger[cnt]=start
				cv2.circle(img, start, 4, [255, 0, 0], -1)

		if cnt > 0:
			cnt = cnt+1
			cv2.putText(img, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)
#			print(finger,len(finger))
			

#	cv2.imshow('final_result',img)

	return finger


