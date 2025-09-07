import sys
import pygame as pg

from settings import Settings
from ship import Ship
class AlienInvasion:

  def __init__(self) -> None:
    pg.init()
    self.clock = pg.time.Clock()
    self.settings = Settings()
    self.screen = pg.display.set_mode((self.settings.width, self.settings.height))
    pg.display.set_caption("Alien Invasion")

    self.ship = Ship(self)

  def run_game(self):
    while True:
      self._check_event()
      self.ship.moving_ship()
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


  def _check_keyup_event(self, event):
    if event.key == pg.K_RIGHT:
      self.ship.moving_right = False
    elif event.key == pg.K_LEFT:
      self.ship.moving_left = False


  def _update_screen(self):
    self.screen.fill(self.settings.bg_color)
    self.ship.draw_ship()
    pg.display.flip()
    

if __name__ == "__main__":
  game = AlienInvasion()
  game.run_game()