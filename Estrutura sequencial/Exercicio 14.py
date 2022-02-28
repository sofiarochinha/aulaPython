print('Rendimento diário de um pescador')

#numero de quilos regulamentado
quilosMaximo = 50

quilosPescado = int(input('Insira o número de quilos de peixes pescados: '))

#não tem verificação se o valor for zero ou negativo
excesso = quilosPescado - quilosMaximo
multa = excesso * 4 #paga uma multa por cada quilo excedente

print('O número de quilos excedidos é: ' , excesso)
print('A multa a pagar é de: ' , multa , '€')
