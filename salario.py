salario = float(input("Qual o salario do funcionario? R$"))
novo_salario = salario + (salario * 15/100)
print("Um funcionario que ganhava {:.2f}, com o aumento de 15%, começou a ganhar {:.2f}". format(salario,novo_salario))
