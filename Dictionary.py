d = {   "Абельсон, Гарольд": "Creative Commons",
        "Айверсон, Кеннет": "APL",
        "Ахо, Альфред":"AWK",
        "Ашкенас, Джереми":"CoffeeScript",
        "Борн, Стивен": "Bourne shell",
        "Брайт, Уолтер": "D",
        "Ван Россум, Гвидо": "Python",
        "Вирт, Никлаус": "Pascal",
        "Вудс, Дон": "INTERCAL",
        "Гослинг, Джеймс":"Java",
      }

A = ['Абельсон, Гарольд','Айверсон, Кеннет','Ашкенас, Джереми','Борн, Стивен','Брайт, Уолтер','Ван Россум, Гвидо','Вирт, Никлаус','Вудс, Дон','Гослинг, Джеймс']

def seach(X):
    for i in range (0,9):
        for j in range(0,len(X)):
            while j < len(X):
                if A[i][j] == X[j]:
                    j+=1
                else:
                    j=0
                    i+=1
        print(d[A[i]])
        break

def ssort():
    print("Абельсон, Гарольд",
        "Айверсон, Кеннет",
        "Ахо, Альфред",
        "Ашкенас, Джереми",
        "Борн, Стивен",
        "Брайт, Уолтер",
        "Ван Россум, Гвидо",
        "Вирт, Никлаус",
        "Вудс, Дон",
        "Гослинг, Джеймс",)



print("Выберете операцию:0-поиск , 1-сортировка")
i = int(input())
if i ==0:
    print("Введите имя")
    c = str(input())
    seach(c)
else:
    print("Абельсон, Гарольд;","Айверсон, Кеннет;","Ахо, Альфред;","Ашкенас, Джереми;","Борн, Стивен;","Брайт, Уолтер;","Ван Россум, Гвидо;","Вирт, Никлаус;","Вудс, Дон;","Гослинг, Джеймс")