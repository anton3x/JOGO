
import pygame

pygame.init()

# Definir as dimensões da janela
largura = 400
altura = 300

# Criar a janela
janela = pygame.display.set_mode((largura, altura))

# Carregar a imagem do botão
botao_imagem = pygame.image.load("imagens_gerais/x.png")

# Definir as dimensões e a posição do botão
botao_largura = 100
botao_altura = 50
botao_pos_x = largura // 2 - botao_largura // 2
botao_pos_y = altura // 2 - botao_altura // 2

# Criar o objeto de superfície do botão
botao = pygame.Surface((botao_largura, botao_altura))
botao.blit(botao_imagem, (0, 0))

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            # Verificar se o botão foi clicado
            if botao.get_rect().move(botao_pos_x, botao_pos_y).collidepoint(evento.pos):
                print("Botão clicado!")

    # Preencher a janela com a cor de fundo
    janela.fill((255, 255, 255))

    # Desenhar o botão na janela
    janela.blit(botao, (botao_pos_x, botao_pos_y))

    # Atualizar a tela
    pygame.display.update()
