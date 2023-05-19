import pygame
import pygame_gui

pygame.init()

# Defina a largura e altura da tela
tela_largura = 1200
tela_altura = 700

# Crie a tela
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Jogo dos Trevos")

# Defina a largura e altura da tela
tela_largura = 1200
tela_altura = 700

# Crie a tela
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Jogo dos Trevos")

# Crie o gerenciador de interface do usuário
gerenciador = pygame_gui.UIManager((tela_largura, tela_altura))


# Defina a posição e tamanho da caixa de texto
pos_x = 960
pos_y = 260
largura = 218
altura = 306

# Crie a caixa de texto
caixa_texto = pygame_gui.elements.UITextBox("",
                                            relative_rect=pygame.Rect((pos_x, pos_y), (largura, altura)),
                                            manager=gerenciador)

# Variável para armazenar os passos do jogador
passos = ["asdadsadsa","ASDads"]

# Loop principal do jogo
rodando = True
clock = pygame.time.Clock()
while rodando:
    tempo_delta = clock.tick(60) / 1000.0

    # Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Atualize a interface do usuário
        gerenciador.process_events(evento)

        # Adicione a lógica do jogo aqui
        # Por exemplo, adicione um passo à lista de passos quando o jogador selecionar um trevo
        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Adicione um passo à lista de passos
            passos.append("Passo: Jogador selecionou um trevo")

            # Atualize a caixa de texto com os passos
            caixa_texto.html_text = "\n".join(passos)
            caixa_texto.rebuild()

    # Atualize a interface do usuário
    gerenciador.update(tempo_delta)

    # Desenhe a tela e a interface do usuário
    tela.fill((0, 0, 0))
    gerenciador.draw_ui(tela)

    pygame.display.flip()