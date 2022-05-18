kmpercorridos = float(input('Informe o valor de Km percorridos com o Veiculo : '))
diasdeloc = int(input('Quantos foram os dias de locação do veiculo: '))

calckm = kmpercorridos * 0.15
calcdiaria = diasdeloc * 60

valortotalhapagar = calckm+calcdiaria

print('Os valores cobrados saõ de diaria {} e KM percorrido {} dando um valor total de {} ' .format(calcdiaria, calckm, valortotalhapagar ))
