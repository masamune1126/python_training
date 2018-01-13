#比較演算子【重要】
a = True
b = False

#ルール値Trueとfalseを宣言する
print (a)
print (b)

c = 5
d = c > 4
print(d)

#d=cは４より大きい
e = c < 4
print(e)

#cが5"以下"であればTrue
f = c <= 5
print(f)


#cが5"以上"であればTrue
g = c >= 5
print(g)

#等しいかどうかを判定する"=="
h = c == 5
print(h)

#等しくないのを判別する[!]True
i = c != 5
print(i)


#文字列で等しいかを判定する場合
j = "Hello!"
k = "Hello!"
l = j == k
print(l)

m = "Hi!"
n = m == j
print(n)
