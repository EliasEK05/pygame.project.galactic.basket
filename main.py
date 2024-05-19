import pygame
import sys
from pygame.locals import *
import math
import random

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


# son :
pygame.mixer.init()
# son principal :
son_principal = pygame.mixer.Sound("son/son_principal.mp3")
# son mode 1 :
son_mode_1 = pygame.mixer.Sound("son/son_mode_1.wav")
#son mode 2 :
son_mode_2 = pygame.mixer.Sound("son/son_mode_2.mp3")
#son score :
son_score0 = pygame.mixer.Sound("son/score_0.mp3")
son_score1 = pygame.mixer.Sound("son/score_1.mp3")
son_score2 = pygame.mixer.Sound("son/score_2.mp3")
son_score3 = pygame.mixer.Sound("son/score_3.mp3")
son_score4 = pygame.mixer.Sound("son/score_4.mp3")
liste_son = [son_score0,son_score1,son_score2,son_score3,son_score4]

# état du son :
etat_son = True

#arrêt du son:
def arret_son():
    pygame.mixer.stop()
# Fonction pour basculer l'état du son (activé/désactivé)
def play_son(nom_son, etat):
    if etat == True:
        if not pygame.mixer.get_busy():  # Ajout de cette ligne
            nom_son.play(loops=-1)
    else:
        pygame.mixer.stop()

def jouer_son_aleatoire():
    son_aleatoire = random.choice(liste_son)
    son_aleatoire.play()


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
parametre = pygame.transform.scale(parametre, (1000, 700))

play = pygame.image.load("image/mode_menu.png").convert_alpha()
play = pygame.transform.scale(play, (1000, 700))

endgame = pygame.image.load("image/end_of_game.png").convert_alpha()
endgame = pygame.transform.scale(endgame, (1000, 700))

mode_2 = pygame.image.load("image/court_mode_2.png").convert_alpha()
mode_2 = pygame.transform.scale(mode_2, (1000, 700))

mode_1 = pygame.image.load("image/court_mode_1.png").convert_alpha()
mode_1 = pygame.transform.scale(mode_1, (1000, 700))


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
bouton_on = pygame.image.load("image/volume_on.png").convert_alpha()
bouton_on = pygame.transform.scale(bouton_on, (150, 150))  # possibilité de changer la taille
bouton_clic_on = bouton_on.get_rect()
bouton_clic_on.topleft = (300, 300)
print(bouton_clic_on)

# bouton off
bouton_off = pygame.image.load("image/volume_off.png").convert_alpha()
bouton_off = pygame.transform.scale(bouton_off, (150, 150))  # possibilité de changer la taille
bouton_clic_off = bouton_off.get_rect()
bouton_clic_off.topleft = (600, 300)
print(bouton_clic_off)

# bouton retour
bouton_retour = pygame.image.load("image/back_button.png").convert_alpha()
bouton_retour = pygame.transform.scale(bouton_retour, (180, 180))
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

# Definition du ballon météorite
ballon_1 = pygame.image.load("image/meteor_ball.png").convert_alpha()
ballon_1 = pygame.transform.scale(ballon_1, (100, 100))

# Definition du ballon planete
ballon_2 = pygame.image.load("image/planet_ball.png").convert_alpha()
ballon_2 =pygame.transform.scale(ballon_2,(100,100))

# Position initial du ballon_métorite_1
pos_x_ballon_1, pos_y_ballon_1 = 150, 425
pos_ballon_1 = [pos_x_ballon_1, pos_y_ballon_1]
ballon_surface_1 = ballon_1.get_rect(center=pos_ballon_1)

#Position inital ballon_planet_2
pos_x_ballon_2, pos_y_ballon_2 = 150, 425
pos_ballon_2 = [pos_x_ballon_2, pos_y_ballon_2]
ballon_surface_2 = ballon_2.get_rect(center=pos_ballon_2)


# hitbox
hitbox = pygame.image.load("image/hitbox.png").convert_alpha()
hitbox = pygame.transform.scale(hitbox, (60, 60))
hitbox_clic = hitbox.get_rect()
hitbox_clic.topleft = (890, 360)

# Temps initial en secondes (1 minute)
time_remaining = 1800


continuer = True
tir = False
current_screen = "menu"  # Initial screen is the main menu


angle_img_1 = 0
angle_img_2 = 0


# définition du score
score = 0000

#hitbox = pygame.Rect(790, 190, 20, 20)

while continuer:

    horloge.tick(60)
    pygame.display.update()

    ecran.fill(0)

    if current_screen == "menu":  # ecran principal
        time_remaining = 1800
        ecran.blit(img, (0, 0))
        ecran.blit(bouton_play, bouton_clic_play.topleft)
        ecran.blit(bouton_reglage, bouton_clic_reglage)
        play_son(son_principal, etat_son)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_play.collidepoint(event.pos):
                    current_screen = "play"
                    arret_son()
                elif bouton_clic_reglage.collidepoint(event.pos):
                    current_screen = "settings"




    elif current_screen == "settings":  # ecran parametre

        ecran.blit(parametre, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        ecran.blit(bouton_on, bouton_clic_on.topleft)
        ecran.blit(bouton_off, bouton_clic_off.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONUP:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "menu"
                elif bouton_clic_on.collidepoint(event.pos):
                    etat_son = True
                    play_son(son_principal, etat_son)
                elif bouton_clic_off.collidepoint(event.pos):
                    etat_son = False
                    play_son(son_principal, etat_son)




    elif current_screen == "play":  # ecran play

        ecran.blit(play, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        ecran.blit(bouton_balle_1, bouton_clic_balle_1.topleft)
        ecran.blit(bouton_balle_2, bouton_clic_balle_2.topleft)
        play_son(son_principal,etat_son)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONDOWN:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "menu"
                elif bouton_clic_balle_1.collidepoint(event.pos):
                    current_screen = "mode_1"
                    arret_son()
                elif bouton_clic_balle_2.collidepoint(event.pos):
                    current_screen = "mode_2"
                    arret_son()




    elif current_screen == "endgame":
        ecran.blit(endgame, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour)
        arial_font = pygame.font.SysFont("Bubblegum", 100, True, False)
        texte_score = arial_font.render(f"{score} ", False, (27, 76, 212))
        ecran.blit(texte_score, (600, 375))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONDOWN:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "play"
                    time_remaining = 1800


    elif current_screen == "mode_1":
        ecran.blit(mode_1, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        début_jeu = pygame.time.get_ticks()
        font = pygame.font.Font(None,36)
        text_color = (0,0,0)
        play_son(son_mode_1,etat_son)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONDOWN:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "play"
                    arret_son()
                    tir = False
                    pos_x_ballon_1,pos_y_ballon_1 = 150,425
                    ballon_surface_1.center = pos_ballon_1
                    time_remaining = 1800
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                pos_x_fin_1, pos_y_fin_1 = event.pos
                pos_x_init_1 = pos_x_ballon_1
                pos_y_init_1 =pos_y_ballon_1
                angle_1 = math.atan2(pos_y_fin_1 - pos_y_init_1, pos_x_fin_1 - pos_x_init_1)
                tir = True
                vitesse_init_x_1 = abs(pos_x_fin_1 - pos_x_init_1) * math.cos(angle_1)
                vitesse_init_y_1 = abs(pos_y_fin_1 - pos_y_init_1)* math.sin(angle_1)

                if vitesse_init_x_1 > 200:
                    vitesse_init_x_1 = 200


            # Permet de replacer le ballon à sa position initial.
            elif event.type == KEYUP:
                tir = False
                pos_x_ballon_1, pos_y_ballon_1 = 150, 425
                ballon_surface_1.center = pos_ballon_1
        clock(time_remaining)

        time_remaining -= 1
        if time_remaining == 0:
            score = 0000
            current_screen = "menu"
            current_screen = "endgame"
            arret_son()

        if tir == True:

            time_elapsed = horloge.tick(60) / 100
            pos_x_ballon_1 += vitesse_init_x_1 * time_elapsed
            pos_y_ballon_1 += vitesse_init_y_1 * time_elapsed + 0.5 * GRAVITE * time_elapsed ** 2
            vitesse_init_y_1 += GRAVITE * time_elapsed
            # permet rebond sur le sol
            if pos_y_ballon_1 > 600:
                pos_y_ballon_1 = 600
                vitesse_init_y_1 = -vitesse_init_y_1 * REBONDISSEMENT

            ballon_surface_1.center = (pos_x_ballon_1, pos_y_ballon_1)



        # texte pour le score
        couleur1 = (226, 216, 12)
        arial_font = pygame.font.SysFont("Bubblegum", 40, True, False)
        texte_ = arial_font.render(f"Score: {score} ", False, couleur1)

        ecran.blit(texte_, (250, 50))

        if (pos_x_ballon_1 > 990) and (pos_x_ballon_1 < 1100):

            if pos_y_ballon_1 < 450 and pos_y_ballon_1 > 150:

                pos_x_ballon_1 = 980
                vitesse_init_x_1 = -vitesse_init_x_1 * REBONDISSEMENT

        # quand la balle touche le filet
        if pos_x_ballon_1 > 795 and pos_x_ballon_1 > 820:
            if pos_y_ballon_1 > 360 and pos_y_ballon_1 < 470 :
                vitesse_init_x_1 = -vitesse_init_x_1 * REBONDISSEMENT



        # quand la balle est dans le panier
        if (pos_x_ballon_1 > 890 and pos_x_ballon_1 < 950) and (pos_y_ballon_1 > 380 and pos_y_ballon_1 < 400) :

            # imcrémentation du score quand la balle rentre dans le panier
            score += 100




        # rotation de la balle
        rotated_ball_1 = pygame.transform.rotate(ballon_1, angle_img_1)
        angle_img_1 -= 2
        ecran.blit(rotated_ball_1, ballon_surface_1)



    elif current_screen == "mode_2":
        ecran.blit(mode_2, (0, 0))
        ecran.blit(bouton_retour, bouton_clic_retour.topleft)
        play_son(son_mode_2,etat_son)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == MOUSEBUTTONDOWN:
                if bouton_clic_retour.collidepoint(event.pos):
                    current_screen = "play"
                    arret_son()
                    tir = False
                    pos_x_ballon_2, pos_y_ballon_2 = 150, 425
                    ballon_surface_2.center = pos_ballon_2
                    time_remaining = 1800
            elif event.type == MOUSEBUTTONUP and event.button == 3:
                pos_x_fin_2, pos_y_fin_2 = event.pos
                pos_x_init_2 = pos_x_ballon_2
                pos_y_init_2 = pos_y_ballon_2
                angle_2 = math.atan2(pos_y_fin_2 - pos_y_init_2, pos_x_fin_2 - pos_x_init_2)
                tir = True
                vitesse_init_x_2 = abs(pos_x_fin_2 - pos_x_init_2) * math.cos(angle_2)
                vitesse_init_y_2 = abs(pos_y_fin_2 - pos_y_init_2) * math.sin(angle_2)

                if vitesse_init_x_2 > 200:
                    vitesse_init_x_2 = 200


            # Permet de replacer le ballon à sa position initial.
            elif event.type == KEYUP:
                tir = False
                pos_x_ballon_2, pos_y_ballon_2 = 150, 425
                ballon_surface_2.center = pos_ballon_2
        clock(time_remaining)

        time_remaining -= 1
        if time_remaining == 0:
            current_screen = "endgame"
            score = 0000
            current_screen = "menu"
            arret_son()

        if tir == True:

            time_elapsed = horloge.tick(60) / 100
            pos_x_ballon_2 += vitesse_init_x_2 * time_elapsed
            pos_y_ballon_2 += vitesse_init_y_2 * time_elapsed + 0.5 * GRAVITE * time_elapsed ** 2
            vitesse_init_y_2 += GRAVITE * time_elapsed
            # permet rebond sur le sol
            if pos_y_ballon_2 > 600:
                pos_y_ballon_2 = 600
                vitesse_init_y_2 = -vitesse_init_y_2 * REBONDISSEMENT

            ballon_surface_2.center = (pos_x_ballon_2, pos_y_ballon_2)

        # rotation de la balle
        rotated_ball_2 = pygame.transform.rotate(ballon_2, angle_img_2)
        angle_img_2 -= 2
        ecran.blit(rotated_ball_2, ballon_surface_2)

        pygame.display.flip()

pygame.quit()
sys.exit()
