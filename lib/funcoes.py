# Importando pacotes
from random import choice
from time import sleep

from .usuario import usuario, clear
from .inimigos import greenguard, necropolis, doomwood, Inimigo


def menu_principal():
    """Função para chamar o menu principal"""
    print('Menu principal')
    print('___________________')
    print('| 1 Novo jogo     |')
    print('| 2 Carregar jogo |')
    print('-------------------')
    opcao = input('Escolha uma das opções: ').strip(" ").lower()
    clear()

    if opcao in ('novo jogo', '1'):
        print('Novo jogo iniciado!')
        menu_opcoes()

    elif opcao in ('carregar jogo', '2'):
        try:
            usuario.load()
            menu_opcoes()

        except FileNotFoundError:
            print('Arquivo de save não encontrado.')

    else:
        print('Opção inválida.')

    sleep(2)
    menu_principal()


def menu_opcoes():
    """Função para chamar o menu de opções"""
    print('Menu de opções')
    print('__________________________')
    print('| 1 Mapa    4 Descansar  |')
    print('| 2 Status  5 Artefatos  |')
    print('| 3 Salvar  6 Inventário |')
    print('|           7 Sair       |')
    print('--------------------------')
    opcao = input('Digite uma das opções do menu: ').strip(" ").lower()
    clear()

    match opcao:
        case ('mapa' | '1'):
            mapa()
        case ('status' | '2'):
            usuario.status()
        case ('salvar' | '3'):
            usuario.save()
        case ('descansar' | '4'):
            usuario.vida_atual, usuario.mana_atual = usuario.vida, usuario.mana
            print('Você monta uma tenda para descansar um pouco...')
            print('Descansando, você recupera sua vida e mana!')
        case ('artefatos' | '5'):
            usuario.equips()
        case ('inventario' | '6'):
            usuario.invent()
        case ('sair' | '7'):
            print('Programa finalizado.')
            exit()
        case _:
            print('Opção inválida')

    sleep(2)
    menu_opcoes()


def mapa():
    """Função para visualizar mapa"""
    print('Locais disponíveis')
    print('______________________________')
    print('| 1 Greenguard  3 Necropolis |')
    print('| 2 Battleon    4 Doomwood   |')
    print('|               5 Sair       |')
    print('------------------------------')
    local = input(
        'Digite uma opção, ou sair para voltar ao menu de opções: ').strip(" ").lower()

    match local:
        case ('Greenguard' | '1'):
                inimigo = Inimigo(*choice(greenguard))
                usuario.batalha(inimigo)
        case ('Battleon' | '2'):
                battleon()
        case ('Necropolis' | '3'):
                inimigo = Inimigo(*choice(necropolis))
                usuario.batalha(inimigo)
        case ('Doomwood' | '4'):
                inimigo = Inimigo(*choice(doomwood))
                usuario.batalha(inimigo)
        case ('sair' | '5'):
                menu_opcoes
        case _:
                print('Local inválido.')
                sleep(2)

    # Verificando se o usuário subiu de nível
    if usuario.barra_de_xp >= usuario.levelup:
        usuario.lvlup()

    clear()
    mapa()


def battleon():
    print('Ao entrar na vila, você vê diversas tavernas e lojas')
    print('_________________________')
    print('| 1 Apotecário  3 Sair  |')
    print('| 2 Ferreiro            |')
    print('-------------------------')
    local = input('Digite uma das opções, ou sair: ').strip(" ").lower()


