import pygame
import sys


pygame.init()

#dimension de l'écran de jeu
ecran = pygame.display.set_mode((1000,700)) #pygame.FULLCREEN

# Ajouter un titre à la fenêtre
pygame.display.set_caption('Galctic Basket')

horloge = pygame.time.Clock()


# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



img = pygame.image.load("image/prototype_jeu.jpg").convert_alpha()
img = pygame.transform.scale(img,(900, 500))
imge = img.get_rect()


# Définition de la police de caractères
font = pygame.font.Font(None, 36)

# Temps initial en secondes (1 minute)
time_remaining = 60




while True:

    horloge.tick(60)
    pygame.display.update()


    # Effacer l'écran
    ecran.fill(BLACK)

    #affichage de l'image test
    ecran.blit(img, (50, 80))

    # pour pouvoir utiliser les touches (à utiliser plus tard)
    pygame.event.get()

    # Calcul du temps restant en minutes et secondes
    minutes = time_remaining // 60
    seconds = time_remaining % 60


    # Affichage du temps restant
    time_text = font.render(f"{minutes:02}:{seconds:02}", True, WHITE)
    ecran.blit(time_text, (150, 40))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Réduire le temps restant de 1 seconde
    pygame.time.wait(1000)
    time_remaining -= 1

    # Si le temps est écoulé, arrêter le minuteur
    if time_remaining < 0:
        break

    #ecran.blit(time_text, (950, 40))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False


# Quitter Pygame
pygame.quit()
sys.exit()