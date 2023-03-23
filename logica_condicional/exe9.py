salario = eval(input("Digite o valor do salario: "))
emprestimo = eval(input("Digite o valor da prestação de emprestimo: "))

calcSalario = salario * 0.2

if(emprestimo > calcSalario):
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')

