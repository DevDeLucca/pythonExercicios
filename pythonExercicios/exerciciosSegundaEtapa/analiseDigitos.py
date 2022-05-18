a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o Segundo numero: '))
c = int(input('Digite o Terceiro numero: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
        menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
        maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))


