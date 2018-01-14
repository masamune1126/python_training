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



# 関数print_handを定義してください
def print_hand():
     print("グーを出しました")
# 関数print_handを呼び出してください
print_hand()


# 引数を受け取れるようにしてください
def print_hand(hand):
    # 「◯◯を出しました」と出力されるように書き換えてください
    print( hand +'を出しました')

# 引数に文字列グーを入れてください
print_hand('グー')

# 引数を文字列パーとして関数print_handを呼び出してください
print_hand('パー')

def print_hand(hand, name):
    # 「◯◯は□□を出しました」と出力されるように書き換えてください
    print(name + 'は' + hand + 'を出しました')

# 第2引数に文字列「にんじゃわんこ」を入れてください
print_hand('グー', 'にんじゃわんこ')

# 第2引数に文字列「コンピューター」を入れてください
print_hand('パー', 'コンピューター')
