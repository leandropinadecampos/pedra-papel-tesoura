# JOKENPÔ ou PEDRA, PAPEL, TESOURA!
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice

opcoes = ['Pedra','Papel','Tesoura']
pc = choice(opcoes)

print ('=-=' * 20)
print ('Vamos jogar Pedra, Papel ou Tesoura!'.center(60))
print ('=-=' * 20)
print()
print ('Escolha as seguintes opções:')
print ('[1] Pedra')
print ('[2] Papel')
print ('[3] Tesoura')
print()

while True:
    try:
        usuario = int (input ('Escolha: '))

        if usuario == 1:
            jogador = 'Pedra'
            break
        elif usuario == 2:
            jogador = 'Papel'
            break
        elif usuario == 3:
            jogador = 'Tesoura'
            break
        else:
            print ('Opção Inválida, tente novamente')

    except ValueError:
        print ('Digite um número válido')

vitoria = {
    'Pedra': 'Tesoura',
    'Papel': 'Pedra',
    'Tesoura': 'Papel'
}

import time
print ('PEDRA!')
time.sleep(0.5)
print ('PAPEL!')
time.sleep(0.5)
print ('TESOURA!')
time.sleep(0.5)

print()
print (f'Você escolheu: {jogador}')
print (f'O computador escolheu: {pc}')
print()

if jogador == pc:
    print ('Empate!')
elif vitoria[jogador] == pc:
    print ('Você ganhou!')
else:
    print ('Computador ganhou!')
