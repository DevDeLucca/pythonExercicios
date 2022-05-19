salario = float(input('Qual é o salario do funcionario em R$ ?'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O salario com atualização sera de R${:.2f} '.format(novo))
