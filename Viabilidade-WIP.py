varentrada = int(input("""
                    Selecione o período:
                    Ano = 1
                    Mes = 0

                    """))
entradas = input('Selecione a quantidade de entradas:')


def fluxoCaixa(varentrada, entradas):
    year_list = []
    mouth_list = []
    for i in range(int(entradas)):
       if varentrada == 1:
            year_list.append(input())
       elif varentrada == 0:
            mouth_list.append(input())
    if varentrada == 1:
        print(year_list)
    elif varentrada == 0:
        print(mouth_list)

fluxoCaixa(varentrada, entradas)
