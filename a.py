import pygame
import pygame_gui

pygame.init()

def table_exibicao(botoes, table, ButtonGrups):


    # Desenhar cada trevo e associar um botão
    for i in range(len(table)):
        imagem_fundo = "trevos/" + str(table[i]) + ".png"
        x = 410
        y = 62
        dim = 30
        espacamento = 35
        if len(table) > 9:
            if i == 0:
                x = 410
                botao = Botao1(ButtonGrups, image=imagem_fundo,image1=imagem_fundo, image2=imagem_fundo, dim=dim)
                botao.rect.center = (x, y)
                botoes.insert(i, botao)
            elif i % 2 == 0 and i < 13:
                multiplicador = i // 2
                x += multiplicador * espacamento  # Posição x do trevo

            # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo,image1=imagem_fundo, image2=imagem_fundo, dim=dim)
                botao.rect.center = (x, y)
                botoes.insert(i, botao)
            elif i % 2 != 0 and i < 13:
                multiplicador = i // 2 + 1
                x -= multiplicador * espacamento  # Posição x do trevo

                # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo, image1=imagem_fundo, image2=imagem_fundo, dim=dim)

                botao.rect.center = (x, y)
                botoes.insert(i, botao)

            if i % 2 == 0 and i >= 13:
                y = 95
                multiplicador = i // 2 - 6
                x += multiplicador * espacamento  # Posição x do trevo

            # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo,image1=imagem_fundo, image2=imagem_fundo, dim=dim)
                botao.rect.center = (x, y)
                botoes.insert(i, botao)
            elif i % 2 != 0 and i >= 13:
                y = 95
                multiplicador = i // 2 - 6
                x -= multiplicador * espacamento  # Posição x do trevo

                # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo, image1=imagem_fundo, image2=imagem_fundo, dim=dim)

                botao.rect.center = (x, y)
                botoes.insert(i, botao)
        else:
            dim = 50
            espacamento = 55
            y = 82
            x = 410
            if i == 0:
                x = 410
                botao = Botao1(ButtonGrups, image=imagem_fundo, image1=imagem_fundo, image2=imagem_fundo, dim=dim)

                botao.rect.center = (x, y)
                botoes.insert(i, botao)
            elif i % 2 == 0:
                multiplicador = i // 2
                x += multiplicador * espacamento  # Posição x do trevo

            # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo,image1=imagem_fundo, image2=imagem_fundo, dim=dim)
                botao.rect.center = (x, y)
                botoes.insert(i, botao)
            elif i % 2 != 0:
                multiplicador = i // 2 + 1
                x -= multiplicador * espacamento  # Posição x do trevo

                # Verificar se o trevo está selecionado
                botao = Botao1(ButtonGrups, image=imagem_fundo, image1=imagem_fundo, image2=imagem_fundo, dim=dim)

                botao.rect.center = (x, y)
                botoes.insert(i, botao)


largura = 1024
altura = 600
posx1 = 11
posy1 = 12
screen = pygame.display.set_mode((largura, altura))
ui_manager = pygame_gui.UIManager((largura, altura))
BACKGROUND_COLOR = (0, 132, 252)
imagem_regras = pygame.image.load("imagens_jogo/template_jogo_final.png")


class Botao1(pygame.sprite.Sprite):
    def __init__(self, *groups, image, image1, image2, dim):
        super().__init__(*groups)

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, [dim, dim])  # dimensoes botao voltar atras
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
                # self.image = self.image2

            else:
                self.touche = False
                # self.image = self.image1

        pass

ButtonGrups = pygame.sprite.Group()
ButtonGrups1 = pygame.sprite.Group()

table = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
Botoes = []
table_exibicao(Botoes, table, ButtonGrups)

clock = pygame.time.Clock()
running = True
a = 0
exibido = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if Botoes[0].touche:
            print("Botão %d pressionado" % (0+1))
            table.append(15)


        if len(table) > 9:
            table_exibicao(Botoes, table, ButtonGrups1)
        else:
            table_exibicao(Botoes, table, ButtonGrups)
        print(table)
        ui_manager.process_events(event)

    ui_manager.update(clock.tick(60) / 1000.0)

    screen.fill(BACKGROUND_COLOR)
    imagem_regras = pygame.transform.scale(imagem_regras, (1024, 600))

    screen.blit(imagem_regras, (0, 0))

    ui_manager.draw_ui(screen)

    ButtonGrups.update()
    ButtonGrups.draw(screen)
    ButtonGrups1.update()
    ButtonGrups1.draw(screen)
    if len(table) == 10:
        ButtonGrups.empty()
    ButtonGrups.update()
    #ButtonGrups.draw(screen)
    pygame.display.flip()

pygame.quit()
