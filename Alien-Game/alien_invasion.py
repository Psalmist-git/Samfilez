import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet


def create_fleet(settings, screen, aliens, ship):
    """Create a fleet with more aliens in each wave."""

    alien = Alien(settings, screen)

    alien_width = alien.rect.width
    alien_height = alien.rect.height

    # Calculate how many aliens fit in each row.
    available_x = settings.screen_width - 2 * alien_width
    number_aliens_x = available_x // (2 * alien_width)

    # Calculate how many rows fit above the ship.
    available_y = (
        settings.screen_height
        - 3 * alien_height
        - ship.rect.height
    )

    number_rows = available_y // (2 * alien_height)

    # Prevent division by zero if the screen is too small.
    if number_aliens_x <= 0 or number_rows <= 0:
        print("The screen is too small for an alien fleet.")
        return

    # Calculate the maximum number of aliens that fit.
    max_aliens = number_aliens_x * number_rows

    # Increase the number of aliens with each wave.
    desired_aliens = (
        settings.aliens_per_wave * settings.wave_number
    )

    total_aliens = min(desired_aliens, max_aliens)

    # Create aliens in rows and columns.
    for alien_number in range(total_aliens):
        row_number = alien_number // number_aliens_x
        column_number = alien_number % number_aliens_x

        alien = Alien(settings, screen)

        alien.x = alien_width + 2 * alien_width * column_number
        alien.rect.x = round(alien.x)

        alien.rect.y = (
            alien_height + 2 * alien_height * row_number
        )

        aliens.add(alien)

    print(
        f"Created {total_aliens} aliens "
        f"for Wave {settings.wave_number}."
    )


def increase_difficulty(settings):
    """Increase the difficulty after each completed wave."""

    settings.wave_number += 1
    settings.alien_speed += settings.alien_speedup

    print(f"\nWave {settings.wave_number} starting!")
    print(
        f"Aliens requested: "
        f"{settings.aliens_per_wave * settings.wave_number}"
    )
    print(f"Alien speed: {settings.alien_speed:.1f}")


def check_fleet_edges(settings, aliens):
    """Reverse the fleet direction when an alien reaches an edge."""

    for alien in aliens:
        if (
            alien.rect.right >= settings.screen_width
            and settings.fleet_direction == 1
        ):
            settings.fleet_direction = -1
            drop_fleet(aliens, settings)
            return

        elif (
            alien.rect.left <= 0
            and settings.fleet_direction == -1
        ):
            settings.fleet_direction = 1
            drop_fleet(aliens, settings)
            return


def drop_fleet(aliens, settings):
    """Move all aliens down."""

    for alien in aliens:
        alien.rect.y += settings.fleet_drop_speed

        # Keep the alien's stored vertical position in sync.
        if hasattr(alien, "y"):
            alien.y = float(alien.rect.y)


def update_aliens(settings, aliens, ship):
    """Move the fleet and check whether aliens reach the ship."""

    check_fleet_edges(settings, aliens)

    # Move every alien in the group.
    aliens.update()

    # Check whether an alien has reached the ship.
    for alien in aliens:
        if alien.rect.bottom >= ship.rect.top:
            return True

    return False


def run_game():
    """Run Alien Invasion."""

    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    # Create the ship.
    ship = Ship(screen, settings)

    # Create the alien group and bullet list.
    aliens = Group()
    bullets = []

    # Create the first fleet.
    create_fleet(settings, screen, aliens, ship)

    # Prepare the wave display.
    font = pygame.font.SysFont(None, 36)
    game_over_font = pygame.font.SysFont(None, 72)

    running = True
    game_over = False

    # Main game loop.
    while running:

        # Handle keyboard and window events.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if not game_over:

                    if event.key == pygame.K_RIGHT:
                        ship.moving_right = True

                    elif event.key == pygame.K_LEFT:
                        ship.moving_left = True

                    elif event.key == pygame.K_SPACE:

                        if len(bullets) < settings.bullets_allowed:
                            new_bullet = Bullet(
                                screen,
                                settings,
                                ship
                            )

                            bullets.append(new_bullet)

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

        # Update the game while it is not over.
        if not game_over:

            # Move the ship.
            ship.update()

            # Move bullets and remove those off-screen.
            for bullet in bullets[:]:
                bullet.update()

                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)

            # Detect bullets hitting aliens.
            for bullet in bullets[:]:

                hit_aliens = pygame.sprite.spritecollide(
                    bullet,
                    aliens,
                    True
                )

                if hit_aliens and bullet in bullets:
                    bullets.remove(bullet)

            # Start a new wave when all aliens are destroyed.
            if len(aliens) == 0:
                bullets.clear()

                increase_difficulty(settings)

                settings.fleet_direction = 1

                create_fleet(
                    settings,
                    screen,
                    aliens,
                    ship
                )

            # Move aliens and detect game over.
            if update_aliens(settings, aliens, ship):
                game_over = True
                print("Game over! An alien reached your ship.")

        # Draw the background.
        screen.fill(settings.bg_color)

        # Draw the ship and alien fleet.
        ship.blitme()
        aliens.draw(screen)

        # Draw bullets.
        for bullet in bullets:
            bullet.draw_bullet()

        # Display the current wave.
        wave_text = font.render(
            f"Wave: {settings.wave_number}",
            True,
            (0, 0, 0)
        )

        screen.blit(wave_text, (20, 20))

        # Display the game-over message.
        if game_over:
            message = game_over_font.render(
                "GAME OVER",
                True,
                (200, 0, 0)
            )

            message_rect = message.get_rect(
                center=(
                    settings.screen_width // 2,
                    settings.screen_height // 2
                )
            )

            screen.blit(message, message_rect)

        # Update the display.
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run_game()
    