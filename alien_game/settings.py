class Settings:
  def __init__(self) -> None:
    """Initialize the game's settings."""
    # Screen settings
    self.width = 800
    self.height = 600
    self.bg_color = (230,230,230)
    self.fps = 60

    self.ship_speed = 1.5