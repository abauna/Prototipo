# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import cv2
import qrcode
from tkinter import *
from PIL import Image



def gerar(dado):
    img=cv2.imread("FolhaRespostas.jpg")
    #dado="nome do aluno"
    cv2.putText(img,str(dado),(250,1560),cv2.FONT_HERSHEY_DUPLEX,1,255)
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
    img.save("final.jpg")
    cv2.waitKey(0)
    pass






def aoClicar():
    dado=entrada.get()
    mensagem["text"]=dado
    print(dado)
    gerar(str(dado))
    pass
window = Tk()
window.geometry("300x200+200+100")
window.title("gerador de cartao ")
mensagem = Label(window, text="coloque o nome do aluno", font="impact 20 bold")
mensagem.pack()
entrada = Entry(window, font="arial 15 bold")
entrada.pack()

botao = Button(window, text="gerar", command=aoClicar)
botao.pack()
window.mainloop()