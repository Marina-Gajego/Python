soma = 0;
num = 0;
media = 0;

for i in range (1,11):
    num = int(input(f"Digite o numero {i}°: "))
    if(num > 0):
        soma = soma + num

media = soma/10
print(f"A media dos numeros positivos é de: {media}") 