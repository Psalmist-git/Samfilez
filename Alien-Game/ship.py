import pygame


class Ship:
    """Manage the player's spaceship."""

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        # Get the screen rectangle.
        self.screen_rect = screen.get_rect()

        # Create a rectangle for positioning.
        self.rect = pygame.Rect(0, 0, 60, 50)

        # Place the ship at the bottom center.
        self.rect.midbottom = self.screen_rect.midbottom

        # Use a floating-point position for smooth movement.
        self.x = float(self.rect.x)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Move the ship according to the movement flags."""

        if self.moving_right:
            self.x += self.settings.ship_speed

        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Keep the ship inside the screen.
        max_x = self.screen_rect.right - self.rect.width

        self.x = max(0, min(self.x, max_x))

        # Update the rectangle position.
        self.rect.x = round(self.x)

    def blitme(self):
        """Draw a simple spaceship."""

        # Ship body.
        pygame.draw.polygon(
            self.screen,
            (60, 100, 220),
            [
                self.rect.midtop,
                self.rect.bottomleft,
                (self.rect.centerx, self.rect.bottom - 12),
                self.rect.bottomright,
            ],
        )

        # Cockpit.
        pygame.draw.ellipse(
            self.screen,
            (100, 220, 255),
            (
                self.rect.centerx - 8,
                self.rect.y + 15,
                16,
                20,
            ),
        )
        