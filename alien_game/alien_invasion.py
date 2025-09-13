import sys
import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:

  def __init__(self) -> None:
    pg.init()
    self.clock = pg.time.Clock()
    self.settings = Settings()
    self.screen = pg.display.set_mode((self.settings.width, self.settings.height))
    pg.display.set_caption("Alien Invasion")

    self.ship = Ship(self)
    self.bullets = pg.sprite.Group()
    self.aliens = pg.sprite.Group()

    self._create_fleet()

  def run_game(self):
    while True:
      self._check_event()
      self.ship.moving_ship()
      self._update_bullet()
      self._update_screen()
      self.clock.tick(self.settings.fps)

  def _check_event(self):
    for event in pg.event.get():
        if event.type == pg.QUIT:
          sys.exit()
        elif event.type == pg.KEYDOWN:
          self._check_keydow_event(event)
        elif event.type == pg.KEYUP:
          self._check_keyup_event(event)


  def _check_keydow_event(self, event):
    if event.key == pg.K_RIGHT:
      self.ship.moving_right = True
    elif event.key == pg.K_LEFT:
      self.ship.moving_left = True
    elif event.key == pg.K_q:
      sys.exit()
    elif event.key == pg.K_SPACE:
      self._fire_bullet()


  def _check_keyup_event(self, event):
    if event.key == pg.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pg.K_LEFT:
      self.ship.moving_left = False


  def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)

  def _create_fleet(self):
    """Create the fleet of aliens."""
    # Create an alien and keep adding aliens until there's no room left.
    # Spacing between aliens is one alien width and one alien height.
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size

    current_x, current_y = alien_width, alien_height
    while current_y < (self.settings.height - 4 * alien_height):
      while current_x < (self.settings.width - 2 * alien_width):
        self._create_alien(current_x, current_y)
        current_x += 2 * alien_width

      # Finished a row; reset x value, and increment y value.
      current_x = alien_width
      current_y += 1.5 * alien_height
  

  def _create_alien(self, pos_x, pos_y):
    new_alien = Alien(self)
    new_alien.x = pos_x
    new_alien.rect.x = pos_x
    new_alien.rect.y = pos_y
    self.aliens.add(new_alien) 

  def _update_bullet(self):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    self.bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)

  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    self.ship.draw_ship()
    self.aliens.draw(self.screen)
    pg.display.flip()
    

if __name__ == "__main__":
  game = AlienInvasion()
  game.run_game()