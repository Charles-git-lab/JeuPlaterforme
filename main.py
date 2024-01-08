import pygame
import math
from game import Game
from player import Player

pygame.init()


#Création de la fenetre
pygame.display.set_caption("Test de jeu de plateforme")
screen = pygame.display.set_mode((1509,850))

# Arriere plan
background = pygame.image.load('assets/background.png')

"""#Charger la bannière
banner = pygame.image.load('assets/accueil.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /4)"""

#Bouton pour lancer la partie
play_button = pygame.image.load('assets/bouton.png')
play_button = pygame.transform.scale(play_button, (204, 76))
play_button_rect = play_button.get_rect()
play_button_rect.x = 655
play_button_rect.y = math.ceil(screen.get_height() /2)
#Charger le jeu
game = Game()

#Charger le joueur
player = Player(game)

running = True

while running:

    #Appliquer arrière plan
    screen.blit(background, (0, -170))

    #Verfier si le jeu a commencé ou non
    if game.is_playing:
        #Si oui, les actions peuvent se faire
        game.update(screen)
    #Si le jeu n'a pas commencé, afficher menu d'accueil
    else:
        screen.blit(play_button, play_button_rect)
        """screen.blit(banner, banner_rect)"""

    #Mettre a jour l'écran
    pygame.display.flip()


    # Si on ferme la fenetre
    for event in pygame.event.get():
        # Verification de l'event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        #Detecter les appuis de touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #Detecter si la touche espace est appuyé (pour projectile)
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Verifier si la souris est sur le bouton de démarrage
            if play_button_rect.collidepoint(event.pos):
                #Le jeu se lance
                game.start()