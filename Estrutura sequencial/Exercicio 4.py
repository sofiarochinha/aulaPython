print('Calcular a média de quatro notas')

#int(input()) -> pede um número a um utilizador e tranforma em inteiro
nota1 = int(input('Insere a primeira nota: '))
nota2 = int(input('Insere a segunda nota: '))
nota3 = int(input('Insere a terceira nota: '))
nota4 = int(input('Insere a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4)/4
print('A media das notas é: ' + str(media))