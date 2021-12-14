import time
import cv2
import play
from finger_recognize import finger_detect
import gui_and_key_adjust
from gui_and_key_adjust import key_sta

#定义finger字典，存储指尖坐标信息
finger = {}

#初始化摄像头
cap=cv2.VideoCapture(0)
cap.set(3,800) #设置分辨率
cap.set(4,600)

#播放控制数组
play_buf = [0,0,0,0,0,0,0]

#img_path = "orignal.jpg"

while True:
#	img = cv2.imread(img_path)
	_,img=cap.read()
	img = cv2.resize(img,(800,600))
	
	#返回指尖坐标信息
	finger = finger_detect(img)
#	print(finger,len(finger))

	img = cv2.flip(img, 1)							#将摄像头采集的图像镜像   1：左右镜像   -1：上下镜像
	for i in range(1,len(finger)+1):				#画出指尖位置
		cv2.circle(img, finger[i], 4, [255, 0, 0], -1)
	img = gui_and_key_adjust.draw_Key(img)			#画琴键
	gui_and_key_adjust.Key_adjust(finger, img)		#检测按键是否有效，更新按键状态，并绘制琴键实时状态，绘制琴键键值


	print(key_sta)

	play.play_data(key_sta)

	for i in range(0,7):				#用后状态清零
		key_sta[i] = 0
	
	cv2.imshow('piano',img)				#显示最终结果图

	if cv2.waitKey(1) & 0xFF == ord('q'):  
		break

	






