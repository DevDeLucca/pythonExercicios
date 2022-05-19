from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas Opções são:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('--=--' * 15)
print('Computador Jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[computador]))
print('--=--' * 15)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada Invalida!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada Invalida!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
else:
    print('Jogada Invalida!')

