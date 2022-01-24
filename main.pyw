from tkinter import *
from random import *

root = Tk()
string1 = StringVar()
string2 = StringVar()
string3 = StringVar()
string4 = StringVar()
string5 = StringVar()
string6 = StringVar()
string7 = StringVar()

def main1click():
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.title("World Map")
    level = PhotoImage(file = "img/level1.png") #백그라운드 이미지 설정
    levelImage = Label(root, image = level) #백그라운드 이미지 변수 선언
    levelImage.place(x = -2, y = -2)
    levelB = PhotoImage(file="img/B.png")  # 버튼 이미지 설정
    levelBImage = Button(root, image=levelB, command = level1click)  # 버튼 이미지 변수 선언
    levelBImage.place(x=1050, y=600)  # 버튼 이미지 위치 설정
    root.mainloop()

def level1click():
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.title("Changyong Pacific")
    image = PhotoImage(file = "img/level1g.png")
    levelimage = Label(root, image = image)
    levelimage.place(x=-2, y=-2)
    textbox = Entry(root, width=8, textvariable=string1, font=("Consolas", 20))
    textbox.place(x = 165, y = 305)
    RB = PhotoImage(file="img/RB.png")  # 버튼 이미지 설정
    RBImage = Button(root, image=RB)  # 버튼 이미지 변수 선언
    RBImage.place(x=130, y=250)
    GB = PhotoImage(file="img/GB.png")  # 버튼 이미지 설정
    GBImage = Button(root, image=GB, command=level1correct)  # 버튼 이미지 변수 선언
    GBImage.place(x=130, y=300)
    root.mainloop()

def level1correct():
    UserNum = string1.get()
    if UserNum == "8948":
        main2click()
    else:
        gameover()

def main2click():
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.title("World Map")
    level = PhotoImage(file = "img/level2.png") #백그라운드 이미지 설정
    levelImage = Label(root, image = level) #백그라운드 이미지 변수 선언
    levelImage.place(x = -2, y = -2)
    levelB = PhotoImage(file="img/B.png")  # 버튼 이미지 설정
    levelBImage = Button(root, image=levelB, command=level2click)  # 버튼 이미지 변수 선언
    levelBImage.place(x=1050, y=600)  # 버튼 이미지 위치 설정
    root.mainloop()

def level2click():
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.title("State of Libya")
    image = PhotoImage(file="img/level2g.png")
    levelimage = Label(root, image=image)
    levelimage.place(x=-2, y=-2)
    textbox = Entry(root, width=20, textvariable=string2, font=("Consolas", 18))
    textbox.place(x=65, y=170)
    GB = PhotoImage(file="img/GB2.png")  # 버튼 이미지 설정
    GBImage = Button(root, image=GB, command=level2correct)  # 버튼 이미지 변수 선언
    GBImage.place(x=365, y=172)
    root.mainloop()

def level2correct():
    UserNum = string2.get()
    if UserNum == "365":
        main3click()
    else:
        gameover()

def main3click():
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.title("World Map")
    level = PhotoImage(file = "img/level3.png") #백그라운드 이미지 설정
    levelImage = Label(root, image = level) #백그라운드 이미지 변수 선언
    levelImage.place(x = -2, y = -2)
    levelB = PhotoImage(file="img/B.png")  # 버튼 이미지 설정
    levelBImage = Button(root, image=levelB, command=level3click)  # 버튼 이미지 변수 선언
    levelBImage.place(x=1050, y=600)  # 버튼 이미지 위치 설정
    root.mainloop()

def level3click():
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.title("Federal Republic of Somalia")
    image = PhotoImage(file="img/level3g.png")
    levelimage = Label(root, image=image)
    levelimage.place(x=-2, y=-2)
    textbox = Entry(root, width=10, textvariable=string2, font=("Consolas", 18))
    textbox.place(x=105, y=285)
    RB = PhotoImage(file="img/RB.png")  # 버튼 이미지 설정
    RBImage = Button(root, image=RB)  # 버튼 이미지 변수 선언
    RBImage.place(x=70, y=230)
    GB = PhotoImage(file="img/GB.png")  # 버튼 이미지 설정
    GBImage = Button(root, image=GB, command=level3correct)  # 버튼 이미지 변수 선언
    GBImage.place(x=70, y=280)
    root.mainloop()

def level3correct():
    UserNum = string3.get()
    if UserNum == "SOM":
        main4click()
    else:
        gameover()

def main4click():
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.title("World Map")
    level = PhotoImage(file = "img/level4.png") #백그라운드 이미지 설정
    levelImage = Label(root, image = level) #백그라운드 이미지 변수 선언
    levelImage.place(x = -2, y = -2)
    levelB = PhotoImage(file="img/B.png")  # 버튼 이미지 설정
    levelBImage = Button(root, image=levelB, command=level4click)  # 버튼 이미지 변수 선언
    levelBImage.place(x=1050, y=600)  # 버튼 이미지 위치 설정
    root.mainloop()

def level4click():
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.title("Republic of Yemen")
    image = PhotoImage(file="img/level4g.png")
    levelimage = Label(root, image=image)
    levelimage.place(x=-2, y=-2)
    textbox = Entry(root, width=20, textvariable=string2, font=("Consolas", 18))
    textbox.place(x=65, y=170)
    GB = PhotoImage(file="img/GB2.png")  # 버튼 이미지 설정
    GBImage = Button(root, image=GB, command=level4correct)  # 버튼 이미지 변수 선언
    GBImage.place(x=365, y=172)
    root.mainloop()

def level4correct():
    UserNum = string4.get()
    if UserNum == "235":
        main5click()
    else:
        gameover()

def main6click():
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.title("World Map")
    level = PhotoImage(file = "img/level6.png") #백그라운드 이미지 설정
    levelImage = Label(root, image = level) #백그라운드 이미지 변수 선언
    levelImage.place(x = -2, y = -2)
    levelB = PhotoImage(file="img/B.png")  # 버튼 이미지 설정
    levelBImage = Button(root, image=levelB, command=level6click)  # 버튼 이미지 변수 선언
    levelBImage.place(x=1050, y=600)  # 버튼 이미지 위치 설정
    root.mainloop()

def level6click():
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.title("Republic of Iraq")
    image = PhotoImage(file="img/level6g.png")
    levelimage = Label(root, image=image)
    levelimage.place(x=-2, y=-2)
    colorlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    shuffle(colorlist)
    for i in range(0, 14):
        if colorlist[i+1] == 1:
            CorrectB = PhotoImage(file="img/{}.png".format(colorlist[i+1]))
            CorrectBImage = Button(root, image=CorrectB, command=main7click)
            CorrectBImage.place(x = 12 + (i+1)*30, y = 295)
        else:
            colorlist[i] = PhotoImage(file="img/{}.png".format(colorlist[i+1]))  # 버튼 이미지 설정
            BImage = Button(root, image=colorlist[i], command=gameover)  # 버튼 이미지 변수 선언
            BImage.place(x=12 + (i+1)*30, y=295)

    root.mainloop()

def main5click():
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.title("World Map")
    level = PhotoImage(file = "img/level5.png") #백그라운드 이미지 설정
    levelImage = Label(root, image = level) #백그라운드 이미지 변수 선언
    levelImage.place(x = -2, y = -2)
    levelB = PhotoImage(file="img/B.png")  # 버튼 이미지 설정
    levelBImage = Button(root, image=levelB, command=level5click)  # 버튼 이미지 변수 선언
    levelBImage.place(x=1050, y=600)  # 버튼 이미지 위치 설정
    root.mainloop()

def level5click():
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.title("Syrian Arab Republic")
    image = PhotoImage(file="img/level5g.png")
    levelimage = Label(root, image=image)
    levelimage.place(x=-2, y=-2)
    textbox = Entry(root, width=20, textvariable=string2, font=("Consolas", 18), background=("black"))
    textbox.place(x=65, y=170)
    GB = PhotoImage(file="img/GB2.png")  # 버튼 이미지 설정
    GBImage = Button(root, image=GB, command=level5correct)  # 버튼 이미지 변수 선언
    GBImage.place(x=365, y=172)
    root.mainloop()

def level5correct():
    UserNum = string5.get()
    if UserNum == "15168489879845213849844561649l887784546512138":
        main6click()
    else:
        gameover()

def main7click():
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.title("World Map")
    level = PhotoImage(file = "img/level7.png") #백그라운드 이미지 설정
    levelImage = Label(root, image = level) #백그라운드 이미지 변수 선언
    levelImage.place(x = -2, y = -2)
    levelB = PhotoImage(file="img/B.png")  # 버튼 이미지 설정
    levelBImage = Button(root, image=levelB, command=level7click)  # 버튼 이미지 변수 선언
    levelBImage.place(x=1050, y=600)  # 버튼 이미지 위치 설정
    root.mainloop()

def level7click():
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)
    root.title("People's Republic of Jjang-Ggae")
    image = PhotoImage(file="img/level7g.png")
    levelimage = Label(root, image=image)
    levelimage.place(x=-2, y=-2)
    textbox = Entry(root, width=8, textvariable=string1, font=("Consolas", 20))
    textbox.place(x=165, y=305)
    RB = PhotoImage(file="img/RB.png")  # 버튼 이미지 설정
    RBImage = Button(root, image=RB)  # 버튼 이미지 변수 선언
    RBImage.place(x=130, y=250)
    GB = PhotoImage(file="img/GB.png")  # 버튼 이미지 설정
    GBImage = Button(root, image=GB, command=level7correct)  # 버튼 이미지 변수 선언
    GBImage.place(x=130, y=300)
    root.mainloop()

def level7correct():
    UserNum = string7.get()
    if UserNum == "2":
        gameover()
    else:
        peace()

def peace():
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    root.title("Clear")
    image = PhotoImage(file="img/peace.png")
    levelimage = Label(root, image=image)
    levelimage.place(x=-2, y=-2)

    root.mainloop()
def gameover():
    root.title("Bomb Over.")  # 타이틀 이름 설정
    root.minsize(width=1280, height=720)
    root.maxsize(width=1280, height=720)
    go = PhotoImage(file = "img/gameover.png")
    goimage = Label(root, image=go)
    goimage.place(x=-2, y = -2)
    root.mainloop()

for i in range(1, 6):
    print("System> DO NOT shut off this prompt.")
root.title("Made by dlacked") #타이틀 이름 설정
root.minsize(width=1280, height=720)
root.maxsize(width=1280, height=720)

mainBackgroundImage = PhotoImage(file = "img/main.png") #백그라운드 이미지 설정
mainImage = Label(root, image = mainBackgroundImage) #백그라운드 이미지 변수 선언
mainImage.place(x = -2, y = -2) #백그라운드 이미지 위치 설정

mainButtonImage = PhotoImage(file = "img/buttonimage1.png") #버튼 이미지 설정
mainButton = Button(root, image = mainButtonImage, command = main1click) #버튼 이미지 변수 선언
mainButton.place(x = 450, y = 400) #버튼 이미지 위치 설정

root.mainloop()
