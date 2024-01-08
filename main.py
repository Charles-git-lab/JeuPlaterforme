import pygame
from game import Game
from player import Player

pygame.init()


#Création de la fenetre
pygame.display.set_caption("Test de jeu de plateforme")
screen = pygame.display.set_mode((1080, 720))

# Arriere plan
background = pygame.image.load('assets/background.png')

#Charger le jeu
game = Game()

#Charger le joueur
player = Player(game)

running = True

while running:

    #Appliquer arrière plan
    screen.blit(background, (0, -170))

    #Appliquer image joueur
    screen.blit(game.player.image, game.player.rect)


    #Actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)

    #Recuperer projectile du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #Recuperer monstres
    for monster in game.all_monster:
        monster.forward()
        monster.update_health_bar(screen)

    #Appliquer images du groupe de projectile
    game.player.all_projectiles.draw(screen)

    #Appliquer image au groupe de monstre
    game.all_monster.draw(screen)

    #Verifier si le joueur veut aller a gauche ou droite + délimitation des bordures
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

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
