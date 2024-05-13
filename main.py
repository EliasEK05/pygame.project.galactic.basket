
import pygame
import sys
from pygame.locals import *
import math

pygame.init()

# dimension de l'écran de jeu
ecran = pygame.display.set_mode((1000, 650))


def clock(timeremaining):
    # Calcul du temps restant en minutes et secondes
    minutes = timeremaining // 60
    seconds = timeremaining % 60

    # Définition de la police de caractères
    font = pygame.font.Font(None, 40)

    # Affichage du temps restant
    time_text = font.render(f"{minutes:02}:{seconds:02}", True, BLACK)
    ecran.blit(time_text, (900, 40))



pygame.init()

# dimension de l'écran de jeu
ecran = pygame.display.set_mode((1000, 650))

# Ajouter un titre à la fenêtre
pygame.display.set_caption('Galactic Basket')

horloge = pygame.time.Clock()

#Définition volume général
volume = 100

# Définition des constantes physiques :
GRAVITE = 9.81*5
REBONDISSEMENT = 0.6
vitesse_initial_x = 0
vitesse_initial_y = 0

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fond d'écran menu principal
img = pygame.image.load("image/menu_principal.jpg").convert_alpha()  # mieux manier l'image (moins pixelisé)
img = pygame.transform.scale(img, (1000, 650))
imge = img.get_rect()

# Fond d'écran paramètres
parametre = pygame.image.load("image/test_background.jpg").convert_alpha()
parametre = pygame.transform.scale(parametre, (1000, 750))

play = pygame.image.load("image/test_background.jpg").convert_alpha()
play = pygame.transform.scale(play, (1000, 700))

mode_1 = pygame.image.load("image/court.jpg").convert_alpha()
mode_1 = pygame.transform.scale(mode_1, (1000, 700))

mode_2 = pygame.image.load("image/court.jpg").convert_alpha()
mode_2 = pygame.transform.scale(mode_2, (1000, 700))

# slider pour le volume
class Slider:
    def __init__(self, pos, size, initial_val : float, min : int, max : int):
        self.pos = pos
        self.size = size

        self.slider_left_position = self.pos[0] - (size[0]//2)
        self.slider_right_position = self.pos[0] + (size[0]//2)
        self.slider_top_position = self.pos[1] - (size[1]//2)

        self.min = min
        self.max = max
        self.initial_position = 0

        self.slider_rectangle = pygame.Rect(self.slider_left_position, self.slider_top_position,self.slider_right_position, self.size[0], self.size[1])
        self.slider_button = pygame.Rect(self.slider_left_position + self.initial_position -5,
                                         self.slider_top_position, 30, self.size[1])
# bouton play
bouton_play = pygame.image.load("image/play_button.png").convert_alpha()
bouton_play = pygame.transform.scale(bouton_play, (250, 120))  # possibilité de changer la taille
bouton_clic_play = bouton_play.get_rect()
bouton_clic_play.topleft = (350, 390)
print(bouton_clic_play)

# bouton reglage
bouton_reglage = pygame.image.load("image/settings_button.png").convert_alpha()
bouton_reglage = pygame.transform.scale(bouton_reglage, (250, 120))  # possibilité de changer la taille
bouton_clic_reglage = bouton_reglage.get_rect()
bouton_clic_reglage.topleft = (350, 520)
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

# bouton balle 2
bouton_balle_2 = pygame.image.load("image/planet_ball.png").convert_alpha()
bouton_balle_2 = pygame.transform.scale(bouton_balle_2, (350, 350))
bouton_clic_balle_2 = bouton_balle_2.get_rect()
bouton_clic_balle_2.topleft = (500, 300)

# bouton balle météorite
bouton_balle_1 = pygame.image.load("image/meteor_ball.png").convert_alpha()
bouton_balle_1 = pygame.transform.scale(bouton_balle_1, (350, 350))
bouton_clic_balle_1 = bouton_balle_1.get_rect()
bouton_clic_balle_1.topleft = (150, 300)



# Définition de la police de caractères
font = pygame.font.Font(None, 36)

# Definition du ballon
ballon = pygame.image.load("image/meteor_ball.png").convert_alpha()
ballon = pygame.transform.scale(ballon, (100, 100))

# Position initial du ballon
pos_x_ballon, pos_y_ballon = 150, 425
pos_ballon = [pos_x_ballon, pos_y_ballon]
ballon_surface = ballon.get_rect(center=pos_ballon)



# Temps initial en secondes (1 minute)
time_remaining = 1800


continuer = True
tir = True
current_screen = "menu"  # Initial screen is the main menu


angle = 0

while continuer:

    horloge.tick(60)
    pygame.display.update()

    ecran.fill(0)

    if current_screen == "menu":  # ecran principal
        time_remaining = 1800
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

        ecran.blit(bouton_retour, bouton_clic_retour.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == K_UP:
                volume += 1
            elif event.type == K_DOWN:
                volume -= 1
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "menu"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "menu"




    elif current_screen == "play":  # ecran play

        ecran.blit(play, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        ecran.blit(bouton_reglage, (800, 20))
        ecran.blit(bouton_balle_1, bouton_clic_balle_1.topleft)
        ecran.blit(bouton_balle_2, bouton_clic_balle_2.topleft)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "menu"
                elif bouton_clic_balle_1.collidepoint(event.pos):
                    current_screen = "mode_1"
                elif bouton_clic_balle_2.collidepoint(event.pos):
                    current_screen = "mode_2"
                elif bouton_clic_reglage.collidepoint(event.pos):
                    current_screen = "settings"




    elif current_screen == "mode_1":
        ecran.blit(mode_1, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        début_jeu = pygame.time.get_ticks()
        font = pygame.font.Font(None,36)
        text_color = (0,0,0)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONDOWN:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "play"
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                pos_x_init, pos_y_init = event.pos
                if ballon_surface.collidepoint((pos_x_init, pos_y_init)):
                    print("Ceci est un ballon")
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                pos_x_fin, pos_y_fin = event.pos
                pos_x_init = pos_x_ballon
                pos_y_init =pos_y_ballon
                angle = math.atan2(pos_y_fin - pos_y_init, pos_x_fin - pos_x_init)
                tir = False
                vitesse_init_x = abs(pos_x_fin - pos_x_init) * math.cos(angle)
                vitesse_init_y = abs(pos_y_fin - pos_y_init)* math.sin(angle)

                if vitesse_init_x > 200:
                    vitesse_init_x = 200


            # Permet de replacer le ballon à sa position initial.
            elif event.type == KEYUP:
                tir = True
                pos_x_ballon, pos_y_ballon = 150, 425
                ballon_surface.center = pos_ballon
        clock(time_remaining)

        time_remaining -= 1
        if time_remaining == 0:
            current_screen = "menu"

        if tir == False:

            time_elapsed = horloge.tick(60) / 100
            pos_x_ballon += vitesse_init_x * time_elapsed
            pos_y_ballon += vitesse_init_y * time_elapsed + 0.5 * GRAVITE * time_elapsed ** 2
            vitesse_init_y += GRAVITE * time_elapsed
            # permet rebond sur le sol
            if pos_y_ballon > 600:
                pos_y_ballon = 600
                vitesse_init_y = -vitesse_init_y * REBONDISSEMENT

            ballon_surface.center = (pos_x_ballon, pos_y_ballon)

        # rotation de la balle
        rotated_ball = pygame.transform.rotate(ballon, angle)
        angle -= 2
        ecran.blit(rotated_ball, ballon_surface)

        pygame.display.flip()

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
