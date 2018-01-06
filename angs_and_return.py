a = 7
b = 3

#c,dは引数
def add1(c , d):
    e = c + d
    print(e)

add1(a , b)

#返り値の概念
def add2(c,d):
    e = c + d
    return e

f = add2(a,b)
print(f)
