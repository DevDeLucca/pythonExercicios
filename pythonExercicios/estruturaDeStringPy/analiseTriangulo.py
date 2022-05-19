print('--=--' *20)
print('Analisador de triangulos')
print('--=--' *20)

t1 = float(input('Informe o primeiro valor do triangulo: '))
t2 =  float(input('Informe o segundo valor do triangulo: '))
t3 = float(input('Informe o terceiro valor do triangulo: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t2 + t1:
    print('Os valores acima podem formar triangulos!')
else:
    print('Os valores acima não podem formar triangulo!')
