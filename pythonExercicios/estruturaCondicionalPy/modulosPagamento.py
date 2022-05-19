print('{:=^60}'.format(' Lojas Casas Bahia '))
preco = float(input( 'Preço das compras: R$ ' ))
print(''' Formas de Pagamento
[ 1 ] À Vista Dinheiro
[ 2 ] À Vista Debito ou Pix
[ 3 ] À Vista Cartão de Credito
[ 4 ] 2 x no cartão
[ 5 ] 3 x ou mais no cartão''')

opcao = int(input('Qual e a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 10 / 100)
elif opcao == 3:
    total = preco - (preco * 5 / 100)
elif opcao == 4:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada de R$ {:.2f} Vezes de R$ {:.2f} SEM JUROOS'.format(totalparc, parcela))
elif opcao == 5:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em R$ 2x vezes de R$ {:.2f}'.format(parcela))
print('Sua Compra de  R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, total))

