import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#condicoes da janela
altura = 640
largura = 480
relogio = pygame.time.Clock()
imagem = pygame.image.load('background.png')
x = 0
y = 0

window = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Lucky Numbers Game') #alterar nome da janela
while True:
    relogio.tick(144)
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT: #se clicar no botao "X" ele fecha a janela
            pygame.quit()
            exit()

    pygame.draw.rect(window, (255, 0, 0), (x, y, 100, 50)) #desenhar retangulo (janela, cor,(posicao, tamanhos))
    #pygame.draw.circle(window, (100, 0, 255), (200, 300), 40) #desenhar circulo
    #pygame.draw.line(window, (255,255,0), (390,0), (390,600), 50) #desenhar linha
    pygame.display.update()
    if y >= altura:
        y = 0
    else:
        y += 1
#def escolha():

