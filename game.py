import pygame
from player import Player
from monster import Monster

#Classe qui représente le jeu
class Game:

    def __init__(self):
        #définir si le jeu à commencé ou non
        self.is_playing = False
        #Generer le joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #groupe de monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monsters()
        self.spawn_monsters()

    def game_over(self):#Remettre le jeu à 0
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        #Appliquer image joueur
        screen.blit(self.player.image, self.player.rect)


        #Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        #Recuperer projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #Recuperer monstres
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)

        #Appliquer images du groupe de projectile
        self.player.all_projectiles.draw(screen)

        #Appliquer image au groupe de monstre
        self.all_monster.draw(screen)

        #Verifier si le joueur veut aller a gauche ou droite + délimitation des bordures
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monsters(self):
        monster = Monster(self)
        self.all_monster.add(monster)