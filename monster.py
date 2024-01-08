import pygame
import random

#Classe qui va gerer la notion de monstre

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attaque = 5
        self.image = pygame.image.load('assets/monstre.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800 + random.randint(50, 300)
        self.rect.y = 540
        self.velocity = random.randint(2, 3)

    def damage(self, amount):
        # Infliger les dégats
        self.health -= amount

        #Verifier si les points de vie sont inférieur ou égal à 0
        if self.health <= 0:
            # Disparition et réaparition du monstre après sa mort
            self.rect.x = 800 + random.randint(50, 300)
            self.velocity = random.randint(2, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        #Couleur de la jauge de vie
        bar_color = (88, 243, 30)
        #Définir couleur arrière plan barre de vie
        back_bar_color = (101, 101, 101)

        #Position de la jauge de vie et ses dimensions
        bar_position = [self.rect.x + 20, self.rect.y - 20, self.health, 5]

        #Position de l'arrière plan de la jauge de vie
        back_bar_position = [self.rect.x + 20, self.rect.y - 20, self.max_health, 5]
        #dessin de la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        


    def forward(self):
        #Le déplacement se fait uniquement s'il n'y a pas de collisions
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity