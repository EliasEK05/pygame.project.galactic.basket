import pygame
import sys
from pygame.locals import *

def clock(time_remaining_):
    # Calcul du temps restant en minutes et secondes
    minutes = time_remaining_ // 60
    seconds = time_remaining_ % 60

    # Définition de la police de caractères
    font = pygame.font.Font(None, 36)

    # Affichage du temps restant
    time_text = font.render(f"{minutes:02}:{seconds:02}", True, WHITE)
    ecran.blit(time_text, (150, 40))






pygame.init()

#dimension de l'écran de jeu
ecran = pygame .display.set_mode((1000,700)) #pygame.FULLCREEN

# Ajouter un titre à la fenêtre
pygame.display.set_caption('Galctic Basket')

horloge = pygame.time.Clock()


# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

terrain = pygame.image.load("image/court.jpg").convert_alpha()
terrain = pygame.transform.scale(terrain,(1000, 700))

ballon = pygame.image.load("image/ballon.png").convert_alpha()
ballon = pygame.transform.scale(ballon, (100, 100))
ballon_surface = ballon.get_rect()
ballon_surface.topleft = (100, 375)

img = pygame.image.load("image/prototype_jeu.jpg").convert_alpha()   #mieux manier l'image (moins pixelisé)
img = pygame.transform.scale(img,(900, 500))

bouton_play = pygame.image.load("image/bouton_play.png").convert_alpha()
bouton_play = pygame.transform.scale(bouton_play, (360, 360))  #possibilité de changer la taille
bouton_clic = bouton_play.get_rect()
bouton_clic.topleft = (330, 300)

# Définition de la police de caractères
font = pygame.font.Font(None, 36)

# Temps initial en secondes (1 minute)
time_remaining = 60

continuer = True


while continuer:

    horloge.tick(60)

    # Effacer l'écran
    ecran.fill(BLACK)

    #affichage de l'image test
    ecran.blit(img, (50, 80))
    ecran.blit(bouton_play, (bouton_clic.topleft))


    # pour pouvoir utiliser les touches (à utiliser plus tard)
    pygame.event.get()

    clock(time_remaining)

    # Mettre à jour l'écran à mettre IMPERATIVEMENT apres l'appel de la fonction pas avant
    pygame.display.flip()

    # Réduire le temps restant de 1 seconde
    pygame.time.wait(1000)
    time_remaining -= 1

    # Si le temps est écoulé, arrêter le minuteur
    if time_remaining < 0:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            if bouton_clic.collidepoint(event.pos):
                ecran.fill(BLACK)




                while continuer:

                    horloge.tick(60)
                    pygame.display.flip()
                    ecran.blit(terrain, (0, 0))
                    ecran.blit(ballon, (100, 375))


                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            continuer = False
                        elif event.type == MOUSEBUTTONUP and event.button == 1:
                            if ballon_surface.collidepoint(event.pos):
                                print("ceci est un ballon")



# Quitter Pygame
pygame.quit()
sys.exit()
