valAtualSal = float(input('Informe o valor atual do salario: '))
valDeAumento = float(input('Informe o valor da pordcentagem de aumento: '))

novoValor = valAtualSal + (valAtualSal * valDeAumento/100)

print('O valor do salario era de {} com o aumento de {} fica por {:.2f}' .format(valAtualSal, valDeAumento, novoValor))
