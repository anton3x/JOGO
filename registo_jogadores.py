import pygame
import sys

# Inicializa o Pygame
pygame.init()
fps = pygame.time.Clock()

# Define as cores
AZUL = (0, 0, 255)

# Define a largura e altura da tela
largura = 1024
altura = 600

# Cria a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Lucky Numbers")
font = pygame.font.Font(None, 32)
text = ''

input_rect = pygame.Rect(200,200,140,32)
cor_ativa = pygame.Color('lightskyblue3')
cor_passiva = pygame.Color('gray15')
cor = cor_passiva
ative = False

# Função para exibir texto na tela
def exibir_texto(texto, posicao):
    fonte = pygame.font.Font(None, 25)
    superficie_texto = fonte.render(texto, True, (255, 255, 255))
    tela.blit(superficie_texto, posicao)



# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                ative = True
            else:
                ative = False

        if event.type == pygame.KEYDOWN:
            if ative == True:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode


    # Preenche a tela com a cor azul
    tela.fill((0,0,0))

    if ative:
        cor = cor_ativa
    else:
        cor = cor_passiva
    pygame.draw.rect(tela, cor_ativa, input_rect,2)
    # Exibe o texto na tela
    exibir_texto("Nome de jogador:", (50, 50))

    text_surface = font.render(text, True, (255,255,255))
    tela.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(100,text_surface.get_width() + 10)

    # Atualiza a tela
    pygame.display.flip()
    fps.tick(60)