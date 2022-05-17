real = float(input('Qual o valor em R$ que deseja converter ?'))
dolar = real /4.96
euros = real /5.21
ienes = real /0.038
print('Com R${:.2f} você pode cotar U$ Americanos {:.2f}'.format(real,dolar))
print('Com R${:.2f} você pode cotar E$ Europeus {:.2f}'.format(real,euros))
print('Com R${:.2f} você pode cotar U${:.2f} '.format(real,ienes))

