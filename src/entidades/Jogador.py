jogadores = []

def get_jogadores():
    return jogadores

def set_jogador(jogador):
    jogadores.append(jogador)

class Jogador:
    def __init__(self, nome, rating_atual, titulo_fide=None, estrangeiro=False):
        self.nome = nome
        self.rating_atual = rating_atual
        self.titulo_fide = titulo_fide if titulo_fide in {'CM', 'FM', 'IM', 'GM'} else 'Sem Título'
        self.estrangeiro = estrangeiro

    def __str__(self):
        formato = '{:<20} | {:<4} | {:<3} | {:<3} |'
        return formato.format(self.nome, self.rating_atual, self.titulo_fide, 'Sim' if self.estrangeiro else 'Não')

    @classmethod
    def seleciona_jogadores(cls, prefixo_nome=None, rating_minimo=None, titulo_fide=None, estrangeiro=None):
        jogadores_selecionados = []
        for jogador in jogadores:
            if rating_minimo is not None and jogador.rating_atual < rating_minimo:
                continue
            if prefixo_nome is not None and not jogador.nome.startswith(prefixo_nome):
                continue
            if titulo_fide is not None and jogador.titulo_fide != titulo_fide:
                continue
            if estrangeiro is not None and jogador.estrangeiro != estrangeiro:
                continue
            jogadores_selecionados.append(jogador)
        for jogador in jogadores_selecionados:
            print(jogador)

set_jogador(Jogador('Magnus Carlsen', 2850, 'GM', True))
set_jogador(Jogador('Artur Fonseca', 1900))
set_jogador(Jogador('Fabiano Caruana', 2823, 'GM', True))

Jogador.seleciona_jogadores(estrangeiro=False)




        

        