import pygame
from projectile import Projectile

#Classe pour le joueur avec ses caractéristiques
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3.5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/ninja.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else: #Si le joueur n'a plus de vie
            self.game.game_over()


    
    def update_health_bar(self, surface):
        #dessin de la barre de vie
        pygame.draw.rect(surface, (101, 101, 101), [self.rect.x + 60, self.rect.y - 5, self.max_health, 5])
        pygame.draw.rect(surface, (88, 243, 30), [self.rect.x + 60, self.rect.y - 5, self.health, 5])

    def launch_projectile(self):
        #Nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        #Si le joueur n'entre pas en collisoin avec monstre ou entité
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity