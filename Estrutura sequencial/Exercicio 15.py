print('Calcular o salário liquído a partir do salário bruto')

salarioBruto = int(input('Qual é o seu salário bruto?'))
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print('+ salário bruto: ' , salarioBruto)
print('- IR: ' , impostoRenda)
print('- INSS: ', inss)
print('- sindicato: ', sindicato)
print('= Salario Liquido: ', salarioLiquido)