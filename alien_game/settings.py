class Settings:
  def __init__(self) -> None:
    """Initialize the game's settings."""
    # Screen settings
    self.width = 800
    self.height = 600
    self.bg_color = (230,230,230)
    self.fps = 60

    self.ship_speed = 1.5

    # Bullet settings
    self.bullet_speed = 2.0
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 3