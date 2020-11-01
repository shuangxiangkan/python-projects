class Settings():
    def __init__(self):
        # Initialize the data
        self.screen_width = 1000
        self.screen_heigh = 600
        self.bg_color = (230, 230, 230)

        # Set the moving distance each time
        self.ship_move_distance = 1
        self.ships_limit=3

        # Set the initial data of a bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 1
        self.bullet_color = (60, 60, 60)

        # Set the initial data of a alien
        self.alien_speed_factor=1
        self.alien_moving_direction=1
        self.alien_moving_down_distance=10