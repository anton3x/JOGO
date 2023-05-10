import pygame, sys

posx = 100
posy = 100

pygame.init()

largura = 800
altura = 800

cor_de_fundo = pygame.Color(0, 132, 252) #cor vai ser o azul usado na tela dos botoes inicial
class Botao(pygame.sprite.Sprite):
    def __init__(self, *groups,image, image1, image2):
        super().__init__(*groups)

        # A função `convert_alpha()` é usada para otimizar a imagem para exibição rápida.
        #self.image = pygame.image.load(image).convert_alpha()

        # Redimensiona a imagem carregada em `self.image` para o tamanho [144, 50]
        #self.image = pygame.transform.scale(self.image, [144, 158])

        # Cria um objeto retangular na posição (190, 49) com largura e altura de 144 e 158 pixels, respectivamente
        self.rect = pygame.Rect(posx, posy, 144, 158)

        # Obtém um objeto retangular que abrange toda a imagem carregada em `self.image`
        # Armazena o retângulo na variável `self.rect`
        #self.rect = self.image.get_rect()

        # Carrega duas imagens adicionais especificadas em `image1` e `image2` como objetos Pygame `Surface`
        #self.image1 = pygame.image.load(image1).convert_alpha()
        #self.image2 = pygame.image.load(image2).convert_alpha()

        #o botao foi tocado
        self.touche = False

    def update(self):
        self.mouse = pygame.mouse.get_pressed()
        self.MousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.MousePos):

            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                #self.image = self.image2

            else:
                self.touche = False
                #self.image = self.image1

        pass

screen = pygame.display.set_mode((largura, altura)) #janela
imagem_fundo = pygame.image.load("imagens_jogo/background.jpg").convert() #dá load da imagem
imagem_fundo = pygame.transform.scale(imagem_fundo, (500, 500)) #redimensiona a imagem

screen.blit(imagem_fundo, (10, 10)) #faz o blit + posicao da imagem

pygame.display.flip() # é uma função do Pygame que atualiza a tela.
# Basicamente, essa função faz com que qualquer mudança feita na tela desde a última atualização seja exibida para o usuário.

ButtonGrups = pygame.sprite.Group() #ButtonGrups é uma variável que contém um objeto do tipo Group.
# Esse objeto é usado para agrupar e gerenciar vários sprites do jogo, como botões, inimigos, jogadores, etc.

#botao invisivel do trevo posicao (1,1)
Botao1 = Botao(ButtonGrups,image="imagens_gerais/red_button01.png",image1="imagens_gerais/red_button01.png",image2="imagens_gerais/red_button02.png")
Botao1.rect.center = (100,100) #posicao

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            JogoLoop = False
            pygame.quit()
            sys.exit()

        if Botao1.touche == True: #cada vez que pressionar o botao, vai printar para motivos de verificacao
            print("ABC")

        ButtonGrups.update()
        #ButtonGrups.draw(screen)
    screen.fill(cor_de_fundo) #preenche com a cor
    screen.blit(imagem_fundo, (10,10)) #mete a imagem outra vez

    pygame.display.update() #dá update ao ecra