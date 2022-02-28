primeiroInt = int(input('Insira um número inteiro: '))
segundoInt = int(input('Insira um segundo número inteiro: '))

numeroReal = float(input('Insira um número real: '))

print('a. O produto do dobro do primeiro com metade do segundo \n')

respostaA = 2*primeiroInt * segundoInt/2
print('Resposta a: ' , respostaA)

print('b. a soma do triplo do primeiro com o terceiro.\n')
respostaB = 3*primeiroInt + numeroReal

print('Resposta b: ' , respostaB)

print('c. o terceiro elevado ao cubo.')

#https://www.educative.io/edpresso/calculating-the-exponential-value-in-python
respostaC = numeroReal ** 3 # ou respostaC = pow(numeroReal, 3)

print('Resposta c: ' , respostaC)