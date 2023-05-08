import pygame

fps = pygame.time.Clock()
largura = 1024
altura = 600

JogoLoop = True

tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption("Lucky Numbers")

ColorBack = {"azul": [0, 132, 252], "vermelho": [137, 28, 36]}

class Botao(pygame.sprite.Sprite):
    def __init__(self, *groups,image, image1, image2):
        super().__init__(*groups)

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, [190, 49])
        self.rect = pygame.Rect(190, 49, 190, 49)
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load(image1).convert_alpha()
        self.image2 = pygame.image.load(image2).convert_alpha()

        self.touche = False

    def update(self):
        self.mouse = pygame.mouse.get_pressed()
        self.MousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.MousePos):

            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                self.image = self.image2

            else:
                self.touche = False
                self.image = self.image1

        pass



ButtonGrups = pygame.sprite.Group()

Botao1 = Botao(ButtonGrups,image="imagens_gerais/red_button01.png",image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao1.rect.center = (250, 300)

Botao2 = Botao(ButtonGrups,image="imagens_gerais/red_button01.png",image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao2.rect.center = (512, 300)


Botao4 = Botao(ButtonGrups,image="imagens_gerais/red_button01.png",image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao4.rect.center = (512, 400)

Botao3 = Botao(ButtonGrups,image="imagens_gerais/red_button01.png",image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao3.rect.center = (250, 400)


while JogoLoop:
    fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            JogoLoop = False

        if Botao1.touche == True:
            tela.fill(ColorBack["vermelho"])

        if Botao2.touche == True:
            tela.fill(ColorBack["azul"])


        if Botao3.touche == True:
            tela.fill(ColorBack["azul"])

        if Botao4.touche == True:
            tela.fill(ColorBack["azul"])

        else:
            tela.fill(ColorBack["azul"])

        ButtonGrups.update()
        ButtonGrups.draw(tela)

        pygame.display.update()
pygame.quit()





