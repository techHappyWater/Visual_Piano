import cv2 

key_old=[1,1,1,1,1,1,1]
key_sta=[0,0,0,0,0,0,0]

Key_x_pos = [(120,200), (205, 285), (290, 370), (375, 455), (460, 540), (545, 625), (630, 710)]
Key_y_pos = [0, 250]

#画按键
#入口参数：背景图像
def draw_Key(img_input):
	cv2.rectangle(img_input, (Key_x_pos[0][0], Key_y_pos[0]), (Key_x_pos[0][1], Key_y_pos[1]), (255,255,255),2)
	cv2.rectangle(img_input, (Key_x_pos[1][0], Key_y_pos[0]), (Key_x_pos[1][1], Key_y_pos[1]), (255,255,255),2)
	cv2.rectangle(img_input, (Key_x_pos[2][0], Key_y_pos[0]), (Key_x_pos[2][1], Key_y_pos[1]), (255,255,255),2)
	cv2.rectangle(img_input, (Key_x_pos[3][0], Key_y_pos[0]), (Key_x_pos[3][1], Key_y_pos[1]), (255,255,255),2)
	cv2.rectangle(img_input, (Key_x_pos[4][0], Key_y_pos[0]), (Key_x_pos[4][1], Key_y_pos[1]), (255,255,255),2)
	cv2.rectangle(img_input, (Key_x_pos[5][0], Key_y_pos[0]), (Key_x_pos[5][1], Key_y_pos[1]), (255,255,255),2)
	cv2.rectangle(img_input, (Key_x_pos[6][0], Key_y_pos[0]), (Key_x_pos[6][1], Key_y_pos[1]), (255,255,255),2)

	return img_input


#按键按下时显示出来
def key_press_disp(key_now, img):
	for i in range(0,7):
		if key_now[i]:
			cv2.rectangle(img, (Key_x_pos[i][0], Key_y_pos[0]), (Key_x_pos[i][1], Key_y_pos[1]), (0,0,0),-1)
	return img

#画按键键值
#入口参数：背景图像
def draw_Key_num(img_input):
			#图片  左下角坐标  字体  字体大小  颜色  字体粗细
	cv2.putText(img_input,'1', (int((Key_x_pos[0][0]+Key_x_pos[0][1])/2),80),cv2.FONT_HERSHEY_COMPLEX,2,(255, 255, 0),1)
	cv2.putText(img_input,'2', (int((Key_x_pos[1][0]+Key_x_pos[1][1])/2),80),cv2.FONT_HERSHEY_COMPLEX,2,(255, 255, 0),1)
	cv2.putText(img_input,'3', (int((Key_x_pos[2][0]+Key_x_pos[2][1])/2),80),cv2.FONT_HERSHEY_COMPLEX,2,(255, 255, 0),1)
	cv2.putText(img_input,'4', (int((Key_x_pos[3][0]+Key_x_pos[3][1])/2),80),cv2.FONT_HERSHEY_COMPLEX,2,(255, 255, 0),1)
	cv2.putText(img_input,'5', (int((Key_x_pos[4][0]+Key_x_pos[4][1])/2),80),cv2.FONT_HERSHEY_COMPLEX,2,(255, 255, 0),1)
	cv2.putText(img_input,'6', (int((Key_x_pos[5][0]+Key_x_pos[5][1])/2),80),cv2.FONT_HERSHEY_COMPLEX,2,(255, 255, 0),1)
	cv2.putText(img_input,'7', (int((Key_x_pos[6][0]+Key_x_pos[6][1])/2),80),cv2.FONT_HERSHEY_COMPLEX,2,(255, 255, 0),1)

	return img_input


#判断按键是否按下
def Key_adjust(finger_dict, img):
	key_now=[0,0,0,0,0,0,0]
	for i in range(1,len(finger_dict)+1):
#		print(finger_dict[i][0], finger_dict[i][1])

		#判断指尖坐标是否位于琴键内
		if finger_dict[i][0] > Key_x_pos[0][0] and finger_dict[i][1] > Key_y_pos[0] and finger_dict[i][0] < Key_x_pos[0][1] and finger_dict[i][1] < Key_y_pos[1]:
			key_now[0]=1
		elif finger_dict[i][0] > Key_x_pos[1][0] and finger_dict[i][1] > Key_y_pos[0] and finger_dict[i][0] < Key_x_pos[1][1] and finger_dict[i][1] < Key_y_pos[1]:
			key_now[1]=1
		elif finger_dict[i][0] > Key_x_pos[2][0] and finger_dict[i][1] > Key_y_pos[0] and finger_dict[i][0] < Key_x_pos[2][1] and finger_dict[i][1] < Key_y_pos[1]:
			key_now[2]=1
		elif finger_dict[i][0] > Key_x_pos[3][0] and finger_dict[i][1] > Key_y_pos[0] and finger_dict[i][0] < Key_x_pos[3][1] and finger_dict[i][1] < Key_y_pos[1]:
			key_now[3]=1
		elif finger_dict[i][0] > Key_x_pos[4][0] and finger_dict[i][1] > Key_y_pos[0] and finger_dict[i][0] < Key_x_pos[4][1] and finger_dict[i][1] < Key_y_pos[1]:
			key_now[4]=1
		elif finger_dict[i][0] > Key_x_pos[5][0] and finger_dict[i][1] > Key_y_pos[0] and finger_dict[i][0] < Key_x_pos[5][1] and finger_dict[i][1] < Key_y_pos[1]:
			key_now[5]=1
		elif finger_dict[i][0] > Key_x_pos[6][0] and finger_dict[i][1] > Key_y_pos[0] and finger_dict[i][0] < Key_x_pos[6][1] and finger_dict[i][1] < Key_y_pos[1]:
			key_now[6]=1

	img = key_press_disp(key_now, img)	#实时绘制琴键状态
	img = draw_Key_num(img)				#最后绘制琴键键值

	#只有当目前按下并且上一次没按下，才将相应按键状态置为1
	for i in range(0,7):
		if key_old[i] == 0 and key_now[i] == 1:
			key_sta[i] = 1
		#更新按键历史记录
		key_old[i]=key_now[i]

	return img



