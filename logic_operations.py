#論理演算子

a = 5
b = a > 4 and a <6
print(b)

#andより右と左があってればTrue

c = a > 4 and a < 2
print(c)

#andより右と左があってなければFalse

d = a < 3 or a > 4
print(d)

e = a <3 or a >5
print(e)

#orは右か左がただしければTrueがかえる どっちもちがうと　Falese

f = not a == 5
print(f)
#not演算値はルールを反転させる

