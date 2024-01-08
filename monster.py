import pygame

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
        self.rect.x = 850
        self.rect.y = 540
        self.velocity = 3

    def forward(self):
        #Le déplacement se fait uniquement s'il n'y a pas de collisions
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity