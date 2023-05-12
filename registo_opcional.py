import pygame
import pygame_gui

pygame.init()

# Definir o tamanho da janela
window_surface = pygame.display.set_mode((800, 600))

# Criar um gerenciador de eventos para lidar com eventos do Pygame GUI
manager = pygame_gui.UIManager((800, 600))

# Definir a fonte para a caixa de texto
fonte = pygame.font.Font(None, 36)

# Criar uma caixa de texto usando o Pygame GUI
caixa_texto = pygame_gui.elements.UITextEntryLine(
                relative_rect=pygame.Rect((300, 250), (200, 50)),
                manager=manager,
                #font=fonte
)

# Define o texto para o botão
texto_botao = "Nome:"

# Cria um botão usando o Pygame GUI
botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((325, 325), (150, 50)),
                                     text=texto_botao,
                                     manager=manager
)

# Loop principal
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        # Atualiza o gerenciador de eventos com os eventos do Pygame
        manager.process_events(event)

        # Verifica se o botão foi pressionado
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == botao:
                    # Recupera o texto da caixa de texto e imprime na tela
                    nome = caixa_texto.get_text()
                    print("Nome inserido:", nome)

        # Atualiza o gerenciador de eventos com o tempo
        manager.update(pygame.time.get_ticks() / 1000.0)

    # Desenha o fundo e os elementos do Pygame GUI na tela
    window_surface.fill((255, 255, 255))
    manager.draw_ui(window_surface)

    # Atualiza a janela do Pygame
    pygame.display.update()

# Encerra o Pygame
pygame.quit()