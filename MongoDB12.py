from pymongo import MongoClient
from collections import Counter
client = MongoClient("mongodb://127.0.0.1")
db = client["Football"]
collectionG = db["Game"]
collectionT = db["Team"]
from tkinter import *
def show():
    global collectionG
    global collectionT
    global text
    global scroll
    c = valueF.get()
    key=txt.get()
    sym=txt2.get()
    digit=txt3.get()
    if c=="collectionG":
        c=collectionG
    else:
        c=collectionT
    phrase = True
    #lis = c.find({key:str(digit)})
    #lis = c.find({}, projection=({"_id":0, key:1}))
    text.destroy()
    text = Text(window)
    res =[]
    s=set()
    #if key.find(".")!="0":
    #    for item in lis:
    #        for i in item:
    #            for z in item[i]:
    #                for q in z:
    #                    res.append(z[q])
    #                    s.add(z[q])
    #else:
    #    for item in lis:
    #        for i in item:
    #            res.append(item[i])
    #            s.add(z[q])
    #ruse = c.aggregate([{"$group":{"_id":"$"+key.split('.')[0],"количество":{"$count":1}}}])
    resu = c.aggregate([{"$group":{"_id":"$"+key,"количество":{"$sum":1}}}])
    #for item in ruse:
    #    print(item["количество"])
    for item in resu:
        for i in item:
            crow = item[i]
            break
    for cr in crow:
        s.add(cr)
        res.append(cr)
    time=0
    times=dict()
    for spart in s:
        r=Counter(res)
        user = c.aggregate([{"$unwind":"$"+key.split(".")[0]},{"$group":{"_id":"$"+key, "count":{"$sum":1}}}])
        #user = c.aggregate([{"$project":{"count":{"$size":{"$match":{key:spart}}}}}])
        #user=c.aggregate([{"$unwind":key.split(".")[1]},{"$match":{key:spart}},{"$replaceRoot":{"newRoot":{"key":"$"+key}}}])
        #user=c.aggregate([{"$match":{key:spart}},{"$project":{"size":{"$size":"$"+key}}}])
        #user=c.aggregate([{"$unwind":"$"+key},{"$match":{key:spart}},{"$group":{"_id":"$"+key,"количество":{"$sum":1}}}])
        for item in user:
            times[spart]=item["count"]
        user.close()
        print(times)
        if sym==">":
            if r[spart] > int(digit):
                text.insert(END, spart+"\n")
                time+=times[spart]
                text.insert(END, "")
        elif sym=="<":
            if r[spart] < int(digit): 
                text.insert(END, spart+"\n")
                time+=times[spart]
                text.insert(END, "")
        elif sym=="<=":
            if r[spart] <= int(digit): 
                text.insert(END, spart+"\n")
                time+=times[spart]
                text.insert(END, "")
        elif sym==">":
            if r[spart] > int(digit): 
                text.insert(END, spart+"\n")
                time+=times[spart]
                text.insert(END, "")
        elif sym==">=":
            if r[spart] >= int(digit): 
                text.insert(END, spart+"\n")
                time+=times[spart]
                text.insert(END, "")
        else:
            if r[spart] == int(digit): 
                text.insert(END, spart+"\n")
                time+=times[spart]
                text.insert(END, "")
        text.insert(END, "\n")
        text.insert(END, "\n")
    text.insert(END, "Количество: "+str(time))
    text.grid(row=12, rowspan=5, column=0, columnspan=3, sticky='NSEW')
    scroll.destroy()
    scroll = Scrollbar(window, orient=VERTICAL) 
    scroll.grid(row=12, rowspan=3, column=4, sticky=NS)
    text.config(yscrollcommand=scroll.set)
    scroll.config(command=text.yview)
        
window  = Tk()
window.geometry('700x550')
window.title("СУБД MongoDB")
window.resizable(width=False, height=False)
        
listOFF = ['collectionG', 'collectionT']
valueF = StringVar(window)
valueF.set('collectionG')
lbl1 = Label(window, text="Выберите коллекцию", font=20)
txt1 = OptionMenu(window, valueF,*listOFF)
     

lbl = Label(window, text="Введите ключ", font=20)
txt = Entry(window, width=90)

lbl2 = Label(window, text="Знак сравнения", font=20)
txt2 = Entry(window, width=90)

lbl3 = Label(window, text="Числовое значение", font=20)
txt3 = Entry(window, width=90)

btn1 = Button(window, text="Поиск", command=show)

text = Text(window)
scroll = Scrollbar(window, orient=VERTICAL)

lbl1.grid(row=0, column=1)
txt1.grid(row=1, column=1)

#lblo.grid(row=2, column=1)
#txto.grid(row=3, column=1)

lbl.grid(row=4, column=1)
txt.grid(row=5, column=1)

lbl2.grid(row=6, column=1)
txt2.grid(row=7, column=1)

lbl3.grid(row=8, column=1)
txt3.grid(row=9, column=1)

btn1.grid(row=11, column=2)

lblq = Label(window, text="")
lblq.grid(row=10, column=1)

text.grid(row=12, column=0, columnspan=3, sticky='NSEW')

window.mainloop()



