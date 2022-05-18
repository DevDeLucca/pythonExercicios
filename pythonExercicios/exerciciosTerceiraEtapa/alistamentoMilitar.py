from datetime import date
atual = date.today().year
nascimento = int(input('Entre com sua data de nascimento yyyy: '))
idade = atual - nascimento
print('Quem nasceu no ano de {} tem a idade {} no ano atual{}'.format(nascimento, idade, atual))
if idade == 18:
    print('Você precisa se alistar nesse ano!')
elif idade < 18:
    saldo = 18 - idade
    print('Você não possui idade suficiente para se alistar'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Voce deveria ter se alistado em {}'.format(ano))
