import pygame
def botao2():
    fps = pygame.time.Clock()
    largura = 1024
    altura = 600

    JogoLoop = True

    tela = pygame.display.set_mode([largura, altura])
    pygame.display.set_caption("Lucky Numbers")

    ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36]}

    while JogoLoop:
        fps.tick(60)
        tela.fill(ColorBack["azul"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                JogoLoop = False


            pygame.display.update()
    pygame.quit()