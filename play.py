import time
import threading
from playsound import playsound

def play_data(buf_input):
	for i in range(0,7):
		if buf_input[i]:
#			print(i+1)
			path="./钢琴7键音/"+str(i+1)+".wav"
			threading.Thread(target=playsound,args=(path,)).start()
#		time.sleep(0.03)

	length = len(threading.enumerate())
	print('当前运行的线程数为：%d'%length)

