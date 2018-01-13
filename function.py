#関数の使い方
def func1():
    print("World!")
#func1()

def func2():
    print("Hello")
    func1()

func2()



def func3():
    print("Hi!")
    func2()

func1()