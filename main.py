import pygame
pygame.init()

#Création de la fenetre
pygame.display.set_caption("Jeu de plateforme de test")
screen = pygame.display.set_mode((1080, 720))

# Arriere plan
background = pygame.image.load('assets/bg.jpg')

running = True

while running:

    #Appliquer arrière plan
    screen.blit(background, (0, -200))

    #Mettre a jour l'écran
    pygame.display.flip()


    # Si on ferme la fenetre
    for event in pygame.event.get():
        # Verification de l'event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()