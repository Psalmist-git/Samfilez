class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 5

        # Bullet settings
        self.bullet_speed = 7
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1
        self.alien_speedup = 0.3
        self.fleet_drop_speed = 20
        self.fleet_direction = 1

        # Wave settings
        self.wave_number = 1
        self.aliens_per_wave = 10