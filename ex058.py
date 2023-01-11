import random
import time

print('COMPUTADOR PENSANDO...')
time.sleep(2)
pcNumber = random.randint(1, 5)
userNumber = int(input('Que número o computador pensou? '))
time.sleep(1)
tent = 1
while pcNumber != userNumber:
    userNumber = int(input('Errado! Tente Novamente...Que número o computador pensou? '))
    time.sleep(1)
    tent += 1

print('Você acertou na {}ª tentativa. O número era {}'.format(tent, pcNumber))
