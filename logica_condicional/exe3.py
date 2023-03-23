import math
num = eval(input("Digite um numero: "))

if(num >= 0):
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz}')
else:
    quadrado = num * num
    print(f"O quadrado de {num} é {quadrado}")
