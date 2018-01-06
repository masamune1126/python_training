#tupleはリストに近い

a = [2012,2013,2014]
b = (2012,2013,2014)

#tupleは通常の括弧

print(a)
print(b)

print(a[1])
print(b[1])
#tupleは1度作ると内容の変更が出来ないのがlistとの違い

#リストの内容を換えてみる
a[1] = 2016
print(a)


#↓エラーを出してみる
#b[1] = 2016
#print(b)

a.append(2015)
print(a)

#.appendは追加文字の追加

b.append(2015)
print(b)

#tuppleは要素追加も受付ない。

