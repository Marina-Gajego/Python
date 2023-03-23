altura = eval(input("Digite sua altura: "))
sexo = (input("Digite seu sexo F ou M: "))

if(sexo == 'F' or sexo == 'f'):
    peso = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {peso}')
elif(sexo == 'M' or sexo == 'm'):
    peso = (72.7 * altura) - 58
    print(f'Seu peso ideal é {peso}')
else:
    print('Algum dado foi digitado incorretamente!')


