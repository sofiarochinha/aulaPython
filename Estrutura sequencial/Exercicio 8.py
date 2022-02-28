print('Calcular o salário do mês')

#ganho por hora
#\n é um caracter especial que muda de linha
ganhoHora = int(input('Quanto ganha por hora? \n'))

#numero de horas que trabalha por mes
horasMes = int(input('Numero de horas que trabalha por mês? \n'))

print('O seu salário é de: ' + str(ganhoHora * horasMes) + '€')