n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno foi de {:.1f}'.format(n1, n2, media))
if 7 > media >= 5:
    print('O Aluno esta em Recuperação')
elif media < 5:
    print('O Aluno esta reprovado.')
elif media >= 7:
    print('O Aluno foi aprovado.')
