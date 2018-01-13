    #for文の練習

a = [0,1,2,3,4,5]
for i in a:
    #listに入ってるaを一つづつ実行する指示
    print(i)


    # 省略表記rangeを使った方が完結なのでできるだけrangeを使う
for i in range(0,7):
    print(i)

for i in range(0,6):
    b = i * 2
    print(b)

    #様々なデータ処理
c = ["taro",1985,0.125,True]
print(c)
for i in c:
    print(i)




fruits = ['apple', 'banana', 'orange']

# for文を用いてリストの要素を1つずつ取り出し、「好きな果物は◯◯です」と出力してください
for fruit in fruits:
    print("好きな果物は" + fruit + "です")


fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}

# for文を用いて、辞書のキーを1つずつ取り出し、繰り返しの中で「◯◯は△△という意味です」と出力させてください
for fruit_name in fruits:
    print( fruit_name + "は" + fruits[fruit_name] + "という意味です")
