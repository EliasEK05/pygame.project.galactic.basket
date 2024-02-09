import pygame

pygame.init()

#dimension de l'écran de jeu
ecran = pygame.display.set_mode((1000,700))

horloge = pygame.time.Clock()


while True:

    horloge.tick(60)
    pygame.display.update()


    # pour pouvoir utiliser les touches (à utiliser plus tard)
    pygame.event.get()