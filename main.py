# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import array
import statistics

import cv2
import numpy as np
import colorgram
import argparse
import sys
from PIL import Image, ImageDraw, ImageFont
def media(matriz):
  soma = 0
  tamanho = 0

  for linha in matriz:
    soma += sum(linha)
    tamanho += len(linha)
  return soma / tamanho
def get_colors(fatia2):
    hsv = cv2.cvtColor(fatia2, cv2.COLOR_BGR2HSV)
    b1, g1, r1 = cv2.split(fatia2)
    mb = media(b1)
    mg = media(g1)
    mr = media(r1)
    if((mb>180)or (mr>180)or(mg>180)):
        return "branco"
    else:
        return "marcado"



def verificar(xa,ya):
    fatia2 = imagem[xa:xa + 2000, ya+20:ya+800]
    cv2.imshow("aaaa", fatia2)
    print(xa,ya,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("letra A "+get_colors(fatia2))

    fatia2 = imagem[xa:xa + 10, ya+60:ya+80]
    #cv2.imshow("bb", fatia2)
    print("letra B "+get_colors(fatia2))
    fatia2 = imagem[xa:xa + 10, ya+80:ya+100]
    #cv2.imshow("cc", fatia2)
    print("letra C "+get_colors(fatia2))
    fatia2 = imagem[xa:xa + 10, ya+100:ya+120]
    #cv2.imshow("dd", fatia2)
    print("letra D "+get_colors(fatia2))


    pass
def verifica_coluna(xa,ya):


    # 10,105 cada questao
    # +20,+0  intervalo entre cada questao
    contador = 1
    lista_de_questoes = []
    lista_de_respostas = []
    while (xa < 760):
        print("questao ", contador, " ")
        fatia2 = imagem[xa:xa + 10, ya:yf]
        palavra = " " + str(xa) + str(xf) + " "
        xa = xa + 20
        lista_de_respostas.append(verificar(xa, ya))
        lista_de_questoes.append(xa)
        contador = contador + 1
        print("questao ", contador, " ")
        fatia2 = imagem[xa:xa + 10, ya:yf]
        palavra = " " + str(xa) + str(xf) + " "
        xa = xa + 19
        lista_de_respostas.append(verificar(xa, ya))
        lista_de_questoes.append(xa)
        contador = contador + 1
    print("questao ", contador, " ")
    fatia2 = imagem[xa:xa + 10, ya:yf]
    palavra = " " + str(xa) + str(xf) + " "
    xa = xa + 20
    lista_de_respostas.append(verificar(xa, ya))
    lista_de_questoes.append(xa)
    pass

xa=339
ya=40
xf=350
yf=160
imagem = cv2.imread("img_4.png")
fatia = imagem[xa:xf, ya:yf]
fatia2 = imagem[xa:xa + 10, ya:yf]
cv2.imshow("testet", imagem)
cv2.imshow("t", fatia2)
verifica_coluna(xa,ya)
fatia = imagem[xa:xf, 165:280]
cv2.imshow("teste", fatia)
fatia = imagem[xa:xf, 290:400]
cv2.imshow("test", fatia)
fatia = imagem[xa:xf, 410:525]
cv2.imshow("tes", fatia)
fatia = imagem[359:359 + 10, 40:525]
cv2.imshow("ts", fatia)
# fatia2 = imagem[xa:xa + 10, ya+60:ya+80]
cv2.waitKey(0)