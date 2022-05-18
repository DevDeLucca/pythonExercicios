peso = float(input('Entre com o peso da pessoa(Kg)! '))
altura = float(input('Entre com a altura da pessoa(Mts)! '))
imc = peso / (altura ** 2)
print(' O Indice de massa corporal e de {}'.format(imc))
if imc < 18.5:
    print('Considerado abaixo do ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Considerado PESO IDEAL')
elif 25 <= imc < 30:
    print('Considerado SOBRE PESO, ATENÇÃO!')
elif 30 <= imc < 40:
    print('Considerado OBESIDADE, ATENÇÃO')
else:
    print('CONSIDERADO OBSEIDADE MORBIDA, MUITA ATENÇÃO')
