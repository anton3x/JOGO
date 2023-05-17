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
    html_text="<body><font face='imapact' color='#00FF00'>     Ideia de Jogo:</font> Cada jogador tenta ser o primeiro a preencher completamente o seu jardim com trevos. Mas eles devem verificar se, a qualquer momento, os números são organizados em ordem crescente em cada linha e coluna."
              "\n     Configuração do Jogo: Use um conjunto completo de blocos de trevo (= 1 cor numerada de 1 a 20) por jogador. Com menos de 4 jogadores, devolva as peças não utilizadas à caixa do jogo. \n Embaralhe os trevos e coloque-os virados para baixo no meio da mesa. \n Cada jogador leva um jogo bordo e orienta-o para que a joaninha esteja no canto inferior direito."
              "\n     "
              "\n     Marcação dos pontos: Os jogadores que escolheram a carta mais próxima ao número alvo ganham pontos. O primeiro colocado ganha 2 pontos; o segundo colocado ganha 1 ponto; nenhum outro participante pontua nessa etapa."
              "\n     Descarte e compra das cartas: Os participantes descartam as selecionados anteriormente e pegam outras novas no lugar delas. Se todas acabarem durante essa troca, reembaralhe os itens deixados pelos outros competidores antes naquele espaço disponível novamente." 
              "\n     Fim do jogo: Quando algum participante chegar aos 10 pontos, a disputa termina, e quem tiver obtido mais alcances é o vencedor!"
              "</font></body>",
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



