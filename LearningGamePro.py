from Playable import Playable
from Enemy import Enemy

print('------------------------------------')
print('ゲームを初期化しています')

Djeeta = Playable('ジータ', 500,20)
Cocytus = Enemy('コキュートス' , 1000,40)

Djeeta.Attack(Cocytus)

