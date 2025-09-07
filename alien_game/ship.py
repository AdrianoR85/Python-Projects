import pygame as pg

class Ship:
  def __init__(self, game):
    self.main_screen = game.screen
    self.settings  = game.settings

    self.image = pg.image.load("assets/ship.bmp")
    self.rect = self.image.get_rect()

    self.screen_rect = self.main_screen.get_rect()
    self.rect.midbottom = self.screen_rect.midbottom

    self.moving_right = False
    self.moving_left = False

    self.x = float(self.rect.x)
  
  def moving_ship(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
    elif self.moving_left and self.rect.left > 0:
      self.x -= self.settings.ship_speed
    
    self.rect.x = int(self.x)
  
  def draw_ship(self):
    self.main_screen.blit(self.image, self.rect)