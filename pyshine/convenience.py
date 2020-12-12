# author:    PyShine
# website:   http://www.pyshine.com

# import the necessary packages
import numpy as np
import cv2
import socket,time
import queue
import sounddevice as sd
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def putBText(img,text,text_offset_x=20,text_offset_y=20,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(1,1,1),font = cv2.FONT_HERSHEY_DUPLEX,thickness = 2,alpha=0.6,gamma=0):
	"""
    Inputs:
    img: cv2 image img
    text_offset_x, text_offset_x: X,Y location of text start
    vspace, hspace: Vertical and Horizontal space between text and box boundries
    font_scale: Font size
    background_RGB: Background R,G,B color
    text_RGB: Text R,G,B color
    font: Font Style e.g. cv2.FONT_HERSHEY_DUPLEX,cv2.FONT_HERSHEY_SIMPLEX,cv2.FONT_HERSHEY_PLAIN,cv2.FONT_HERSHEY_COMPLEX
          cv2.FONT_HERSHEY_TRIPLEX, etc
    thickness: Thickness of the text font
    alpha: Opacity 0~1 of the box around text
    gamma: 0 by default

    Output:
    img: CV2 image with text and background
	"""
	R,G,B = background_RGB[0],background_RGB[1],background_RGB[2]
	text_R,text_G,text_B = text_RGB[0],text_RGB[1],text_RGB[2]
	(text_width, text_height) = cv2.getTextSize(text, font, fontScale=font_scale, thickness=thickness)[0]
	x, y, w, h = text_offset_x, text_offset_y, text_width , text_height
	crop = img[y-vspace:y+h+vspace, x-hspace:x+w+hspace]
	white_rect = np.ones(crop.shape, dtype=np.uint8)
	b,g,r = cv2.split(white_rect)
	rect_changed = cv2.merge((B*b,G*g,R*r))


	res = cv2.addWeighted(crop, alpha, rect_changed, 1-alpha, gamma)
	img[y-vspace:y+vspace+h, x-hspace:x+w+hspace] = res

	cv2.putText(img, text, (x, (y+h)), font, fontScale=font_scale, color=(text_B,text_G,text_R ), thickness=thickness)
	return img


def audioCapture(mode='send'):

	frame = [0]
	audio = queue.Queue(maxsize=20)
	def getAudio():
		def callback(indata, outdata, frames, time, status):
			
			if status:
				print(status)

			if mode=='get':
				try:
					frame = audio.get()
					outdata[:] = frame
					
				except queue.Empty as e:
					pass
			else:
				audio.put(indata)
			
		with sd.Stream( channels=2,blocksize=1024, callback=callback):
			input()
			exit()
			
	thread = threading.Thread(target=getAudio, args=())
	thread.start()
	return audio


import matplotlib.pyplot as plt
import matplotlib.animation as animation


def showPlot(name,audio,xmin=0,ymin=-0.5,xmax=1024,ymax=0.5):
	
	# Get the Figure
	fig = plt.figure(figsize=(8,3))
	ax = fig.add_subplot(1,1,1)
	ax.set_facecolor((0,0,0)) 
	fig.tight_layout() 
	ax.yaxis.grid(True)


	def animate(i):
		
		try:
			ax.clear()
			ys = []
			ys = audio.get()
			
			T= ys.shape[0]
			ys = ys[0:T//1]
			X_m = ys
			ax.plot(X_m, '.', color = (0.25,1,0))
			ax.set_ylim( ymin=ymin, ymax=ymax)	
			ax.set_xlim( xmin=xmin, xmax=xmax)	
			ax.set_title(name)		
		except Exception as e:
			try:
				ax.set_ylim( ymin=ymin, ymax=ymax)	
				ax.set_xlim( xmin=xmin, xmax=xmax)	
				ax.set_title(name)		

			except:
				pass
			pass
			print(e)
			
	# Lets call the animation function 	
	ani = animation.FuncAnimation(fig, animate, interval=30)
	plt.ion()
	plt.show()
	plt.pause(0.001)




# TEXT examples
# Hershey Simplex
# Hershey Plain
# Hershey Duplex
# Hershey Complex
# Hershey Triplex
# Hershey Complex Small
# Hershey Script Simplex
# Hershey Script Complex
