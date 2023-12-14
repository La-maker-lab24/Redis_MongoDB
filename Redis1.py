import redis
from tkinter import *
client = redis.Redis(host='localhost', port=6379, db=0)
def settings():
    userName = valueInside.get()
    text1 = txt5.get()
    font = valueF.get()
    font += ";"
    font += "{}".format(txt2.get())
    font += ";"
    fontColor = valueColor.get()
    font += valueFont.get()
    client.set(userName, "{},{}".format(font, fontColor))
    info = client.get(userName).decode().split(",")
    info1 = info[0].split(";")
    txt15.config(text=text1, font=(info1[0],info1[1],info1[2]), fg=info[1])
def apply(userName):
    userName = valueInside.get()
    if client.exists(userName):
        text1 = txt5.get()
        info = client.get(userName).decode().split(",")
        info1 = info[0].split(";")
        txt15.config(text=text1, font=(info1[0], info1[1], info1[2]), fg=info[1])        
        
window  = Tk()
window.geometry('700x500')
window.title("СУБД Redis")
window.resizable(width=False, height=False)

f_top = Frame(window)
f_bot = Frame(window)

listOfUsers = ['user1', 'user2', 'user3']
valueInside = StringVar(f_top)
valueInside.set('user1')
lbl = Label(f_top, text="Введите ваше имя", font=20)
txt = OptionMenu(f_top, valueInside, *listOfUsers, command=apply)

listOFF = ['Times New Roman', 'Calibri Light', 'STXingkai', 'Comic Sans MS', 'Arial Black']
valueF = StringVar(f_top)
valueF.set('Times New Roman')
lbl1 = Label(f_top, text="Выберите название шрифта", font=20)
txt1 = OptionMenu(f_top, valueF,*listOFF)

lbl2 = Label(f_top, text="Введите размер шрифта", font=20)
txt2 = Entry(f_top, width=90)

listOfColors = ['black', 'red', 'blue', 'green', 'yellow']
valueColor = StringVar(f_top)
valueColor.set('black')
lbl3 = Label(f_top, text="Выберите цвет шрифта", font=20)
txt3 = OptionMenu(f_top, valueColor, *listOfColors)

listOfFonts = ['normal', 'bold', 'italic', 'overstrike']
valueFont = StringVar(f_top)
valueFont.set('normal')
lbl4 = Label(f_top, text="Выберите начертание шрифта", font=20)
txt4 = OptionMenu(f_top, valueFont, *listOfFonts)

lbl5 = Label(f_top, text="Введите текст", font=20)
txt5 = Entry(f_top, width=90)

txt15 = Label(f_top, text='')

btn = Button(f_top, text="Сохранить", command=settings)

f_top.pack(side=LEFT, ipadx=10, ipady = 100)
lbl.pack(side=TOP)
txt.pack(side=TOP)

lbl1.pack(side=TOP)
txt1.pack(side=TOP)

lbl2.pack(side=TOP)
txt2.pack(side=TOP)

lbl3.pack(side=TOP)
txt3.pack(side=TOP)

lbl4.pack(side=TOP)
txt4.pack(side=TOP)

lbl5.pack(side=TOP)
txt5.pack(side=TOP)
txt15.pack(side=TOP)

btn.pack(side=LEFT, padx=20)

window.mainloop()



