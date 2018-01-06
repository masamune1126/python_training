a = 1
def func1():
    print(a)

func1()

def func2():
    b =  2
    print(b)

func2()

print(b)
#変数bが見つからないのは関数外からアクセスできないから。
#アクセスできる範囲内をスコープという。
