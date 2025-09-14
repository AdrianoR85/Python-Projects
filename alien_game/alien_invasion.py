import sys
from time import sleep

import pygame as pg

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stat import GameStats


class AlienInvasion:

  def __init__(self) -> None:
    pg.init()
    self.clock = pg.time.Clock()
    self.settings = Settings()
    self.screen = pg.display.set_mode((self.settings.width, self.settings.height))
    pg.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    self.stats = GameStats(self)

    self.ship = Ship(self)
    self.bullets = pg.sprite.Group()
    self.aliens = pg.sprite.Group()

    self._create_fleet()

    # Start Alien Invasion in an active state.
    self.game_active = True

  def run_game(self):
    while True:
      self._check_event()

      if self.game_active:
        self.ship.moving_ship()
        self._update_bullet()
        self._update_aliens()
        
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


  def _check_fleet_edges(self):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in self.aliens.sprites():
      if alien.check_edges():
        self._change_fleet_direction()
        break


  def _change_fleet_direction(self):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in self.aliens.sprites():
      alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1


  def _check_bullet_alien_collisions(self):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pg.sprite.groupcollide(self.bullets, self.aliens, True, True)

    if not self.aliens:
      # Destroy existing bullets and create new fleet.
      self.bullets.empty()
      self._create_fleet()
      

  def _ship_hit(self):
    """Respond to the ship being hit by an alien."""
    if self.stats.ships_left > 0:
      # Decrement ships_left.
      self.stats.ships_left -= 1

      # Get rid of any remaining bullets and aliens.
      self.bullets.empty()
      self.aliens.empty()

      # Create a new fleet and center the ship.
      self._create_fleet()
      self.ship.center_ship()

      # Pause.
      sleep(0.5)
    else:
      self.game_active = False

  
  def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

  def _check_aliens_bottom(self):
    """Check if any aliens have reached the bottom of the screen."""
    for alien in self.aliens.sprites():
      if alien.rect.bottom >= self.settings.height:
        # Treat this the same as if the ship got hit.
        self._ship_hit()
        break


  def _update_bullet(self):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    self.bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)
    
    self._check_bullet_alien_collisions()


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