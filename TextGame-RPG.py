#
#
#
# JOGO
#
#
#
import random
player_vida = 1000
player_sp = 200
inimigo_vida = 50
n = int(input('Numero que inimigos que deseja enfrentar: '))
inimigos = []
for i in range(n):
    inimigos.append([i+1, inimigo_vida])

jogando = True
while jogando:
    print('Life Points:', player_vida)
    print('Magic Points:', player_sp)

    acao = int(input('Para Atacar, digite :1: - Para se curar, digite :2:'))

    if acao == 1:
        selecionado = random.choice(inimigos)
        dano = random.randint(10, 25)
        print('Inimigo atacado foi %i, causando %i de dano: ' %(selecionado[0], dano))
        selecionado[1] -= dano
        print('Pontos de vida do inimigo selecionado:%i' % selecionado[1])
        if selecionado[1] < 0:
            print('Você vendeu este inimigo')
    elif acao == 2 and player_sp > 10:
        cura = random.randint(10, 30)
        player_vida += cura
    else:
        print('Você não tem pontos de magia para se curar!')


















