# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import array
import statistics

import cv2
import numpy as np
import colorgram
from PIL import Image
import argparse
import sys
from PIL import Image, ImageDraw, ImageFont
import qrcode

#img=np.zeros((320,600),dtype=np.uint8)
img=cv2.imread("FolhaRespostas.jpg")
#img=imag[100:150,100:250]
dado="nome do aluno"
cv2.putText(img,dado,(250,1560),cv2.FONT_HERSHEY_DUPLEX,1,255)

#img[225:100, 1525:1651] = (255, 0,0)
#cv2.imshow("janela",img)
cv2.imwrite("fonte_opencv.jpg",img)
qr = qrcode.QRCode(version = 1,
                   box_size = 5,
                   border = 5)
qr.add_data(dado)
imag = qr.make_image(fill_color = 'black',
                    back_color = 'white')
imag.save('qr.jpg')

img = Image.open(r"fonte_opencv.jpg")
imag = Image.open(r"qr.jpg")
img.paste(imag, (90,1525))
#imag.show()
img.show()
img.save("final.jpg")
cv2.waitKey(0)
