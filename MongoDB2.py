from pymongo import MongoClient
client = MongoClient("mongodb://127.0.0.1")
db = client["shop"]
collection = db["product"]

print("Список названий товаров из заданной категории\n")
category = input("продукты, посуда, одежда или техника: ")
print("")
names = collection.find({"категория":category}, projection=({"_id":0, "наименование товара":1}))
for item in names:
    print(item["наименование товара"])
names.close()
print("")
print("")
print("")
print("Список характеристик\n")
char = collection.find({"категория":category}, projection=({"_id":0, "наименование товара":1, "характеристики":1}))
for item in char:
    print(item["наименование товара"], " ", item["характеристики"])
char.close()
print("")
person = input("Сергей, Елизавета, Мария, Иван, Александра, Евгения, Евгений, Александр, Надежда, Ксения, Ульяна, Ольга, Костя, Михаил: ")
print("")
print("")
print("")
print("Список названий и стоимостей товаров, которые купил определённый человек\n")
nameprice = collection.find({"о покупателе.Имя":person}, projection=({"_id":0, "наименование товара":1, "цена":1}))
for item in nameprice:
    print(item["наименование товара"], " ", item["цена"])
nameprice.close()
print("")
color = input("бежевый, белый, синий, красный, зелёный, чёрный, серый: ")
print("")
print("")
print("")
print("Список названий товаров, проивзодителей и цен (цвет)")
print("")
namespp = collection.find({"характеристики.цвет":color}, projection=({"_id":0, "наименование товара":1, "производитель":1, "цена":1}))
for item in namespp:
    print(item["наименование товара"], " ",item["производитель"], " ", item["цена"])
namespp.close()

s=0
po =[]
print("")
print("")
print("")
print("Общая сумма")
print("")
products=["пшёная крупа", "рис", "овсяная крупа", "пшено", "чашка", "тарелка", "чайный сервиз", "Набор ложек", "Стакан", "футболка", "рубашка", "кепка", "шапка", "кеды", "наушники", "клавиатура", "компьютерная мышь", "монитор", "ноутбук", "гречневая крупа"]
for p in products:
    summ = collection.find({"наименование товара":p}, projection=({"_id":0, "цена":1}))
    for item in summ:
        c = int(item["цена"])
    summ.close()
    summ1 = collection.aggregate([{"$match":{"наименование товара":p}},{"$project":{"size":{"$size":"$о покупателе"}}}])
    for item in summ1:
        pr = item["size"]
    summ1.close()
    s+=int(pr)*int(c)
print(s)
print("")
print("")
print("")
print("Количество товаров в каждой категории")
print("")
dig = collection.aggregate([{"$group":{"_id":"$категория","количество товаров":{"$sum":1}}}])
for item in dig:
    print(item)
dig.close()
print("")
print("")
print("")
print("Список имён покупателей заданного товара")
print("")
product1 = input("пшёная крупа, рис, овсяная крупа, пшено, чашка, тарелка, чайный сервиз, Набор ложек, Стакан, футболка, рубашка, кепка, шапка, кеды, наушники, клавиатура, компьютерная мышь, монитор, ноутбук, гречневая крупа ")

listnames = collection.find({"наименование товара":product1}, projection=({"_id":0, "о покупателе.Имя":1}))
for item in listnames:
    print(item)
listnames.close()
print("")
print("")
print("")
print("Список имён покупателей заданного товара с доставкой фирмы с заданным названием")
print("")
firm = input("Перекрёсток, Сигма, Магнит, МВидео ")
namefirm = collection.aggregate([{"$match":{"наименование товара":product1}},{"$unwind":"$о покупателе"},{"$match":{"о покупателе.Служба доставки":firm}},{"$replaceRoot":{"newRoot":{"имя":"$о покупателе.Имя"}}}])
for item in namefirm:
    print(item)
namefirm.close()

client.close()
