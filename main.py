import pygame
from game import Game
from player import Player

pygame.init()


#Création de la fenetre
pygame.display.set_caption("Test de jeu de plateforme")
screen = pygame.display.set_mode((1080, 720))

# Arriere plan
background = pygame.image.load('assets/bg.jpg')

#Charger le jeu
game = Game()

#Charger le joueur
player = Player()

running = True

while running:

    #Appliquer arrière plan
    screen.blit(background, (0, -200))

    #Appliquer image joueur
    screen.blit(game.player.image, game.player.rect)
    #Mettre a jour l'écran
    pygame.display.flip()


    # Si on ferme la fenetre
    for event in pygame.event.get():
        # Verification de l'event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
