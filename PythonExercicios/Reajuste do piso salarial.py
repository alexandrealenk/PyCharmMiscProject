salário = float(input('Qual o piso atual? R$ '))
valor = float(input('Qual o valor da porcentagem de aumento? '))
reajuste = salário + (salário * (valor/100))
print('Com o aumento de {}%, o novo valor do piso salarial passou a ser R${:.2f}'.format(valor, reajuste))
