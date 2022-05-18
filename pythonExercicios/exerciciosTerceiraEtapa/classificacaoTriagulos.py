t1 = int(input('Entre com o primeiro lado do triangulo'))
t2 = int(input('Entre com o segundo lado do triangulo'))
t3 = int(input('Entre com o terceiro lado do triangulo'))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 +t2:
    print('Pode formar um triangulo!')
    if t1 == t2 == t3:
        print('E um trinagulo Equilatero!')
    elif t1 != t2 != t3 != t1:
        print('E um triangulo ESCALENO')
    else:
        print('E um triangulo ISOCELES')
else:
    print('Não pode formar um triangulo!')
