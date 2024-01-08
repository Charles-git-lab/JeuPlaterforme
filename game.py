import pygame
from player import Player
from monster import Monster

#Classe qui représente le jeu
class Game:

    def __init__(self):
        #Generer le joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #groupe de monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monsters()
        self.spawn_monsters()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monsters(self):
        monster = Monster(self)
        self.all_monster.add(monster)