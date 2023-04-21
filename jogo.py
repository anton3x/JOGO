import pygame
from pygame.locals import *
from sys import exit

pygame.init()

#condicoes da janela
altura = 640
largura = 480

window = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Lucky Numbers Game') #alterar nome da janela
while True:
    for event in pygame.event.get():
        if event.type == QUIT: #se clicar no botao "X" ele fecha a janela
            pygame.quit()
            exit()

    pygame.draw.rect(window,(255,0,0), (200, 300,100,50)) #desenhar retangulo
    pygame.draw.circle(window, (100, 0, 255), (200, 300), 40) #desenhar circulo
    pygame.draw.line(window, (255,255,0), (390,0), (390,600), 50) #desenhar linha
    pygame.display.update()
#def escolha():

print('piroca')
