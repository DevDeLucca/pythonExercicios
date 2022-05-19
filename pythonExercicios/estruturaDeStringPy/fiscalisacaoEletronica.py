velocidade = float(input('Qual a velocidade do carro para a via em questão? '))
if velocidade > 80:
    print('MULTADO, você excedeu o valor permitido para a via, que seria 80KM H')
    multa = (velocidade-80)* 7
    print('Sendo assim você deve pagar uma multa proporcional ao valor excedido de {}'.format(multa))
print('Tenha um otimo dia, a velocidade esta dentro do permitido...')
