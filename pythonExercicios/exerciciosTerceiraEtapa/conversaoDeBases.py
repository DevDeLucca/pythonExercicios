num = int(input('Digite seu numero inteiro para conversão: '))
print(''''Escolha uma das opções para conversão:
[ 1 ] Conversão para BINARIO
[ 2 ] Conversão para OCTAL
[ 3 ] Conversão para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} Convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opçaõ Digitada Invalida. Tente novamente')
