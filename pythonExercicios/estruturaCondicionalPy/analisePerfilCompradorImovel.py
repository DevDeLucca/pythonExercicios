casa = float(input('Qual o valor do Imovel? '))
salario = float(input('Qual é o valor do salario em R$? '))
meses = float(input('Em quanto meses gostaria de pagar o imovel? '))
prestacoes = casa / meses
minimo = salario * 30 / 100
print('Para pagar as prestações do imovel de R${:.2f} em {:.2f} meses'.format(casa, meses))
print('A prestação será de R${:.2f}'.format(prestacoes))
if prestacoes <= minimo:
    print('Emprestimo consedido para financiar o Imovel')
else:
    print('Emprestimo negado para financiar o imovel, pois o valor Excede 30% do salario')
