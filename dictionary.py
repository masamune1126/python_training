#辞書の使い方

#aに辞書のキーワードを登録する｛"名称":XX,"名称":XX｝
a = {"Taro":1985,"Hanako":1986}
print(a)

#taroの指定要素だけ取り出しする場合a[要素]で出力する
b = a["Taro"]
print(b)

#要素の追加をする際指定の要素の後にワードを追加して代入する
a["Jiro"] = 1988
print(a)

#指定した要素の変更をおこなう場合は代入の後の数字を変更する
a["Hanako"] = 1990
print(a)

#辞書登録は文字列以外も対応ができる。
c = {1:1991,2:1992}
print(c)

d = c[2]
print(d)



# 変数fruitsに辞書を代入してください
fruits = {"apple":"りんご","banana":"バナナ"}

# 辞書fruitsのキー「banana」に対応する値を出力してください
print(fruits['banana'])

# 辞書fruitsを用いて、「appleは◯◯という意味です」となるように出力してください
print("appleは" + fruits['apple'] + "という意味です")
