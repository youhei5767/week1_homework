#下記のコードが期待通り動作するような、1から6の整数をランダムに出力する dice() 関数を実装してください
#print(dice()) # 1から6の整数をランダムに出力する

import random
def dices():
    return random.randint(1,6)
print(dices())


