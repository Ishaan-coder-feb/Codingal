import pygame
pygame.init()
display=pygame.display.set_mode((300,300))
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN: 
            print("A key has been pressed")
            if event.key == pygame.K_UP:
                print("The Up key had been pressed")
            elif event.key == pygame.K_DOWN:
                print("The Down key has been pressed")
            elif event.key == pygame.K_RIGHT:
                print("The Right key was pressed")
            elif event.key == pygame.K_LEFT: 
                print("The Left key was pressed")
            else:
                print("The Space key was pressed")
            

