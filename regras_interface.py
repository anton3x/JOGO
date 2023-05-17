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


text_box = pygame_gui.elements.UITextBox(
    html_text="<body><font color='#FFA500' face='Times New Roman'><b>Ideia de Jogo:</b></font> Cada jogador tenta ser o primeiro a preencher completamente o seu jardim com trevos. Mas eles devem verificar se os números estão organizados em ordem crescente em cada linha e coluna.</body>"
              "\n<font color='#FFA500' face='Arial'><b>Configuração do Jogo:</b></font> Usa um conjunto completo de trevos (= 1 cor numerada de 1 a 20) por jogador. Com menos de 4 jogadores, devolve as peças não utilizadas à caixa do jogo. \n Embaralha os trevos e coloca-os virados para baixo no meio da mesa. \n Cada jogador leva um jogo bordo e orienta-o para que a joaninha esteja no canto inferior direito.</body>"
              "\n<font color='#FFA500' face='Verdana'><b>GamePlay:</b></font> O jogador mais velho começa e, em seguida, o jogo prossegue no sentido horário. Na tua vez, deves escolher uma das duas opções a seguir:"
              "\n<font color='#FFA500' face='Comic Sans MS'><b>A) Take a face-down clover:</b></font> Pega um trevo virado para baixo do meio da mesa e coloca-o, virado para cima, no tabuleiro de jogo (vê Regras de Colocação à direita). Se não podes ou não queres colocá-lo, deixa-lo, virado para cima no meio da mesa."
              "\n<font color='#FFA500' face='Comic Sans MS'><b>B) Take a face-up clover:</b></font> Não reveles outro trevo. Em vez disso, pega um dos trevos virados para cima e adicioná-lo ao tabuleiro de jogo em de acordo com as Regras de Colocação</b></font>." 
              "\n<font color='#FFA500' face='Comic Sans MS'><b>Regras de Colocação:</b></font> Podes adicionar um novo trevo a um espaço vazio no tabuleiro de jogo ou trocá-lo por um trevo colocado anteriormente (e devolver o trevo trocado no meio da mesa, com a face para cima)."
              "\nO número do trevo que colocas no tabuleiro deve caber, em ordem crescente, com todos os outros números na sua linha e na sua coluna (mas os números em uma linha ou coluna não precisam seguir uns aos outros como 7,8,9...). "
              "</body>",
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



