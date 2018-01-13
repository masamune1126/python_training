#分岐
a = 5
if a == 5:
    print("Hello!")
else:
    print("Hi")

b = 4
if b < 3:
    print("Hello!")

#もし違う条件だった場合"elif"
elif b < 5:
    print("Hi")
#上記以外の場合"else"=#elseはどれもみたしてなければなので条件指定しなくてよい。

else:
    print("Yeal!")



#論理演算子で記述
time = 15
if time > 5 and time <12:
    print("Good Morning!")
elif time >= 12 and time <18:
    print("Goodnafternoon!")
else:
    print("Fuck")


#条件分岐の基本構造は重要なので今後も見ておく


