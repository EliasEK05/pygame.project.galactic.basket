import pygame
import sys
from pygame.locals import *

pygame.init()

# dimension de l'écran de jeu
ecran = pygame.display.set_mode((1000, 650))  # pygame.FULLCREEN

# Ajouter un titre à la fenêtre
pygame.display.set_caption('Galactic Basket')

horloge = pygame.time.Clock()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

img = pygame.image.load("image/menu_principal.jpg").convert_alpha()  # mieux manier l'image (moins pixelisé)
img = pygame.transform.scale(img, (1000, 650))
imge = img.get_rect()

parametre = pygame.image.load("image/bouton_play.png").convert_alpha()
parametre = pygame.transform.scale(parametre, (1000, 750))

play = pygame.image.load("image/test_background.jpg").convert_alpha()
play = pygame.transform.scale(play, (1000, 700))

mode_1 = pygame.image.load("image/court.jpg").convert_alpha()
mode_1 = pygame.transform.scale(mode_1, (1000, 700))

mode_2 = pygame.image.load("image/court.jpg").convert_alpha()
mode_2 = pygame.transform.scale(mode_2, (1000, 700))

# bouton play
bouton_play = pygame.image.load("image/play_button.png").convert_alpha()
bouton_play = pygame.transform.scale(bouton_play, (200, 200))  # possibilité de changer la taille
bouton_clic_play = bouton_play.get_rect()
bouton_clic_play.topleft = (400, 420)
print(bouton_clic_play)

# bouton reglage

bouton_reglage = pygame.image.load("image/settings_button.png").convert_alpha()
bouton_reglage = pygame.transform.scale(bouton_reglage, (200, 200))  # possibilité de changer la taille
bouton_clic_reglage = bouton_reglage.get_rect()
bouton_clic_reglage.topleft = (400, 500)
print(bouton_clic_reglage)

# bouton on
bouton_on = pygame.image.load("image/Untitled_Artwork (1).png").convert_alpha()
bouton_on = pygame.transform.scale(bouton_on, (150, 150))  # possibilité de changer la taille
bouton_clic_on = bouton_on.get_rect()
bouton_clic_on.topleft = (300, 300)
print(bouton_clic_on)

# bouton off
bouton_off = pygame.image.load("image/ballon.png").convert_alpha()
bouton_off = pygame.transform.scale(bouton_off, (150, 150))  # possibilité de changer la taille
bouton_clic_off = bouton_off.get_rect()
bouton_clic_off.topleft = (600, 300)
print(bouton_clic_off)

# bouton retour
bouton_retour = pygame.image.load("image/back_button.png").convert_alpha()
bouton_retour = pygame.transform.scale(bouton_retour, (150, 150))
bouton_clic_retour = bouton_retour.get_rect()
bouton_clic_retour.topleft = (20, 20)
print(bouton_clic_retour)

# bouton mode 1
bouton_mode_1 = pygame.image.load("image/Untitled_Artwork (1).png").convert_alpha()
bouton_mode_1 = pygame.transform.scale(bouton_mode_1, (350, 100))
bouton_clic_mode_1 = bouton_mode_1.get_rect()
bouton_clic_mode_1.topleft = (330, 200)
print(bouton_clic_mode_1)

# bouton mode 2
bouton_mode_2 = pygame.image.load("image/Untitled_Artwork (1).png").convert_alpha()
bouton_mode_2 = pygame.transform.scale(bouton_mode_2, (350, 100))
bouton_clic_mode_2 = bouton_mode_2.get_rect()
bouton_clic_mode_2.topleft = (330, 400)
print(bouton_clic_mode_2)

# Définition de la police de caractères
font = pygame.font.Font(None, 36)

# Temps initial en secondes (1 minute)
time_remaining = 60

continuer = True
current_screen = "menu"  # Initial screen is the main menu

while continuer:

    horloge.tick(60)
    pygame.display.update()

    ecran.fill(0)

    if current_screen == "menu":  # ecran principal
        ecran.blit(img, (0, 0))
        ecran.blit(bouton_play, bouton_clic_play.topleft)
        ecran.blit(bouton_reglage, bouton_clic_reglage)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_play.collidepoint(event.pos):
                    current_screen = "play"
                elif bouton_clic_reglage.collidepoint(event.pos):
                    current_screen = "settings"



    elif current_screen == "settings":  # ecran parametre
        ecran.blit(parametre, (0, 0))
        ecran.blit(bouton_on, bouton_clic_on.topleft)
        ecran.blit(bouton_off, bouton_clic_off.topleft)
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "menu"



    elif current_screen == "play":  # ecran play
        ecran.blit(play, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        ecran.blit(bouton_mode_1, bouton_clic_mode_1.topleft)
        ecran.blit(bouton_mode_2, bouton_clic_mode_2.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "menu"
                elif bouton_clic_mode_1.collidepoint(event.pos):
                    current_screen = "mode_1"
                elif bouton_clic_mode_2.collidepoint(event.pos):
                    current_screen = "mode_2"


    elif current_screen == "mode_1":
        ecran.blit(mode_1, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "play"

    elif current_screen == "mode_2":
        ecran.blit(mode_2, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "play"

pygame.quit()
sys.exit()

