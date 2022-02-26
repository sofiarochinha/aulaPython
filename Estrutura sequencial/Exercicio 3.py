print('Vamos calcular a soma de dois numeros')
numero1 = input('Digite o primeiro numero: ')
numero2 = input('Digite o segundo numero: ')

#como o input retorna uma string é perciso transformar a string em números inteiros
soma = int(numero1) + int(numero2)

print('A soma é: ' + str(soma)) #str(soma) para poder imprimir o valor da soma é perciso transformar novamente a variável em string