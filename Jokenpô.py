
#Jogo de jokenpô usandom a biblioteca random
import random
from time import sleep

def jokenpô():
    while True:
        print(f'Bem vindo ao jogo Jokenpô!')
        sleep(0.5)
        escolha_usuário = str(input('\nEscolha Pedra, Papel ou Tesoura: '))
        escolha_usuário = escolha_usuário.upper()
        escolha_computador = ['Pedra', 'Papel', 'Tesoura']
        computador = random.choice(escolha_computador)
        computador = computador.upper()
        print(f'O computador escolheu: {computador}')
        print(f'O usuário escolheu: {escolha_usuário}')

        if escolha_usuário == computador: 
            sleep(1.0)
            print(f'Empatou!')

        elif escolha_usuário == 'PEDRA' and computador == 'TESOURA':
            print(f'Você ganhou.')
            sleep(1.0)
            print(f'Parabéns, campeã(o)!')   

        elif escolha_usuário == 'TESOURA' and computador == 'PAPEL':
            print(f'Você ganhou.')
            sleep (1.0)
            print(f'Parabéns, campeã(o)!')

        elif escolha_usuário == 'PAPEL' and computador == 'PEDRA':
            print(f'Você ganhou.')
            sleep(1.0)    
            print(f'Parabéns, campeã(o)!')

        else:
            print(f'Você perdeu.')

        continuar = str(input('[S] Para sim | [N] Para não: '))
        continuar = continuar.upper()
        if continuar not in ['S', 'SIM']:
            print(f'=-=' * 15)
            sleep(1.5)
            print(f'ENCERRANDO O JOGO')
            print(f'=-=' * 15)
            break

        

jogo = jokenpô()