from datetime import date
atual = date.today().year
nasci = int(input('Entre com a data de nascimento: '))
idade = atual - nasci
print('O atleta possui {} anos de idade'.format(idade))
if idade <= 9:
    print('O Atleta foi classificado como MIRIM')
elif idade <= 14:
    print('O atleta foi classificado como INFANTIL')
elif idade <= 19:
    print('O atleta foi classificado como JUNIOR')
elif idade <= 25:
    print('O atleta foi classificado como SENIOR')
else:
    print('O atleta foi classificado como MASTER')
