# author:    PyShine
# website:   http://www.pyshine.com

# import the necessary packages
import pyshine as ps,cv2,imutils
import time
image = cv2.imread('lena.jpg')
image = imutils.resize(image,width=720)

text  =  'ID: '+str(123)
image = ps.putBText(image,text,text_offset_x=20,text_offset_y=20,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(1,1,1))
text = str(time.strftime("%H:%M %p"))
image = ps.putBText(image,text,text_offset_x=image.shape[1]-170,text_offset_y=20,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(1,1,1))

text  =  '6842'
image = ps.putBText(image,text,text_offset_x=80,text_offset_y=372,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))

text  =  "Lena Fors'en"
image = ps.putBText(image,text,text_offset_x=80,text_offset_y=425,vspace=20,hspace=10, font_scale=1.0,background_RGB=(20,210,4),text_RGB=(255,255,255))

text  =  'Status: '
image = ps.putBText(image,text,text_offset_x=image.shape[1]-130,text_offset_y=200,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))
text  =  'On time'
image = ps.putBText(image,text,text_offset_x=image.shape[1]-130,text_offset_y=242,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))


text  =  'Attendence: '
image = ps.putBText(image,text,text_offset_x=image.shape[1]-200,text_offset_y=394,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))
text  =  '96.2%      '
image = ps.putBText(image,text,text_offset_x=image.shape[1]-200,text_offset_y=436,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))

cv2.imshow('Output', image)
cv2.waitKey(0)
