import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
  """A class to manage bullets fired from the ship."""

  def __init__(self, game) -> None:
    """Create a bullet object at the ship's current position."""
    super().__init__()
    self.main_screen = game.screen
    self.settings = game.settings
    self.color = self.settings.bullet_color

    # Create a bullet rect at (0, 0) and then set correct position.
    self.rect = pg.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
    self.rect.midtop = game.ship.rect.midtop

    # Store the bullet's position as a float.
    self.y = float(self.rect.y)

  def update(self):
    """Move the bullet up the screen."""
    # Update the exact position of the bullet.
    self.y -= self.settings.bullet_speed
    # Update the rect position.
    self.rect.y = self.y

  def draw_bullet(self):
    pg.draw.rect(self.main_screen, self.color, self.rect)