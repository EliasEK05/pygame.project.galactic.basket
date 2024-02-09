import pygame

pygame.init()

#dimension de l'écran de jeu
ecran = pygame.display.set_mode((1000,700)) #pygame.FULLCREEN


horloge = pygame.time.Clock()


img = pygame.image.load("\prototype_jeu.jpg").convert_alpha()
img = pygame.transform.scale(img,(200, 100))
imge = img.get_rect()


while True:

    horloge.tick(60)
    pygame.display.update()

    ecran.blit(imge)

    # pour pouvoir utiliser les touches (à utiliser plus tard)
    pygame.event.get()


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False