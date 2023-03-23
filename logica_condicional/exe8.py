nota1 = eval(input("Digite a 1° nota: "))
nota2 = eval(input("Digite a 2° nota: "))

media = (nota1 + nota2)/2

if(nota1 > 10 or nota1 < 0):
    print('Valores invalidos digite uma nota de 0 a 10')
    exit
elif(nota2 > 10 or nota2 < 0):
    print('Valores invalidos digite uma nota de 0 a 10')
    exit
else:
    print(f"A media das notas {nota1} e {nota2} é {media}")
