from random import randint
computador = randint (0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    if jogador < computador:
     print('Mais... Tente novamente')
    if jogador > computador:
     print('Menos... Tente novamente')   
print('Acertou com {} palpites'.format(palpites))