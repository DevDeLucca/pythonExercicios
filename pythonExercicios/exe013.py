valProd = float(input('Informe o valor do produto: '))
valDesc = float(input('Informe o valor da pordcentagem de desconto: '))

novoValor = valProd - (valProd * valDesc/100)
print('O valor do Produto era de {} com desconto de {} fica por {}' .format(valProd, valDesc, novoValor))
