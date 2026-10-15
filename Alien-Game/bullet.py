import pygame


class Bullet:
    """Manage bullets fired by the spaceship."""

    def __init__(self, screen, settings, ship):
        self.screen = screen
        self.settings = settings

        # Create a bullet rectangle.
        self.rect = pygame.Rect(
            0,
            0,
            settings.bullet_width,
            settings.bullet_height,
        )

        # Start the bullet at the top of the ship.
        self.rect.midbottom = ship.rect.midtop

        # Store the vertical position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet upward."""

        self.y -= self.settings.bullet_speed
        self.rect.y = round(self.y)

    def draw_bullet(self):
        """Draw the bullet on the screen."""

        pygame.draw.rect(
            self.screen,
            self.settings.bullet_color,
            self.rect,
        )