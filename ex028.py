import random
import time

print('COMPUTADOR PENSANDO...')
time.sleep(2)
pcNumber = random.randint(1, 4)
userNumber = int(input('Que número o computador pensou? '))
time.sleep(1)
if userNumber == pcNumber:
    print('Parabéns, você acertou... O número pensado pelo computador foi {}'.format(pcNumber))
else:
    print('Você errou, Tente Novamente! O número era {}'.format(pcNumber))







