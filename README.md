# pyshine
A collection of simply yet high level utilities for Python.

## Installation

### Installing dependencies

Provided the below python packages are installed, pyshine is completely pip installable.



### Installing pyshine

`pip install pyshine`

To upgrade to the newest version
`pip install --upgrade pyshine`


### pyshine.putBText()
putBText(): Put Background Box with Text
```
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
```
### usage
```python3
import pyshine as ps
import cv2
image = cv2.imread('lena.jpg')
text  =  'HELLO WORLD!'
image =  ps.putBText(image,text,text_offset_x=20,text_offset_y=20,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(1,1,1))
cv2.imshow('Output', image)
cv2.waitKey(0)
```
## License

© 2020 PyShine

This repository is licensed under the MIT license. See LICENSE for details.
