import pygame
import random

#Classe qui va gerer la notion de monstre

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attaque = 3
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
        #dessin de la barre de vie
        pygame.draw.rect(surface, (101, 101, 101), [self.rect.x + 20, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (88, 243, 30), [self.rect.x + 20, self.rect.y - 20, self.health, 5])
        


    def forward(self):
        #Le déplacement se fait uniquement s'il n'y a pas de collisions
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        #Si le monstre touche le joueur, infliger des dégats au joueur
        else:
            self.game.player.damage(self.attaque)