distancia = float(input('Qual e a Quilometragem percorrida pela viagem? '))
print('Você esta preste a começar uma corrida de {} Km.'.format(distancia))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua viagem sera de R$ {:.2f}'.format(preco))
