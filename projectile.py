import pygame


#Classe qui va gerer le projectile
class Projectile(pygame.sprite.Sprite):

    #Constructeur de la classe proj
    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('assets/shuriken.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 150
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0

    #Faire tourner le projectile
    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    #Supprimer projectile
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #Verifier si le projectile touche un monstre
        if self.player.game.check_collision(self, self.player.game.all_monster):
            #suppression du projectile après avoir toucher le monstre
            self.remove()


        #verifier si le projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            #Supprimer projectile
            self.remove()      