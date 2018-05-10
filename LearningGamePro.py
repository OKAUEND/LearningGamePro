from Playable import Playable
from Enemy import Enemy
import random

print('------------------------------------')
print('ゲームを初期化しています')

Djeeta = Playable('ジータ', 500,20)
Cocytus = Enemy('コキュートス' , 1000,40)
Turn = 1
ClearFlag = True
print('ゲームの初期化が完了しました。')
print('------------------------------------')

while ClearFlag :
    print('Turn ' + str(Turn))
    Djeeta.info()
    Cocytus.info()

    print('あなたのターンです。行動を選んでください。')
    Choice = int(input('1:攻撃 / 2:防御 / 3:回復 : '))

    if Choice == 1:
        Djeeta.Attack(Cocytus)
    elif Choice == 2:
        Djeeta.Defence()
    elif Choice == 3:
        Djeeta.Heal()

    print('敵のターンです。')
    Choice = random.randrange(1,3)

    if Choice == 1:
        Cocytus.Attack(Djeeta)
    elif Choice == 2:
        Cocytus.Defence()
    elif Choice == 3:
        Cocytus.Heal()

    if Djeeta.HP == 0 or Cocytus.HP == 0:
        ClearFlag = False
    else:
        Turn += 1
        Djeeta.Guard = 0
        Cocytus.Guard = 0
    print('------------------------------------')

    print('ゲームを終了します')


