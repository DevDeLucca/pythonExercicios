media = float(input('Digite o valor percorrido em metros: '))

hm = float(media * 100)
dam = float(media * 10 )
mm = float(media / 1000)
cm = float(media / 100 )
dm = float(media / 10 )

print('O valor digitado {} em metros corresponde a {:.2f} Hectômetro  e {:.2f} Decâmetro e {} Milímetro e {} Centímetro e {} Decímetro ' .format(media, hm, dam, mm, cm, dm))
