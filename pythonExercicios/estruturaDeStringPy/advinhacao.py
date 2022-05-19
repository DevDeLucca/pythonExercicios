from random import randint
from time import sleep
computador = randint(0, 5) #sorteia um numero de o a 5
print('--=--' *25)
print('Analisando possiveis numeros entre 0 e 5, tente advinhar...')
print('--=--' *25)
jogador = int(input('Digite sua opçao de numero para tentar me vencer: ')) # Jogador entra com um numero
print('Pensando...')
sleep(3)
if jogador == computador:
    print('Não consigo acreditar, você me venceu nessa')
else:
    print('Por sorte não pensei no numero {} é sim no {} sendo assim sua inteligencia artifical ganhou!' .format(jogador, computador))
