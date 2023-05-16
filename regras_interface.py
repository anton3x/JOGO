import pygame
import pygame_gui

pygame.init()

# Define as dimensões da tela e cria a superfície
largura = 1024
altura = 600
screen = pygame.display.set_mode((largura, altura))

# Cria um gerenciador de interface de usuário e define o tema
ui_manager = pygame_gui.UIManager((largura, altura ), 'data/themes/theme_1.json')

# Define as dimensões e a posição da caixa de texto
largura_textbox = 800
altura_textbox = 400
posição_x_textbox = 100
posição_y_textbox = 150
text_box_rect = pygame.Rect(posição_x_textbox, posição_y_textbox, largura_textbox, altura_textbox)





# Cria a caixa de texto
text_box = pygame_gui.elements.UITextBox(
    html_text="<body><font color>O jogo é composto por dois tabuleiros de 4x4 espaços (casas) para cada jogador. Para jogar usam-se os trevos numerados de 1 a 20; um conjunto por cada jogador. Os trevos de ambos os jogadores são misturados num só saco. À vez, cada jogador retira um trevo do saco colocando-o no seu tabuleiro. Deve primeiro preencher os 4 espaços da diagonal principal e de seguida os restantes espaços. Como regra de base, quer na vertical quer na horizontal os números devem ser colocados em ordem estritamente crescente. As restantes regras podem ser lidas no ficheiro em "
              "f k.</font></body>",
    relative_rect=text_box_rect,
    manager=ui_manager)

# Define a cor de fundo da tela
BACKGROUND_COLOR = ([0, 132, 252])

imagem_regras = pygame.image.load("imagens_gerais/REGRAS.png")

# Loop principal do jogo
clock = pygame.time.Clock()
while True:
    # Processa os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        ui_manager.process_events(event)

    ui_manager.update(clock.tick(60) / 1000.0)

    screen.fill(BACKGROUND_COLOR)
    imagem_regras = pygame.transform.scale(imagem_regras, (420,245))

    screen.blit(imagem_regras, (280,-40))

    ui_manager.draw_ui(screen)
    pygame.display.update()



