#論理演算子
#aの条件判定の書き方

#andの右と左が両方当てはまる場合Trueを出す演算子
a = 5
b =  a > 4 and a <6
print(b)


#andより右と左があってなければFalse
c = a > 4 and a < 2
print(c)


#orは右か左どちらかがただしければTrueがかえる どっちもちがうと　Falese
d = a <3 or a >4
print(d)

e = a < 3 or a > 5
print(e)

#not演算値はルールを反転させる
f = not a == 5
print(f)

g = not a ==4
print(g)
