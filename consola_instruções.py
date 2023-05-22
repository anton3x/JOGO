import pygame
import pygame_gui

pygame.init()

# Defina a largura e altura da tela
tela_largura = 1200
tela_altura = 700

# Crie a tela
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Jogo dos Trevos")

# Crie o gerenciador de interface do usuário
gerenciador = pygame_gui.UIManager((tela_largura, tela_altura))

# Defina a posição e tamanho da caixa de texto e do container de rolagem
pos_x = 960
pos_y = 260
largura = 218
altura = 306


# Crie a caixa de texto dentro do container de rolagem
caixa_texto = pygame_gui.elements.UITextBox(html_text="<body><font color='#FFA500' face='Times New Roman'><b>Ideia de Jogo:</b></font> Cada jogador tenta ser o primeiro a preencher completamente o seu jardim com trevos. Mas eles devem verificar se os números estão organizados em ordem crescente em cada linha e coluna.</body>"
              "\n<font color='#FFA500' face='Arial'><b>Configuração do Jogo:</b></font> Usa um conjunto completo de trevos (= 1 cor numerada de 1 a 20) por jogador. Com menos de 4 jogadores, devolve as peças não utilizadas à caixa do jogo. \n Embaralha os trevos e coloca-os virados para baixo no meio da mesa. \n Cada jogador leva um jogo bordo e orienta-o para que a joaninha esteja no canto inferior direito.</body>"
              "\n<font color='#FFA500' face='Verdana'><b>GamePlay:</b></font> O jogador mais velho começa e, em seguida, o jogo prossegue no sentido horário. Na tua vez, deves escolher uma das duas opções a seguir:"
              "\n<font color='#FFA500' face='Comic Sans MS'><b>A) Take a face-down clover:</b></font> Pega um trevo virado para baixo do meio da mesa e coloca-o, virado para cima, no tabuleiro de jogo (vê Regras de Colocação à direita). Se não podes ou não queres colocá-lo, deixa-lo, virado para cima no meio da mesa."
              "\n<font color='#FFA500' face='Comic Sans MS'><b>B) Take a face-up clover:</b></font> Não reveles outro trevo. Em vez disso, pega um dos trevos virados para cima e adicioná-lo ao tabuleiro de jogo em de acordo com as Regras de Colocação</b></font>." 
              "\n<font color='#FFA500' face='Comic Sans MS'><b>Regras de Colocação:</b></font> Podes adicionar um novo trevo a um espaço vazio no tabuleiro de jogo ou trocá-lo por um trevo colocado anteriormente (e devolver o trevo trocado no meio da mesa, com a face para cima)."
              "\nO número do trevo que colocas no tabuleiro deve caber, em ordem crescente, com todos os outros números na sua linha e na sua coluna (mas os números em uma linha ou coluna não precisam seguir uns aos outros como 7,8,9...). "
              "</body>",
                                            relative_rect=pygame.Rect((0, 0), (largura, altura)),
                                            manager=gerenciador)

# Variável para armazenar os passos do jogador
passos = ["asdadsadsa", "ASDads","asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads""asdadsadsa", "ASDads"]

# Loop principal do jogo
rodando = True
clock = pygame.time.Clock()
tempo_delta = clock.tick(60) / 1000.0
passos.append("Passo: Jogador selecionou um trevo")

            # Atualize a caixa de texto com os passos
caixa_texto.html_text = "<br>".join(passos)
caixa_texto.rebuild()
while rodando:

    # Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Atualize a interface do usuário
        gerenciador.process_events(evento)


    # Atualize a interface do usuário
    gerenciador.update(tempo_delta)
    # Desenhe a tela e a interface do usuário
    tela.fill((0, 0, 0))
    gerenciador.draw_ui(tela)
    pygame.display.update()
    pygame.display.flip()
