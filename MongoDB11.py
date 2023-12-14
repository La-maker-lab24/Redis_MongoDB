# Изменение 1
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb://127.0.0.1")
db = client["Football"]
collectionG = db["Game"]
collectionT = db["Team"]
from tkinter import *
def apply(v):
    v = valueF.get()
    global listK
    global listO
    global valueO
    global txto
    global collectionG
    global collectionT
    del listO
    del listK
    global txtk
    global valueK
    listO=[]
    listK=[]
    if v=="collectionG":
        #listO = ['23.01.2023']
        normal = collectionG.find({}, projection=({"_id":1}))
        listK=["дата", "счёт",
               "забитые мячи.0.положение", "забитые мячи.0.минута", "забитые мячи.0.автор", "забитые мячи.0.передачи",
               "забитые мячи.1.положение", "забитые мячи.1.минута", "забитые мячи.1.автор", "забитые мячи.1.передачи",
               "забитые мячи.2.положение", "забитые мячи.2.минута", "забитые мячи.2.автор", "забитые мячи.2.передачи",
               "количество ударов по воротам.0.положение", "количество ударов по воротам.0.минута", "количество ударов по воротам.0.автор", "количество ударов по воротам.0.передачи",
               "пенальти.0.положение", "пенальти.0.минута", "пенальти.0.автор", "пенальти.0.передачи",
               "нарушения правил.0.жёлтые карточки", "нарушения правил.0.красные карточки", "нарушения правил.0.кому", "нарушения правил.0.минута", "нарушения правил.0.причина"
               ]
        for n in normal:
            listO.append(n["_id"])
        valueO.set(listO[0])
        valueK.set(listK[0])
        txto.destroy()
        txtk.destroy()
    if v=="collectionT":
        normal = collectionT.find({}, projection=({"_id":1}))
        listK=["дата", "счёт",
               "запасные игроки.0.ФИО", "запасные игроки.0.позиция",
               "состав игроков.0.ФИО", "состав игроков.0.позиция",
               "состав игроков.1.ФИО", "состав игроков.1.позиция",
               "ФИО тренера",
               "город",
               "название"
               ]
        for n in normal:
            listO.append(n["_id"])
        #listO = ["Разумихин"]
        valueO.set(listO[0])
        valueK.set(listK[0])
        txto.destroy()
        txtk.destroy()
    txtk = OptionMenu(window, valueK,*listK)
    txto = OptionMenu(window, valueO,*listO)
    txto.grid(row=3, column=1)
    txtk.grid(row=5, column=1)
        
def add():
    collect = valueF.get()
    doc = valueO.get()
    global db
    global client
    global collectionG
    global collectionT
    key = valueK.get()
    means = txt2.get()
    if collect=="collectionG":

        collectionG.update_one({"_id":ObjectId(doc)},{"$set":{key: means}})
    else:
        collectionT.update_one({"_id":ObjectId(doc)},{"$set":{key: means}})
        
def save():
    collect = valueF.get()
    global collectionG
    global collectionT
    key = valueK.get()
    means = txt2.get()
    if collect=="collectionG":
        collectionG.insert_one({key:means})
    else:
        collectionT.insert_one({key:means})
    means = txt2.delete(0, END)
    
    
def show():
    global collectionG
    global collectionT
    global text
    global scroll
    c = valueF.get()
    if c=="collectionG":
        c=collectionG
    else:
        c=collectionT
    text.destroy()
    text = Text(window)
    lis = c.find()
    for item in lis:
        for i in item:
            text.insert(END, str(i)+" "+str(item[i])+" "+"\n")
            text.insert(END, "")
        text.insert(END, "\n")
        text.insert(END, "\n")
    text.grid(row=10, rowspan=5, column=0, columnspan=3, sticky='NSEW')
    scroll.destroy()
    scroll = Scrollbar(window, orient=VERTICAL) 
    scroll.grid(row=10, rowspan=5, column=4, sticky=NS)
    text.config(yscrollcommand=scroll.set)
    scroll.config(command=text.yview)
        
window  = Tk()
window.geometry('840x650')
window.title("СУБД MongoDB")
window.resizable(width=False, height=False)
        
listOFF = ['collectionG', 'collectionT']
valueF = StringVar(window)
valueF.set('collectionG')
lbl1 = Label(window, text="Выберите коллекцию", font=20)
txt1 = OptionMenu(window, valueF,*listOFF, command=apply)
     
listO = ["выберите документ"]
valueO = StringVar(window)
valueO.set(listO[0])
lblo = Label(window, text="Выберите документ", font=20)
txto = OptionMenu(window, valueO,*listO)

listK = ["выберите ключ"]
valueK = StringVar(window)
valueK.set(listK[0])
lblk = Label(window, text="Выберите документ", font=20)
txtk = OptionMenu(window, valueK,*listK)

lbl2 = Label(window, text="Введите значение", font=20)
txt2 = Entry(window, width=90)

btn1 = Button(window, text="Добавить ключ-значение", command=add)
btn2 = Button(window, text="Сохранить документ", command=save)
btn3 = Button(window, text="Показать документы", command=show)

text = Text(window)
scroll = Scrollbar(window, orient=VERTICAL)

lbl1.grid(row=0, column=1)
txt1.grid(row=1, column=1)

lblo.grid(row=2, column=1)
txto.grid(row=3, column=1)

lblk.grid(row=4, column=1)
txtk.grid(row=5, column=1)

lbl2.grid(row=6, column=1)
txt2.grid(row=7, column=1)
lblq = Label(window, text="")
lblq.grid(row=8, column=1)
btn1.grid(row=9, column=0)
btn2.grid(row=9, column=1)
btn3.grid(row=9, column=2)
text.grid(row=10, column=0, columnspan=3, sticky='NSEW')

window.mainloop()



