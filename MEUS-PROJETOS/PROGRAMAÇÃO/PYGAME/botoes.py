def button (msg, x,y,w,h,ic,ac):  #largura, altura, cor inativa e ativa
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    botao_clicado = False

    #desenhar um botão na tela
    if (x + w) > mouse [0] > x and (y + h) > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1:
            botao_clicado = True
            time.sleep(0.1)  #amem david delay para ignorar duplo clique
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    #para escrever no botão
    textSurf, TextRect = text_objects(msg, smallText)
    #para escrever no meio
    TextRect.center = ((x+(w/2), (y + (h/2))))
    screen.blit(textSurf, TextRect)

    return botao_clicado