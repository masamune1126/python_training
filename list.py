#listについて
a = [2012,2013,2014]
print(a)


#リストにアクセスする方法
print(a[0])
print(a[1])
print(a[2])


#Cで指定するリストの1-4を出力する。
#リストは複数の要素をまとめる事ができる。(文字もOK)
b = 2012
c = [b,2015,20.1,"Fuck","Hi"]
print(c[0:5])


fruits = ['apple', 'banana', 'orange']
# リストの末尾に文字列「grape」を追加してください
fruits.append('grape')


# 変数fruitsに代入したリストを出力してください
print(fruits)

# インデックス番号が0の要素を文字列「cherry」に更新してください
fruits[0] = 'cherry'

# インデックス番号が0の要素を出力してください
print(fruits[0])
