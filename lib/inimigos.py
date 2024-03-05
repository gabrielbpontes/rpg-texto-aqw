from .usuario import Personagem


class Inimigo(Personagem):
    """Classe dos inimigos"""
    def __init__(self, nome, vida, ataque, defesa, pontos_xp, dinheiro):
        super().__init__(vida, ataque, defesa)
        self.__nome = nome
        self.__pontos_xp = pontos_xp
        self.__dinheiro = dinheiro

    @property
    def nome(self):
        return self.__nome

    @property
    def pontos_xp(self):
        return self.__pontos_xp

    @property
    def dinheiro(self):
        return self.__dinheiro


# Inimigos
# Greenguard
frogzard = ('Frogzard', 8, 4, 0, 2, 2)
wereboar = ('Wereboard', 14, 5, 1, 6, 5)
greenguard = (frogzard, wereboar)

# Necropolis
ghoul = ('Ghoul', 16, 6, 1, 3, 3)
bellhop = ('Bellhop', 30, 12, 12, 12, 11)
necropolis = (ghoul, bellhop)

# Doomwood
treeant = ('Treeant', 10, 5, 3, 5, 5)
ectomancer = ('Ectomancer', 14, 8, 6, 7, 8)
doomwood = (treeant, ectomancer)
