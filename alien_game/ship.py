import pygame as pg

class Ship:
  def __init__(self, game):
    """Initialize the ship and set its starting position."""
    self.main_screen = game.screen
    self.settings = game.settings
    self.screen_rect = game.screen.get_rect()

    # Load the ship image and get its rect.
    self.image = pg.image.load('assets/ship.bmp')
    self.rect = self.image.get_rect()

    # Start each new ship at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom

    # Store a float for the ship's exact horizontal position.
    self.x = float(self.rect.x)

    # Movement flags; start with a ship that's not moving.
    self.moving_right = False
    self.moving_left = False

  
  def center_ship(self):
    """Center the ship on the screen."""
    self.rect.midbottom = self.screen_rect.midbottom
    self.x = float(self.rect.x)

  def moving_ship(self):
    """Update the ship's position based on movement flags."""
     # Update the ship's x value, not the rect.
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.x += self.settings.ship_speed
    if self.moving_left and self.rect.left > 0:
        self.x -= self.settings.ship_speed
        
    # Update rect object from self.x.
    self.rect.x = self.x # type: ignore
  
  def draw_ship(self):
   """Draw the ship at its current location."""
   self.main_screen.blit(self.image, self.rect)